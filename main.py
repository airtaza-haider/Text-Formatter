from text_formatter.message_formatter import sparkles, emoji_decorator

@emoji_decorator
@sparkles

def greet(message):
    
    return message

def main():
    print(greet (input("Enter text: ")))
