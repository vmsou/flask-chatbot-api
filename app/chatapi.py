from abc import ABC, abstractmethod

import openai


class ChatAPI(ABC):
    @abstractmethod
    def reply(self, message: str) -> str: 
        ...

class OpenAIChatAPI(ChatAPI):
    def __init__(self, api_key: str, system_content: str = "Você é um assistente útil."):
        super().__init__()
        openai.api_key = api_key
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
