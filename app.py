"""
app.py

Main Streamlit application file for the Mental Health Companion Chatbot.

This app provides a simple, beginner-friendly chat interface where
students can express their thoughts and feelings. It detects the user's
mood, checks for harmful/crisis keywords, and generates empathetic
responses using the Google Gemini API, along with relaxation tips and
motivational messages.

IMPORTANT DISCLAIMER:
This chatbot is NOT a substitute for professional mental health care.
It does not diagnose conditions and cannot replace a licensed
counselor, therapist, or doctor.
"""

import streamlit as st

from chatbot import get_chatbot_response
from mood_detection import detect_mood, detect_harmful_content
from relaxation_tips import get_relaxation_tip
from motivational_messages import get_motivational_message


# ---------------------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="Mental Health Companion Chatbot",
    page_icon="🧠",
    layout="centered",
)


# ---------------------------------------------------------------------
# Safety message shown when harmful keywords are detected
# ---------------------------------------------------------------------
SAFETY_MESSAGE = (
    "🚨 **Please reach out to a trusted person or a mental health "
    "professional immediately.** If you are in immediate danger, "
    "please contact your local emergency services right away. "
    "You are not alone, and support is available."
)


def initialize_session_state():
    """
    Initialize Streamlit session state variables if they don't already
    exist. This keeps the conversation history persistent across
    reruns of the app within the same session.
    """
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Add a friendly welcome message from the assistant
        st.session_state.messages.append({
            "role": "assistant",
            "content": (
                "Hi there! 👋 I'm your Mental Health Companion. "
                "I'm here to listen and support you. "
                "How are you feeling today?"
            ),
        })


def display_disclaimer():
    """Display a short disclaimer at the top of the app."""
    st.caption(
        "⚠️ This chatbot offers supportive conversation and general "
        "wellness tips. It is **not** a replacement for professional "
        "mental health care. If you are in crisis, please contact a "
        "professional or local emergency services."
    )


def display_chat_history():
    """Render all previous messages in the conversation as chat bubbles."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def handle_user_message(user_input: str):
    """
    Process a new user message: check for safety concerns, detect mood,
    generate a chatbot response, and update the conversation history.

    Args:
        user_input (str): The message typed by the user.
    """
    try:
        # Add the user's message to the chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # 1. Safety check: look for harmful/crisis keywords first
        if detect_harmful_content(user_input):
            st.session_state.messages.append({
                "role": "assistant",
                "content": SAFETY_MESSAGE,
            })
            return

        # 2. Detect the user's mood from their message
        mood = detect_mood(user_input)

        # 3. Generate an empathetic response using the Gemini API
        ai_response = get_chatbot_response(user_input, mood)

        # 4. Get a relevant relaxation tip and motivational message
        tip = get_relaxation_tip(mood)
        motivation = get_motivational_message(mood)

        # 5. Combine everything into one assistant reply
        mood_label = mood.capitalize() if mood != "neutral" else "Neutral"
        full_response = (
            f"{ai_response}\n\n"
            # f"**Detected mood:** {mood_label} 🧭\n\n"
            # f"💡 **Relaxation tip:** {tip}\n\n"
            # f"🌟 **Remember:** {motivation}"
        )

        st.session_state.messages.append({
            "role": "assistant",
            "content": full_response,
        })

    except Exception as error:
        # Catch-all to keep the app from crashing on unexpected errors
        st.session_state.messages.append({
            "role": "assistant",
            "content": (
                "I'm sorry, something went wrong while processing your "
                f"message. Please try again. (Error: {error})"
            ),
        })


def main():
    """Main function that runs the Streamlit app."""
    # ---- Header ----
    st.title("🧠 Mental Health Companion Chatbot")
    st.subheader("A safe space to share your thoughts and feelings 💬")
    display_disclaimer()
    st.divider()

    # ---- Initialize and display chat ----
    initialize_session_state()
    display_chat_history()

    # ---- Chat input box ----
    user_input = st.chat_input("Type how you're feeling... 📝")

    if user_input:
        # Display the user's message immediately
        with st.chat_message("user"):
            st.markdown(user_input)

        # Show a spinner while generating the response
        with st.chat_message("assistant"):
            with st.spinner("Thinking... 🤔"):
                handle_user_message(user_input)
                # Display only the latest assistant message
                st.markdown(st.session_state.messages[-1]["content"])

    # ---- Sidebar with extra info ----
    with st.sidebar:
        st.header("ℹ️ About")
        st.write(
            "This chatbot listens to your feelings, detects your mood, "
            "and offers supportive, empathetic responses along with "
            "relaxation tips and motivational messages."
        )
        st.write(
            "**Examples you can try:**\n"
            "- I am stressed about exams.\n"
            "- I feel anxious.\n"
            "- I feel lonely.\n"
            "- I am feeling sad.\n"
            "- I am worried about placements."
        )
        st.divider()
        st.warning(
            "🚨 If you are in crisis or having thoughts of self-harm, "
            "please contact a mental health professional or local "
            "emergency services immediately."
        )
        st.divider()
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.rerun()


if __name__ == "__main__":
    main()
