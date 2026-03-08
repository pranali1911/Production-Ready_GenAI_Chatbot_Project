import os
from google import genai
from src.config.setting import GEMINI_API_KEY, MODEL_NAME

# # Gemini API handling (separate from UI)
def get_client():
    os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
    return genai.Client()

def generate_answer(client, final_prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=final_prompt
        )
        answer = (response.text or "").strip()

        # # Fallback if empty
        if not answer:
            return "⚠️ I could not generate a response. Please try again."

        return answer

    except Exception:
        return "⚠️ Something went wrong. Please try again."