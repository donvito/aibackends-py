from aibackends.llm.base import BaseProvider
from aibackends.tasks.llm.llm_base_task import LLMBaseTask

class TextCompletionTask(LLMBaseTask):
    def __init__(self, provider: BaseProvider, model: str, system_prompt: str, user_prompt: str,
                 task_id: str = None, **kwargs):
        super().__init__(task_id, provider, model, **kwargs)
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt
        self.max_tokens = kwargs.get("max_tokens", 100)
        self.temperature = kwargs.get("temperature", 0.7)
        self.result = None

    async def run(self):
        print(f"\nRunning task {self.task_id}")
        response = self.provider.generate_text_completion(
            model=self.model,
            system_prompt=self.system_prompt,
            user_prompt=self.user_prompt,
            max_tokens=self.max_tokens,
            temperature=self.temperature)
        return {
            "task_id": self.task_id,
            "task_name": self.name,
            "response" : response
        }

    def get_result(self):
        return self.result