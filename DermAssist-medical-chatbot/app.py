

from fastapi import FastAPI, File, UploadFile, Form, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse

import base64
import requests
import io

from PIL import Image
from dotenv import load_dotenv

import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ API key is not set in the .env file")

# Chat history per session (in-memory)
session_chats = {}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    session_id = request.cookies.get("session_id", os.urandom(8).hex())
    response = templates.TemplateResponse("index.html", {"request": request, "session_id": session_id})
    response.set_cookie("session_id", session_id)
    return response

@app.post("/upload_and_query")
async def upload_and_query(
    request: Request,
    image: UploadFile = File(...),
    query: str = Form(...),
    session_id: str = Form(...)
):
    try:
        image_content = await image.read()
        if not image_content:
            raise HTTPException(status_code=400, detail="empty file")

        encoded_image = base64.b64encode(image_content).decode("utf-8")

        try:
            img = Image.open(io.BytesIO(image_content))
            img.verify()
        except Exception as e:
            logger.error(f"Invalid image format: {str(e)}")
            raise HTTPException(status_code=400, detail=f"Invalid image format: {str(e)}")

        # First-time prompt injection
        if session_id not in session_chats or not session_chats[session_id]:
            modified_query = f"""
{query.strip()}

Please:
1. Identify the skin condition in the image.
2. Give a concise explanation (max 3 lines).
3. In a **separate section**, list **Pakistani market-available drugs** used to treat it:
    - Use table format with: Generic name | Pakistani Brand | Type | Estimated PKR price
    - Only list **essential** medications (not all possible).
    - At the end, include a **subtotal** in PKR.

Format it like:

---
### 🧾 Diagnosis & Explanation
<Short explanation here>

---
### 💊 Recommended Treatment (Pakistani Market)
| Drug | Brand | Type | PKR Price |
...
Subtotal: PKR xxx

Add no extra description. Be concise.
"""
        else:
            modified_query = query.strip()

        user_message = {
            "role": "user",
            "content": [
                {"type": "text", "text": modified_query},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
            ]
        }

        if session_id not in session_chats:
            session_chats[session_id] = []

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
            logger.error(f"Error from meta-llama API: {response.status_code} - {response.text}")
            return JSONResponse(status_code=response.status_code, content={"error": response.text})

    except HTTPException as he:
        logger.error(f"HTTP Exception: {str(he)}")
        raise he
    except Exception as e:
        logger.error(f"Unexpected error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error occurred: {str(e)}")

@app.post("/continue_chat")
async def continue_chat(query: str = Form(...), session_id: str = Form(...)):
    try:
        if session_id not in session_chats:
            raise HTTPException(status_code=400, detail="No existing chat session found")

        # Inject brevity instruction
        modified_query = f"""{query.strip()}

Please respond in **50 words or fewer**. Be concise and factual. No summaries or extra elaboration."""

        user_message = {"role": "user", "content": modified_query}
        session_chats[session_id].append(user_message)

        response = requests.post(
            GROQ_API_URL,
            json={
                "model": "meta-llama/llama-4-scout-17b-16e-instruct",
                "messages": session_chats[session_id],
                "max_tokens": 300  # Encourage brevity
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
            logger.error(f"Error from meta-llama API: {response.status_code} - {response.text}")
            return JSONResponse(status_code=response.status_code, content={"error": response.text})

    except Exception as e:
        logger.error(f"Error in continued chat: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error in continued chat: {str(e)}")

@app.post("/clear_chat")
async def clear_chat(session_id: str = Form(...)):
    session_chats[session_id] = []
    return JSONResponse(content={"message": "Chat history cleared."})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
