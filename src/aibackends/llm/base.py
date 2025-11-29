from abc import ABC, abstractmethod

class BaseProvider(ABC):
    """Interface all llm must implement."""
    @abstractmethod
    def __init__(self, api_key: str = None):
        """Enforce that all subclasses must implement this constructor."""
        pass

    @abstractmethod
    def generate_text_completion(self, model: str, system_prompt: str, message: str):
        """Send a chat completion request."""
        pass