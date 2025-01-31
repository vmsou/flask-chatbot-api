import os

from abc import ABC, abstractmethod
from typing import Literal

from openai import OpenAI


class ChatAPI(ABC):
    @abstractmethod
    def reply(self, message: str) -> str: 
        ...

class OpenAIChatAPI(ChatAPI):
    def __init__(self, model: str = None, api_key: str = None, api_url: str = None):
        super().__init__()
        self.model = model
        self.api_key = api_key
        self.api_url = api_url
        self.client = OpenAI(api_key=api_key, base_url=api_url)

    def reply(self, message: str) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": message}]
        )
        return completion.choices[0].message.content
    

class DeepSeekChatAPI(ChatAPI):
    def __init__(self, api_key: str = None):
        super().__init__()
        self.chat_api: ChatAPI = OpenAIChatAPI(model="deepseek-chat", api_key=api_key, api_url="https://api.deepseek.com")

    def reply(self, message: str) -> str: return self.chat_api.reply(message)
    

class HuggingFaceChatAPI(ChatAPI):
    def __init__(self, api_key: str = None, model="deepseek-ai/DeepSeek-R1"):
        super().__init__()
        self.chat_api: ChatAPI = OpenAIChatAPI(model=model, api_key=api_key, api_url="https://huggingface.co/api/inference-proxy/together")

    def reply(self, message: str) -> str: return self.chat_api.reply(message)


class ChatAPIProvider:
    PROVIDERS = {
        "openai": OpenAIChatAPI,
        "deepseek": DeepSeekChatAPI,
        "huggingface": HuggingFaceChatAPI,
    }

    @staticmethod
    def get(name: Literal['openai', 'deepseek', 'huggingface']) -> ChatAPI:
        name = name.lower().strip()
        if name == "openai": return OpenAIChatAPI(model=os.getenv("API_MODEL"), api_key=os.getenv("OPENAI_API_KEY"), api_url=os.getenv("API_URL"))
        elif name == "deepseek": return DeepSeekChatAPI(api_key=os.getenv("DEEPSEEK_API_KEY"))
        elif name == "huggingface": return HuggingFaceChatAPI(model=os.getenv("API_MODEL"), api_key=os.getenv("HUGGINGFACE_API_KEY"))
        raise Exception(f"Provedor não encontrado: {name}")
