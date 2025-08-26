def guardrail(func):
    def wrapper(text, *args, **kwargs):
        offensive_words = ["stupid", "idiot", "hate"]
        if any(word in text.lower() for word in offensive_words):
            return "Please keep your language polite!"
        return func(text, *args, **kwargs)
    return wrapper

@guardrail
def check_offensive(text: str) -> str:
    return text
