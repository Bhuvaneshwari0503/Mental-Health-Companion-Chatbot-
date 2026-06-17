"""
motivational_messages.py

This file stores motivational and encouraging messages used by the
Mental Health Companion Chatbot. Messages are organized by mood so the
chatbot can pick a relevant one to show alongside the AI-generated reply.

No external libraries are required for this file.
"""

import random


# General motivational messages that can be shown regardless of mood
GENERAL_MESSAGES = [
    "You are stronger than you think. 💪",
    "Progress matters more than perfection. 🌱",
    "One step at a time — you don't have to do everything today. 👣",
    "Difficult moments are temporary. This will pass. 🌤️",
    "Believe in yourself. You have overcome hard things before. ✨",
    "It's okay to rest. Resting is part of moving forward. 🌙",
    "You are doing better than you think you are. 🌟",
    "Small progress is still progress. Keep going. 🚶",
]

# Messages tailored to specific moods
MOOD_MESSAGES = {
    "stressed": [
        "Stress is a sign you care, not a sign you're failing. Take a breath. 🌬️",
        "You don't have to carry everything at once. Break it down. 🧩",
        "This stressful moment does not define your whole journey. 🛤️",
    ],
    "anxious": [
        "You are safe right now, in this moment. 🫶",
        "Anxious thoughts are not always accurate predictions. 🌈",
        "Focus on just the next small step, not the whole staircase. 🪜",
    ],
    "lonely": [
        "Feeling lonely doesn't mean you are unlovable or forgotten. 💛",
        "Reaching out, even a little, can make a big difference. 📞",
        "You deserve connection, and it's okay to seek it out. 🤝",
    ],
    "sad": [
        "It's okay to feel sad. Your feelings are valid. 💙",
        "Sadness is a visitor, not a permanent resident. 🌧️➡️🌤️",
        "Be as kind to yourself as you would be to a friend. 🤍",
    ],
    "happy": [
        "It's wonderful that you're feeling good — savor this moment! 🎉",
        "Your happiness is well-deserved. Keep shining! ☀️",
    ],
}


def get_motivational_message(mood: str = "general") -> str:
    """
    Return a random motivational message based on the detected mood.

    Args:
        mood (str): The detected mood (e.g., "stressed", "anxious",
                     "lonely", "sad", "happy"). Defaults to "general".

    Returns:
        str: A motivational message string.
    """
    try:
        mood = mood.lower().strip()
        if mood in MOOD_MESSAGES:
            # Combine mood-specific and general messages for variety
            combined = MOOD_MESSAGES[mood] + GENERAL_MESSAGES
            return random.choice(combined)
        else:
            return random.choice(GENERAL_MESSAGES)
    except Exception:
        # Fallback message in case anything goes wrong
        return "You are doing the best you can, and that is enough. 🌟"
