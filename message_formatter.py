def sparkles(func):
    def wrapper(message):
        
        border= "✨" * (len(message) +10)
        result= func(message)
        return f"{border}\n✨ {result} ✨\n{border}"
    return wrapper


def emoji_decorator(func):
    
    def wrapper(message):
        result = func(message)
        return f"💫💤 {result} 💫💤"
    return wrapper