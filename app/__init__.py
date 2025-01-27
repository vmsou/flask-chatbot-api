from flask import Flask
from app.chatbot import chatbot_bp

def create_app():
    app = Flask(__name__)

    # app.config['SECRET_KEY'] = 'teste123'
    app.register_blueprint(chatbot_bp, url_prefix="/api")

    return app

app = create_app()