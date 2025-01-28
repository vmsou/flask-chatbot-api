import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, insert
from sqlalchemy import Table, Column, Integer, Text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///chatbot.db")
engine = create_engine(DATABASE_URL)
metadata = MetaData()

interactions = Table(
    "interaction", metadata,
    Column("id", Integer, primary_key=True),
    Column("user_message", Text),
    Column("bot_reply", Text),
)

def init_db():
    metadata.create_all(bind=engine)

def log_interaction(user_message: str, bot_reply: str):
    with engine.connect() as conn:
        stmt = insert(interactions).values(
            user_message=user_message,
            bot_reply=bot_reply,
        )
        conn.execute(stmt)
