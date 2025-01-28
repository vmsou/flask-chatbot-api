import os

from flask import Blueprint, request, jsonify

from app.chatapi import ChatAPI, ChatAPIProvider

chatbot_bp = Blueprint("chatbot", __name__)
chat_api: ChatAPI = ChatAPIProvider.get("deepseek")

@chatbot_bp.route("/chat", methods=['POST'])
def chat():
    user_message = request.json.get("message")

    if not user_message: return jsonify({"error": "Mensagem não fornecida"}), 400
    
    try:
        response = chat_api.reply(user_message)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
