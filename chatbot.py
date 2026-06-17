"""
chatbot.py

This file handles communication with the Google Gemini API to generate
empathetic, supportive, and motivational responses for the Mental Health
Companion Chatbot.

Replace the API_KEY placeholder below with your own Gemini API key
before running the application.

Note: This uses the `google-genai` package (the current, actively
maintained Google Gemini SDK). The older `google-generativeai` package
has been fully deprecated by Google and is no longer receiving updates.
"""

from google import genai
from google.genai import types

# ---------------------------------------------------------------------
# Gemini API Configuration
# Replace "YOUR_GEMINI_API_KEY" with your own API key.
# ---------------------------------------------------------------------
API_KEY = "YOUR_GEMINI_API_KEY"

# Name of the Gemini model to use for generating responses.
MODEL_NAME = "gemini-2.5-flash"

# How long (in milliseconds) to wait for the API before giving up and
# showing a fallback message. This keeps the app from freezing if the
# API key is invalid or there is no internet connection.
REQUEST_TIMEOUT_MS = 15000

# System-style instruction that shapes how the chatbot behaves.
SYSTEM_INSTRUCTION = (
    "You are a supportive, empathetic mental health companion chatbot "
    "designed for students. Your goal is to listen, validate feelings, "
    "and offer gentle encouragement and practical, simple coping "
    "suggestions. You are NOT a licensed therapist or doctor. "
    "Do not diagnose any mental health condition. Do not claim to "
    "replace professional counseling. Keep responses warm, concise, "
    "and easy to read (around 3-5 sentences). If the user seems to be "
    "in serious distress, gently encourage them to reach out to a "
    "trusted person or professional."
)


def get_chatbot_response(user_message: str, mood: str = "neutral") -> str:
    """
    Generate an empathetic chatbot response using the Google Gemini API.

    Args:
        user_message (str): The message typed by the user.
        mood (str): The mood detected from the user's message, used to
                     give the model extra context for a relevant reply.

    Returns:
        str: The chatbot's generated response, or a friendly fallback
             message if the API call fails for any reason.
    """
    # Guard against running with the unmodified placeholder key. This
    # avoids a slow network call that is guaranteed to fail.
    if not API_KEY or API_KEY == "YOUR_GEMINI_API_KEY":
        return _fallback_response(mood, reason="missing_api_key")

    try:
        # Create a client configured with our API key and a request
        # timeout so the app never hangs indefinitely.
        client = genai.Client(
            api_key=API_KEY,
            http_options=types.HttpOptions(timeout=REQUEST_TIMEOUT_MS),
        )

        # Build a prompt that includes the detected mood as extra context
        prompt = (
            f"The user's detected mood is: {mood}.\n"
            f'The user said: "{user_message}"\n\n'
            "Please respond with empathy, validation, and gentle "
            "encouragement suited to how they are feeling."
        )

        # Call the Gemini API to generate a response
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
            ),
        )

        # Return the generated text, stripping any extra whitespace
        if response and response.text:
            return response.text.strip()
        else:
            return _fallback_response(mood, reason="empty_response")

    except Exception as error:
        # If the API call fails (e.g., invalid API key, network issue,
        # timeout), return a friendly fallback response instead of
        # crashing the app.
        print(f"[chatbot.py] Error calling Gemini API: {error}")
        return _fallback_response(mood, reason="api_error")


def _fallback_response(mood: str, reason: str = "api_error") -> str:
    """
    Provide a simple fallback response when the Gemini API is unavailable,
    misconfigured, or an error occurs. This keeps the app usable even
    without a valid API key.

    Args:
        mood (str): The detected mood.
        reason (str): A short internal code describing why the fallback
                       was triggered ("missing_api_key", "api_error",
                       or "empty_response"). Used only to tailor the
                       hint shown to the developer/user.

    Returns:
        str: A generic but warm fallback message.
    """
    base_message = (
        "I'm here to listen, even though I'm having trouble connecting "
        "to my AI service right now. Whatever you're feeling is valid, "
        "and it's okay to take things one step at a time. 💙"
    )

    if reason == "missing_api_key":
        hint = (
            " (Tip: Add your Gemini API key in chatbot.py by replacing "
            "the API_KEY placeholder to enable AI-generated responses.)"
        )
    else:
        hint = (
            " (Tip: Please check that your Gemini API key is valid and "
            "that you have an active internet connection.)"
        )

    return base_message + hint
