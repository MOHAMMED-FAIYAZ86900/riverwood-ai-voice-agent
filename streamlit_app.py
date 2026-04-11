import streamlit as st
from src.llm_engine import generate_response
from src.memory_manager import get_conversation_history, save_conversation
from src.text_to_speech import generate_audio_file

st.set_page_config(page_title="Riverwood AI Agent")

st.title("🏡 Riverwood Estate AI Assistant")

st.markdown("""
Welcome! This AI assistant provides:

- 📊 Construction updates  
- 📍 Project information  
- 📅 Site visit assistance  

Ask anything below 👇
""")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask something")

if user_input:

    history = get_conversation_history()

    response = generate_response(user_input, history)

    save_conversation(user_input, response)

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("AI", response))

    # 🔊 Generate audio
    audio_file = generate_audio_file(response)

    # ▶️ Play in Streamlit
    st.audio(audio_file, format="audio/mp3")

# Show chat
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 AI:** {message}")