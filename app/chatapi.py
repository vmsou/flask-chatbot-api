import os

from abc import ABC, abstractmethod
from typing import Literal

import openai

class ChatAPI(ABC):
    @abstractmethod
    def reply(self, message: str) -> str: 
        ...

class OpenAIChatAPI(ChatAPI):
    def __init__(self, api_key: str = None, system_content: str = "Você é um assistente útil."):
        super().__init__()
        openai.api_key = os.getenv("OPENAI_API_KEY") if api_key is None else api_key
        self.system_content = system_content

    def reply(self, message: str) -> str:
        response = openai.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {"role": "system", "content": self.system_content},
                {"role": "user", "content": message}
            ]
        )
        return response['choices'][0]['message']['content']

class ChatAPIProvider:
    @staticmethod
    def get(name: Literal['openai']) -> ChatAPI:
        if name == "openai":
            return OpenAIChatAPI()
        else:
            raise ValueError(f"Provedor desconhecido: {name}")

        