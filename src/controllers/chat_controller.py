from prompts.career_prompts import build_prompt
from src.config.setting import HISTORY_LAST_N
from src.services.gemini_service import generate_answer

# # Token optimization + memory handling
def history_to_text(messages, last_n=HISTORY_LAST_N):
    text = ""
    for m in messages[-last_n:]:
        role = "User" if m["role"] == "user" else "Assistant"
        text += f"{role}: {m['content']}\n"
    return text.strip()

# # Main controller function
def handle_user_message(client, messages, user_input: str) -> str:
    history_text = history_to_text(messages)
    final_prompt = build_prompt(user_input, history_text)
    return generate_answer(client, final_prompt)