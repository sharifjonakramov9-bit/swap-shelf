import requests
from django.conf import settings

def send_to_telegram(book):
    text = f"""
📚 New Book Added!

📖 {book.title}
✍ {book.author}
📂 {book.genre.name}
⭐ Owner Rating: {getattr(book.owner, 'rating', 'N/A')}

Condition: {book.condition}
Type: {book.type}

📝 {book.description}

🔗 Request via website
"""
    url = f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": settings.CHANNEL_ID,
        "text": text
    })