from aibackends.llm.base import BaseProvider
from aibackends.tasks.base import BaseTask

class SummarizeText(BaseTask):
    def __init__(self, provider: BaseProvider, model: str, text: str):
        self.name = "SummarizeTextTask"
        self.provider = provider
        self.model = model
        self.system_prompt = "Summarize the following text:"
        self.text = text
        self.result = str
        pass

    def set_provider(self, provider: BaseProvider):
        self.provider = provider

    def run(self):
        print(f"\nRunning task {self.name}")
        result = self.provider.generate_text_completion(self.model, self.system_prompt, self.text)
        self.result = result

    def get_result(self):
        return self.result