import requests
import random

API_URL = "http://127.0.0.1:5000/chat"
  # Change to your hosted URL after deployment

fallbacks = [
    "Bot: I lost connection to the chaos core.",
    "Bot: Try again, maybe the server took a nap.",
    "Bot: The matrix glitched.",
    "Bot: I can't think right now... blame the backend.",
]

print("Bot: Hello, mortal. Welcome to ChaosBot.")
user_name = input("Bot: What’s your name, creature? ")

print(f"Bot: Alright {user_name}, let’s start messing things up.\n(Type 'bye' to quit)\n")

while True:
    user_input = input(f"{user_name}: ")

    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Bot: Peace out. Try not to break anything.")
        break

    try:
        response = requests.post(API_URL, json={"message": user_input})
        if response.ok:
            print("Bot:", response.json()["response"])
        else:
            print("Bot:", random.choice(fallbacks))
    except Exception as e:
        print("Bot:", random.choice(fallbacks))
        print(f"(Debug info: {e})")
