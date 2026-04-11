# 🎙️ Riverwood AI Voice Agent

An AI-powered voice assistant that simulates real estate customer interactions for **Riverwood Estate**.  
This system can greet users, provide construction updates, answer queries, and respond using natural voice.

---

## 🚀 Overview

This project demonstrates a **human-like AI voice agent** capable of:

- Conversational interaction with customers
- Providing real-time construction updates
- Answering project-related queries
- Responding with natural voice output

It is designed as a prototype for an **AI-powered CRM system in real estate**.

---

## ✨ Features

- 🎤 **Speech-to-Text** (Microphone input)
- 🤖 **LLM Integration** (OpenRouter - LLaMA models)
- 🔊 **Text-to-Speech** (ElevenLabs)
- 🎧 **Audio Playback in UI**
- 💬 **Conversation Memory**
- 🌐 **Multilingual Support (English + Hindi)**
- 🖥️ **Streamlit Web Interface**

---

## 🧠 System Architecture

```

User (Voice/Text Input)
↓
Speech Recognition (SpeechRecognition)
↓
Conversation Manager
↓
LLM (OpenRouter - LLaMA)
↓
Text-to-Speech (ElevenLabs)
↓
Audio Output (Browser / Speaker)

````

---

## 🛠️ Tech Stack

| Component            | Technology Used |
|---------------------|----------------|
| Programming         | Python         |
| LLM API             | OpenRouter     |
| Speech Recognition  | SpeechRecognition |
| Text-to-Speech      | ElevenLabs     |
| UI Framework        | Streamlit      |
| HTTP Requests       | Requests       |
| Environment Config  | python-dotenv  |

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/MOHAMMED-FAIYAZ86900/riverwood-ai-voice-agent.git
cd riverwood-ai-voice-agent
````

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```
OPENROUTER_API_KEY=your_openrouter_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

⚠️ Do not upload `.env` to GitHub.

---

## ▶️ Run the Application

### 🖥️ Run Voice Agent (Terminal)

```bash
python app.py
```

---

### 🌐 Run Web UI (Streamlit)

```bash
streamlit run streamlit_app.py
```

Open in browser:

```
http://localhost:8501
```

---


## 💬 Example Interaction

**AI:**
Hello! This is Riverwood Estate calling with an update about your plot.

**User:**
Can you tell me about the construction progress?

**AI:**
Construction is progressing well this month. Are you planning to visit the site soon?

---

## 📊 Scalability Design (1000 Calls Scenario)

To handle large-scale operations such as calling 1000 customers:

* 📦 **Queue System**: Kafka / Redis Queue
* ⚙️ **Worker Nodes**: Parallel processing
* ☎️ **Telephony Integration**: Twilio API
* ☁️ **Cloud Deployment**: Docker + Kubernetes

---

## 🚀 Future Improvements

* 📞 Real-time phone call integration (Twilio)
* 🧠 RAG-based memory with vector database
* 🌍 Advanced multilingual support
* 📊 CRM analytics dashboard

---

## 👨‍💻 Author

**Mohammed Faiyaz**
AI & ML Engineering Student
RV College of Engineering, Bengaluru

🔗 LinkedIn: [https://www.linkedin.com/in/mohammed-faiyaz-b49167291/](https://www.linkedin.com/in/mohammed-faiyaz-b49167291/)

---

## ⭐ Acknowledgment

Built as part of the **Riverwood AI Systems Internship Challenge**, focusing on real-world AI system design and implementation.

---

````
