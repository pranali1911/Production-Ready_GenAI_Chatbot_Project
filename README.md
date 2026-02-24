
# 🤖 Production-Ready GenAI Career Advisor Chatbot

A domain-specific Generative AI chatbot built to help users with career-related tasks such as resume review, interview preparation, job search guidance, and skill roadmap suggestions.  
The chatbot uses structured prompt engineering and is deployed as a Streamlit web application.

---

## 🚀 Features
- Career-focused AI assistant (resume, interview, job search, skill roadmap)
- Structured system prompts with role-based instructions
- Reusable prompt builder for configurable prompts
- Session-based conversation memory
- Simple and clean Streamlit UI
- Production-ready setup using environment variables for API keys

---

## 🛠️ Tech Stack
- Python  
- Streamlit  
- Gemini API (LLM)  
- Prompt Engineering  
- dotenv (for environment variables)

---

## 📂 Project Structure
```

GenAI-Career-Advisor-Chatbot/
│
├── app.py                  # Main Streamlit app
├── prompts/
│   └── career_prompts.py   # System prompts & prompt builder
├── requirements.txt
├── .env.example            # Sample env file
└── README.md

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/GenAI-Career-Advisor-Chatbot.git
cd GenAI-Career-Advisor-Chatbot
````

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv genai_env
# On Windows:
genai_env\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 5️⃣ Run the App

```bash
streamlit run app.py
```

---

## 📌 Example Use Cases

* Improve your resume with AI feedback
* Prepare for interviews with tailored questions
* Analyze job descriptions and skill gaps
* Get a learning roadmap for Data Analyst / Data Scientist roles

---

## 🧪 Sample Prompt

> "Make a roadmap for becoming a Data Analyst."

---

## 🔒 Notes

* Do NOT commit your `.env` file or API keys.
* Prompts are configurable inside `prompts/career_prompts.py`.

---

## 📸 Screenshots

<img width="1906" height="865" alt="Screenshot 2026-02-24 225646" src="https://github.com/user-attachments/assets/d033eec3-1437-4015-9ff0-652efb7a92bc" />
.



