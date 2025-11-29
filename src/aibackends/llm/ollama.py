from aibackends.llm.base import BaseProvider

from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from typing import cast

api_base_url = "http://localhost:11434/v1"

class OllamaClient(BaseProvider):
    def __init__(self):
        pass

    def generate_text_completion(self, model: str, system_prompt: str, message: str):

        client = OpenAI(
            api_key="",
            base_url=api_base_url
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ]

        completion = client.chat.completions.create(
            model=model,
            messages=cast(list[ChatCompletionMessageParam], cast(object, messages)),
        )

        if completion is None or completion.choices is None or len(completion.choices) == 0:
            raise ValueError("API returned an empty or invalid response")

        return completion.choices[0].message.content


