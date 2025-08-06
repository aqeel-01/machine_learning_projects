

#  MultiModal Scout 🪐

MultiModal Scout is a FastAPI-based web application that allows users to upload **images**, **PDFs**, or **videos** and query them using natural language. It uses **LLaMA-4 (via Groq)** to provide intelligent, context-aware responses by analyzing the uploaded content.

---

##  Screenshot

![MultiModal Scout UI](multimodel%20chatbot/screenshot/multimodel%20pic1.PNG)

---

##  Features

-  Upload **images**, **PDFs**, or **videos**
-  Ask contextual questions based on file content
-  Uses **Meta LLaMA 4 Scout (17B)** via **Groq API**
-  Extracts key frames from videos for AI analysis
-  Extracts text from PDFs for context
-  Maintains session history using browser storage
-  Beautiful UI built with **Tailwind CSS**

---

##  Installation
```
### 1. Clone the repository


cd multimodal-scout

### 2. Create and activate a virtual environment

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Set up environment variables

Create a .env file in the root directory:


GROQ_API_KEY=your_groq_api_key_here

You can get your API key from Groq.

##  Running the App

uvicorn app:app --reload

Open your browser and navigate to:

 http://127.0.0.1:8000

```

##  File Structure

```
.
├── app.py
├── templates/
│   └── index.html
├── multimodel chatbot/
│   └── screenshot/
│       └── multimodel pic1.PNG
├── .env
└── requirements.txt

```

##  Supported File Types
Type	Usage
 Image	Sent to LLaMA as base64-encoded inline image URLs
 PDF	Extracts up to 5 pages of text for context
 Video	Extracts 5 key frames and sends them as image context

##  How It Works

User uploads a file and submits a query.

The backend:

Extracts relevant content (text or images).

Packages it into a message payload.

Sends it to the Groq API (LLaMA 4).

The AI returns a contextual answer based on your file and query.

Response is displayed in the chat UI.

##  Clear Chat Sessions

The app stores session chats per session in memory and browser storage. Use the "🗑️ Clear Chat" button to reset your current session.

