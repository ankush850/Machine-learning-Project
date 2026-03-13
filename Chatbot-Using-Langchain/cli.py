import sys
from src.config import settings
from src.chat_service import ChatService

def main():
    if not settings.OPENAI_API_KEY:
        print("Set OPENAI_API_KEY in .env")
        return
    chat = ChatService(
        api_key=settings.OPENAI_API_KEY,
        model=settings.OPENAI_MODEL,
        temperature=settings.TEMPERATURE,
    )
    print("Chatbot ready. Type /exit to quit.")
    while True:
        try:
            text = input("> ").strip()
        except EOFError:
            break
        if not text or text.lower() == "/exit":
            break
        reply = chat.ask(text)
        print(reply)

if __name__ == "__main__":
    main()
