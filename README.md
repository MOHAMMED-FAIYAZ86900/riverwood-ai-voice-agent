# 🎙️ Riverwood AI Voice Agent

An AI-powered voice assistant that simulates real estate customer interactions for **Riverwood Estate**.  
This system can greet users, provide construction updates, answer queries, and maintain natural conversations using voice.

---

## 🚀 Overview

This project demonstrates a **human-like AI voice agent** capable of:

- Making conversational interactions with customers
- Providing project updates (e.g., construction progress)
- Handling user queries in real-time
- Responding with natural-sounding speech

It is designed as a prototype for an **AI-powered CRM system in real estate**.

---

## ✨ Features

- 🎤 **Speech-to-Text**: Converts user voice into text
- 🤖 **LLM Integration**: Generates contextual responses using OpenRouter
- 🔊 **Text-to-Speech**: Converts responses into natural voice using ElevenLabs
- 💬 **Conversation Memory**: Maintains multi-turn context
- 🌐 **Multilingual Support**: Handles English and basic Hindi inputs
- ⚡ **Low Latency Interaction**: Fast response pipeline

---

## 🧠 System Architecture
User Voice
↓
Speech Recognition (SpeechRecognition)
↓
Conversation Manager
↓
LLM (OpenRouter - LLaMA / Mistral)
↓
Text-to-Speech (ElevenLabs)
↓
Audio Response


---

## 🛠️ Tech Stack

| Component            | Technology Used |
|---------------------|----------------|
| Programming         | Python         |
| LLM API             | OpenRouter     |
| Speech Recognition  | SpeechRecognition |
| Text-to-Speech      | ElevenLabs     |
| HTTP Requests       | Requests       |
| Environment Config  | python-dotenv  |

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/riverwood-ai-voice-agent.git
cd riverwood-ai-voice-agent



2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file in the root directory:

OPENROUTER_API_KEY=your_openrouter_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key

⚠️ Do not upload .env to GitHub.

▶️ Running the Application
python app.py

💬 Example Interaction

AI:
Hello! This is Riverwood Estate calling with an update about your plot.

User:
Can you tell me about the construction progress?

AI:
Construction work is progressing well this month. Are you planning to visit the site soon?

📊 Scalability Design (1000 Calls Scenario)

To handle large-scale operations such as calling 1000 customers:

📦 Queue System: Kafka / Redis Queue for task distribution
⚙️ Worker Nodes: Parallel processing of calls
☎️ Telephony Integration: Twilio API for call handling
☁️ Cloud Deployment: Docker + Kubernetes for scaling
🚀 Future Improvements
📞 Real-time phone call integration (Twilio)
🧠 Advanced memory using vector databases (RAG)
🌍 Improved multilingual support
🎨 Web UI using Streamlit
📊 Analytics dashboard for CRM insights
👨‍💻 Author

Mohammed Faiyaz
AI & ML Engineering Student
RV College of Engineering, Bengaluru

🔗 LinkedIn: https://www.linkedin.com/in/mohammed-faiyaz-b49167291/

⭐ Acknowledgment

This project was built as part of the Riverwood AI Systems Internship Challenge, focusing on real-world AI system design and implementation.
