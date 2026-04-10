from src.speech_to_text import listen_to_user
from src.llm_engine import generate_response
from src.text_to_speech import speak_text
from src.memory_manager import save_conversation, get_conversation_history

history = []

def start_voice_agent():
    speak_text("Hello! This is Riverwood Estate calling with an update about your plot.")

    print("Riverwood AI Voice Agent Started")

    while True:

        user_input = listen_to_user()

        if user_input.lower() in ["exit", "stop", "quit"]:
            print("Ending conversation.")
            break

        conversation_history = get_conversation_history()

        response = generate_response(user_input, conversation_history)

        print("AI:", response)

        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": response})

        save_conversation(user_input, response)

        speak_text(response)