from abc import ABC, abstractmethod

class BaseTask(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def run(self) -> str:
        pass