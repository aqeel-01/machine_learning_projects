

#  DermAssist – AI-Powered Skin Condition Chatbot

DermAssist is an AI-driven medical chatbot built using **FastAPI** and **LLAMA-4 (via GROQ)**. It enables users to upload a **skin condition image**, ask health-related queries, and receive a **diagnosis with treatment recommendations tailored for the Pakistani market**.

---

##  Live Demo

>  Upload an image →  Ask a question →  Get an AI-powered diagnosis and treatment.

---

##  Features

-  **AI-Powered Skin Condition Analysis**  
-  Upload **skin images** and get diagnosis
-  Ask follow-up **text queries**
-  **Local drug recommendations** in **tabular format**
-  Built with **FastAPI + Tailwind CSS + LLAMA-4 (GROQ API)**
-  Pakistani pharmaceutical market data (estimates)

---

##  Screenshots

###  Upload & Ask

![Upload and Ask](screenshots/chatbot%20pic1.PNG)



###  AI Chat Response
![Chatbot Response](screenshots/chatbot%20pic2.PNG)

---

##  Demo Video

[ Click here to view screen recording demo](demo/screenrecording.mp4)

<!-- Optional image link -->
<!-- [![Watch Demo](screenshots/chatbotpic1.png)](demo/screenrecording.mp4) -->

---

##  Getting Started
```
### 1. Clone the Repository



### 2. Install Dependencies

Make sure you have Python 3.8+ installed.


pip install -r requirements.txt

### 3. Configure .env

Create a .env file in the project root with your GROQ API Key:


GROQ_API_KEY=your_groq_api_key_here

### 4. Run the App

uvicorn app:app --reload
Visit: http://127.0.0.1:8000
```
##  Project Structure

```
dermassist/
│
├── app.py                   # FastAPI backend
├── templates/
│   └── index.html           # Frontend (Tailwind + JS)
├── screenshots/
│   ├── chatbotpic1.png      # Upload screen
│   └── chatbotpic2.png      # Response screen
├── demo/
│   └── screenrecording.mp4  # Demo video (linked in README)
├── .env                     # API key (not committed)
└── requirements.txt         # Dependencies

```

##  How It Works

On image upload, the system:

Encodes the image in base64

Sends it to the LLAMA-4 Scout model via the GROQ API

Requests a concise diagnosis + treatment table (localized to Pakistan)

Continues chat in 50-word or fewer responses for clarity

Persists chat in memory per session ID via cookies


##  Technologies Used

FastAPI

GROQ + LLAMA-4

Tailwind CSS

Pillow

JavaScript Fetch API

