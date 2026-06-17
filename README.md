# 🧠 Mental Health Companion Chatbot

A simple, beginner-friendly AI chatbot built with **Python**, **Streamlit**,
and the **Google Gemini API** to support student mental well-being.

## ⚠️ Disclaimer

This chatbot is designed to offer supportive conversation, mood-based
encouragement, and general relaxation tips. **It is not a substitute for
professional mental health care.** It does not diagnose any mental health
condition. If you or someone you know is in crisis, please contact a
licensed mental health professional or local emergency services
immediately.

## 📋 Project Description

Students often face high levels of stress, anxiety, and loneliness but
may hesitate to approach professional counselors. This project provides
a safe, simple AI-powered chatbot that:

- Listens to what a student is feeling.
- Detects their mood using keyword-based analysis.
- Generates empathetic, motivational responses using Google Gemini.
- Suggests relevant relaxation tips.
- Watches for harmful/crisis keywords and responds with a safety message.

## ✨ Features

1. **AI Chatbot** — A ChatGPT-style conversational interface where users
   can type their thoughts and feelings, with full conversation history
   maintained during the session.
2. **Mood Detection** — Detects moods such as Happy, Sad, Stressed,
   Anxious, and Lonely using simple keyword-based analysis.
3. **Relaxation Tips** — Offers mood-specific wellness tips (e.g., deep
   breathing for stress, grounding techniques for anxiety).
4. **Motivational Responses** — Shares encouraging, positive messages
   tailored to the user's mood.
5. **Safety Feature** — Detects harmful keywords (e.g., "suicide",
   "self-harm", "kill myself") and immediately displays a message
   encouraging the user to seek help from a trusted person or
   professional, instead of generating a normal chatbot reply.

## 🛠️ Technologies Used

- **Python 3.10+**
- **Streamlit** — for the web-based chat interface
- **Google Gemini API** (`google-genai`) — for generating
  empathetic AI responses
- Standard Python libraries (`random`)

## 📁 Project Structure

```
mental_health_companion/
├── app.py                     # Main Streamlit application
├── chatbot.py                 # Handles Gemini API communication
├── mood_detection.py          # Keyword-based mood & safety detection
├── relaxation_tips.py         # Mood-based relaxation tips
├── motivational_messages.py   # Mood-based motivational messages
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## 🔑 Gemini API Setup

This project uses the Google Gemini API to generate chatbot responses.

1. Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/).
2. Open `chatbot.py`.
3. Replace the placeholder with your own key:

   ```python
   API_KEY = "YOUR_GEMINI_API_KEY"
   ```

   with:

   ```python
   API_KEY = "your-actual-api-key-here"
   ```

> If the API key is missing or invalid, the app will still run and show
> a friendly fallback message instead of crashing.

> **Note:** This project uses the `google-genai` package, which is
> Google's current, actively maintained Gemini SDK. The older
> `google-generativeai` package has been fully deprecated by Google and
> no longer receives updates.

## 💻 Installation Steps

1. **Clone or download** this project folder to your computer.

2. **(Optional but recommended)** Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Gemini API key** in `chatbot.py` as described above.

## ▶️ Running the App

From inside the project folder, run:

```bash
python -m streamlit run app.py
```

Streamlit will start a local server and open the app in your default
web browser (usually at `http://localhost:8501`).

## 💬 Example Messages to Try

- "I am stressed about exams."
- "I feel anxious."
- "I feel lonely."
- "I am feeling sad."
- "I am worried about placements."

## 🤝 A Final Note

Talking to this chatbot can be a helpful first step, but please remember
that real human connection and professional support matter. If you're
struggling, reaching out to a friend, family member, counselor, or
mental health professional can make a real difference.
