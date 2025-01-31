import os

from dotenv import load_dotenv
from flask import Blueprint, request, jsonify, render_template

from app.chatapi import ChatAPI, ChatAPIProvider

load_dotenv()

chatbot_bp = Blueprint("chatbot", __name__, template_folder='templates', static_folder='static')
provider = os.getenv("CHAT_PROVIDER")
chat_api: ChatAPI = ChatAPIProvider.get("openai" if not provider else provider)

@chatbot_bp.route("/chat", methods=['POST'])
def chat():
    model = request.json.get('model')
    chat_api.model = model
    user_message = request.json.get("message")

    if not user_message: return jsonify({"error": "Mensagem não fornecida"}), 400
    
    try:
        response = chat_api.reply(user_message)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


