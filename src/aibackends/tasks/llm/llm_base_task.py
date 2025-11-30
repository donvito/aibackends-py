from aibackends.llm.base import BaseProvider
from aibackends.tasks.base import BaseTask

class LLMBaseTask(BaseTask):
    def __init__(self, task_id: str, provider: BaseProvider, model: str, **kwargs):
        super().__init__(task_id, name=kwargs.get("name", ""))
        self.provider = provider
        self.model = model

    async def run(self):
        pass