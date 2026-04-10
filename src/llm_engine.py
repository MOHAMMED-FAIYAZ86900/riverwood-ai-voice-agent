import os
import requests
from dotenv import load_dotenv
from src.prompts import SYSTEM_PROMPT

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_response(user_input, history):

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(history)

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/llama-3.1-8b-instruct",
            "messages": messages,
            "max_tokens": 80
        }
    )

    data = response.json()

    # Debug print if something goes wrong
    if "choices" not in data:
        print("OpenRouter Error Response:", data)
        return "Sorry, I am having trouble generating a response right now."

    return data["choices"][0]["message"]["content"]