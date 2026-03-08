import os
import sys
import logging
import streamlit as st
from google import genai
from dotenv import load_dotenv

# Fix import path for prompts/
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from prompts.career_prompts import SYSTEM_PROMPT, build_prompt
from src.services.gemini_service import get_client
from src.controllers.chat_controller import handle_user_message

# Load env
load_dotenv()

# Load API key safely
os.environ['GOOGLE_API_KEY'] = os.getenv("Gemini_class_1")

# -----------------------------
# Simple logging (Step 3)
# -----------------------------
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger("career_bot")

# # Initialize Gemini client once (session-based)
if "client" not in st.session_state:
    st.session_state.client = genai.Client()
client = st.session_state.client

# -----------------------------
# # Streamlit UI config
# -----------------------------
st.set_page_config(page_title="Career Advisor Chatbot")
st.title("💼 Career Advisor Chatbot")

# Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Convert history to text (simple multi-turn memory)
def history_to_text(messages, last_n=8):
    text = ""
    for m in messages[-last_n:]:
        role = "User" if m["role"] == "user" else "Assistant"
        text += f"{role}: {m['content']}\n"
    return text.strip()

# Show history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask about resume, interview, job emails...")

if user_input:
    # # Save user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            history_text = history_to_text(st.session_state.messages)
            final_prompt = build_prompt(user_input, history_text)

            try:
                # # Log API call start
                logger.info("Calling Gemini API...")

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=final_prompt
                )

                answer = (response.text or "").strip()

                # # Log API success
                logger.info("Gemini API success")

                # # Fallback if empty response
                if not answer:
                    answer = "⚠️ I could not generate a response. Please try again."

            except Exception as e:
                # # Log full error
                logger.exception("Gemini API error")

                # # User-friendly fallback message
                answer = "⚠️ Something went wrong while generating the response. Please try again in a moment."

            st.markdown(answer)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})

if st.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# -----------------------------
# # Sidebar for user-friendly layout (Optional)
# -----------------------------
with st.sidebar:
    st.header("⚙️ Help")
    st.write("Ask about resume, interview, job emails, JD analysis.")

with st.sidebar:
    st.subheader("🕘 Chat History (last 5)")
    for msg in st.session_state.messages[-5:]:
        st.write(f"{msg['role']}: {msg['content'][:50]}...")                   
        
        
