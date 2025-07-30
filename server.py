from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
import os
from flask_cors import CORS

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)  # Allow requests from the desktop app

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")
        
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chaotic, sarcastic, funny chatbot."},
                {"role": "user", "content": user_input}
            ]
        )
        return jsonify({"response": completion['choices'][0]['message']['content']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
