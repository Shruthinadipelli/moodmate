def detect_text_emotion(text):
    text = text.lower()

    if any(word in text for word in ["happy", "joy", "excited", "great", "good"]):
        return "happy"

    elif any(word in text for word in ["sad", "depressed", "unhappy", "tired"]):
        return "sad"

    elif any(word in text for word in ["angry", "mad", "furious", "annoyed"]):
        return "angry"

    elif any(word in text for word in ["calm", "relaxed", "peaceful"]):
        return "calm"

    elif any(word in text for word in ["energetic", "active", "motivated"]):
        return "energetic"

    else:
        return "neutral"
