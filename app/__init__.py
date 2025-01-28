from flask import Flask

from app.chatbot import chatbot_bp
from app.database import init_db


def create_app():
    app = Flask(__name__)
    app.register_blueprint(chatbot_bp, url_prefix="/api")

    @app.cli.command("init-db")
    def initialize_databse():
        init_db()
        print("Banco de dados inicializado com sucesso!")

    return app

app = create_app()