from aibackends.llm.base import BaseProvider
from aibackends.tasks.base import BaseTask

class TranslateText(BaseTask):
    def __init__(self, provider: BaseProvider, model: str, text: str, target_language:str):
        self.name = "TranslateTextTask"
        self.provider = provider
        self.model = model
        self.system_prompt = f"Translate the following text to the target language {target_language}: "
        self.text = text
        self.target_language = target_language
        self.result = None
        pass

    def set_provider(self, provider: BaseProvider):
        self.provider = provider

    def run(self):
        print(f"\nRunning task {self.name}")
        result = self.provider.generate_text_completion(self.model, self.system_prompt, self.text)
        self.result = result

    def get_result(self):
        return self.result