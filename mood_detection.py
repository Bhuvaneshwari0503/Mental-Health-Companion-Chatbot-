"""
mood_detection.py

This file handles mood detection and safety keyword detection for the
Mental Health Companion Chatbot. It uses simple, beginner-friendly
keyword-based analysis (no heavy NLP libraries required) to keep the
project easy to understand and run.

No external libraries are required for this file.
"""


# Keywords associated with each mood category.
# The lists are intentionally simple and can be expanded over time.
MOOD_KEYWORDS = {
    "stressed": [
        "stress", "stressed", "stressful", "overwhelmed", "pressure",
        "exam", "exams", "deadline", "deadlines", "too much work",
        "burned out", "burnt out",
    ],
    "anxious": [
        "anxious", "anxiety", "nervous", "worried", "worry", "panic",
        "scared", "afraid", "fear", "placement", "placements",
        "interview", "uneasy",
    ],
    "lonely": [
        "lonely", "loneliness", "alone", "isolated", "no friends",
        "nobody understands", "left out", "disconnected",
    ],
    "sad": [
        "sad", "sadness", "down", "unhappy", "depressed", "crying",
        "cry", "upset", "heartbroken", "miserable",
    ],
    "happy": [
        "happy", "great", "excited", "good day", "joyful", "grateful",
        "awesome", "wonderful", "glad",
    ],
}

# Harmful or crisis-related keywords that trigger an immediate safety response.
# IMPORTANT: This list is for basic safety detection only and is NOT a
# substitute for professional crisis detection systems.
HARMFUL_KEYWORDS = [
    "suicide", "suicidal", "self-harm", "self harm", "kill myself",
    "end my life", "hopeless", "want to die", "no reason to live",
    "hurt myself",
]


def detect_harmful_content(user_message: str) -> bool:
    """
    Check if the user's message contains any harmful or crisis-related
    keywords that require an immediate safety response.

    Args:
        user_message (str): The raw message typed by the user.

    Returns:
        bool: True if a harmful keyword is detected, False otherwise.
    """
    try:
        message_lower = user_message.lower()
        for keyword in HARMFUL_KEYWORDS:
            if keyword in message_lower:
                return True
        return False
    except Exception:
        # If anything goes wrong, fail safe by treating it as non-harmful
        # but this should rarely happen with simple string operations.
        return False


def detect_mood(user_message: str) -> str:
    """
    Detect the user's mood based on keyword matching.

    Args:
        user_message (str): The raw message typed by the user.

    Returns:
        str: The detected mood ("stressed", "anxious", "lonely", "sad",
             "happy", or "neutral" if no keywords match).
    """
    try:
        message_lower = user_message.lower()
        mood_scores = {mood: 0 for mood in MOOD_KEYWORDS}

        # Count how many keywords from each mood appear in the message
        for mood, keywords in MOOD_KEYWORDS.items():
            for keyword in keywords:
                if keyword in message_lower:
                    mood_scores[mood] += 1

        # Find the mood with the highest score
        best_mood = max(mood_scores, key=mood_scores.get)

        # If no keywords matched at all, return "neutral"
        if mood_scores[best_mood] == 0:
            return "neutral"

        return best_mood
    except Exception:
        # Fallback to neutral mood if detection fails for any reason
        return "neutral"
