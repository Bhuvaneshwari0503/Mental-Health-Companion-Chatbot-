"""
relaxation_tips.py

This file stores relaxation and wellness tips used by the Mental Health
Companion Chatbot. Tips are organized by mood so the chatbot can suggest
relevant, simple coping strategies to the user.

No external libraries are required for this file.
"""

import random


# Relaxation tips organized by mood category
RELAXATION_TIPS = {
    "stressed": [
        "Take a short 5-minute break and step away from your work. ☕",
        "Practice deep breathing: inhale for 4 seconds, hold for 4, exhale for 4. 🌬️",
        "Break large tasks into smaller, more manageable steps. ✅",
        "Try stretching your shoulders and neck to release tension. 🧘",
    ],
    "anxious": [
        "Focus on one task at a time instead of everything at once. 🎯",
        "Try slow, deep breathing to calm your nervous system. 🌬️",
        "Ground yourself by naming 5 things you can see around you. 👀",
        "Write down your worries on paper to get them out of your head. 📝",
    ],
    "lonely": [
        "Reach out to a friend or family member, even with a small message. 💬",
        "Spend time doing a hobby you enjoy, like drawing, music, or reading. 🎨",
        "Consider joining a club, group, or online community with shared interests. 🌐",
        "A short walk outside can help you feel more connected to the world. 🚶",
    ],
    "sad": [
        "Allow yourself to feel sad without judgment — it's a normal emotion. 💙",
        "Listen to music that comforts you or matches your mood. 🎵",
        "Try journaling about what you're feeling and why. 📓",
        "Gentle movement, like a short walk, can sometimes lift your mood. 🌳",
    ],
    "happy": [
        "Savor this positive moment and notice what contributed to it. 🌞",
        "Consider sharing your good mood with someone you care about. 🎉",
    ],
}

# General tips applicable to any mood
GENERAL_TIPS = [
    "Stay hydrated and try to get enough rest tonight. 💧",
    "Take a few minutes to step outside and get some fresh air. 🌤️",
    "Remember that it's okay to ask for help when you need it. 🤝",
]


def get_relaxation_tip(mood: str = "general") -> str:
    """
    Return a random relaxation tip based on the detected mood.

    Args:
        mood (str): The detected mood (e.g., "stressed", "anxious",
                     "lonely", "sad", "happy"). Defaults to "general".

    Returns:
        str: A relaxation tip string.
    """
    try:
        mood = mood.lower().strip()
        if mood in RELAXATION_TIPS:
            return random.choice(RELAXATION_TIPS[mood])
        else:
            return random.choice(GENERAL_TIPS)
    except Exception:
        # Fallback tip in case anything goes wrong
        return "Take a moment to breathe slowly and be kind to yourself. 🌿"


def get_all_tips_for_mood(mood: str) -> list:
    """
    Return the full list of relaxation tips for a given mood.

    Args:
        mood (str): The detected mood.

    Returns:
        list: A list of tip strings. Returns general tips if mood is unknown.
    """
    try:
        mood = mood.lower().strip()
        return RELAXATION_TIPS.get(mood, GENERAL_TIPS)
    except Exception:
        return GENERAL_TIPS
