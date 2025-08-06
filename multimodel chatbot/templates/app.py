


from fastapi import FastAPI, File, UploadFile, Form, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse

import base64
import requests
import io
import tempfile
import os
import logging

from PIL import Image
from PyPDF2 import PdfReader
from dotenv import load_dotenv

import cv2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ API key is not set in the .env file")

session_chats = {}

def extract_frames(video_bytes, frame_count=5):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(video_bytes)
        temp_video_path = temp_video.name

    cap = cv2.VideoCapture(temp_video_path)
    frames = []
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_indices = [int(i * total_frames / frame_count) for i in range(frame_count)]

    for idx in frame_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if ret:
            _, buffer = cv2.imencode('.jpg', frame)
            frames.append(buffer.tobytes())

    cap.release()
    os.unlink(temp_video_path)
    return frames

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    session_id = request.cookies.get("session_id", os.urandom(8).hex())
    response = templates.TemplateResponse("index.html", {"request": request, "session_id": session_id})
    response.set_cookie("session_id", session_id)
    return response

@app.post("/upload_and_query")
async def upload_and_query(request: Request, file: UploadFile = File(...), query: str = Form(...), session_id: str = Form(...)):
    try:
        file_content = await file.read()
        if not file_content:
            raise HTTPException(status_code=400, detail="Empty file uploaded.")

        file_type = file.content_type
        user_message_content = [{"type": "text", "text": query.strip()}]

        if file_type.startswith("image/"):
            encoded_image = base64.b64encode(file_content).decode("utf-8")
            img = Image.open(io.BytesIO(file_content))
            img.verify()
            user_message_content.append({
                "type": "image_url",
                "image_url": {"url": f"data:{file_type};base64,{encoded_image}"}
            })

        elif file_type == "application/pdf":
            pdf_reader = PdfReader(io.BytesIO(file_content))
            extracted_text = ""
            for page in pdf_reader.pages[:5]:
                extracted_text += page.extract_text() or ""
            extracted_text = extracted_text[:4000]
            user_message_content[0]["text"] += (
                f"\n\nThe user has uploaded a PDF. Here is the extracted text for context:\n\n{extracted_text}\n\nPlease consider this while answering."
            )

        elif file_type.startswith("video/"):
            frames = extract_frames(file_content, frame_count=5)
            for frame_bytes in frames:
                encoded_frame = base64.b64encode(frame_bytes).decode("utf-8")
                user_message_content.append({
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{encoded_frame}"}
                })
            user_message_content[0]["text"] += "\n\nThe user has uploaded a video. Provided are 5 extracted frames for context. Please consider these while answering."
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type. Only images, PDFs, and videos are allowed.")

        if session_id not in session_chats:
            session_chats[session_id] = []

        system_message = {
            "role": "system",
            "content": "You are a helpful assistant. Please keep your response within 12 lines. It can be shorter."
        }
        session_chats[session_id].append(system_message)

        user_message = {"role": "user", "content": user_message_content}
        session_chats[session_id].append(user_message)

        response = requests.post(
            GROQ_API_URL,
            json={
                "model": "meta-llama/llama-4-scout-17b-16e-instruct",
                "messages": session_chats[session_id],
                "max_tokens": 1000
            },
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            }
        )

        if response.status_code == 200:
            result = response.json()
            assistant_message = result["choices"][0]["message"]
            session_chats[session_id].append(assistant_message)
            return JSONResponse(status_code=200, content={"llama": assistant_message["content"]})
        else:
            logger.error(f"Groq API error: {response.status_code} - {response.text}")
            return JSONResponse(status_code=response.status_code, content={"error": response.text})

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@app.post("/continue_chat")
async def continue_chat(query: str = Form(...), session_id: str = Form(...)):
    try:
        if session_id not in session_chats:
            raise HTTPException(status_code=400, detail="No existing chat session found.")

        system_message = {
            "role": "system",
            "content": "Please keep your response within 6 lines. It can be shorter."
        }
        session_chats[session_id].append(system_message)

        user_message = {"role": "user", "content": query.strip()}
        session_chats[session_id].append(user_message)

        response = requests.post(
            GROQ_API_URL,
            json={
                "model": "meta-llama/llama-4-scout-17b-16e-instruct",
                "messages": session_chats[session_id],
                "max_tokens": 600
            },
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            }
        )

        if response.status_code == 200:
            result = response.json()
            assistant_message = result["choices"][0]["message"]
            session_chats[session_id].append(assistant_message)
            return JSONResponse(status_code=200, content={"llama": assistant_message["content"]})
        else:
            logger.error(f"Groq API error: {response.status_code} - {response.text}")
            return JSONResponse(status_code=response.status_code, content={"error": response.text})

    except Exception as e:
        logger.error(f"Error continuing chat: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error continuing chat: {str(e)}")

@app.post("/clear_chat")
async def clear_chat(session_id: str = Form(...)):
    session_chats[session_id] = []
    return JSONResponse(content={"message": "Chat history cleared."})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)