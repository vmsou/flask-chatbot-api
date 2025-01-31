from flask import Flask, render_template

from app.chatbot import chatbot_bp
from app.database import init_db
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(chatbot_bp, url_prefix="/api")

    @app.cli.command("init-db")
    def initialize_databse():
        init_db()
        print("Banco de dados inicializado com sucesso!")

    @app.route("/")
    def index():
        return render_template("index.html")

    return app



app = create_app()