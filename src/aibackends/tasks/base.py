from abc import ABC, abstractmethod
import uuid

class BaseTask(ABC):
    def __init__(self, task_id: str = None, name: str = None):
        self.task_id = task_id or str(uuid.uuid4())
        self.name = name

    @abstractmethod
    def run(self):
        pass