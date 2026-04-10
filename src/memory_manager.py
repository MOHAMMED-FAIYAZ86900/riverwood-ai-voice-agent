# Simple conversation memory

conversation_history = []

def save_conversation(user_input, ai_response):

    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    conversation_history.append({
        "role": "assistant",
        "content": ai_response
    })


def get_conversation_history():
    return conversation_history