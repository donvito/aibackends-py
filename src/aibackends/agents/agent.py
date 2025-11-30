from typing import List
from aibackends.tasks.llm.llm_base_task import LLMBaseTask
import asyncio

class Agent:
    def __init__(self, name: str, tasks: List[LLMBaseTask] = None):
        self.name = name
        self.tasks = tasks
        self.results: List[str] = []
        pass

    def agent_name(self):
        return self.name

    async def run_tasks(self):
        print(f"Running tasks for agent {self.name}")
        # Run all tasks concurrently and collect results directly
        self.results = await asyncio.gather(*[task.run() for task in self.tasks])
        return self.results