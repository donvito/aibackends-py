from typing import List, Dict
from aibackends.tasks.base import BaseTask

class Agent:
    def __init__(self, name: str, tasks: List[BaseTask] = None):
        self.name = name
        self.tasks = tasks
        self.results: List[str] = []
        pass

    def agent_name(self):
        return self.name

    def run_tasks(self):
        print(f"Running tasks for agent {self.name}")
        for task in self.tasks:
            task.run()
            self.results.append(task.get_result())

    def get_results(self):
        return self.results