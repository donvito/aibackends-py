from abc import ABC, abstractmethod

class BaseProvider(ABC):
    """Interface all llm must implement."""
    def __init__(self, api_key: str = None):
        """Enforce that all subclasses must implement this constructor."""
        self.api_key = api_key

    @abstractmethod
    def generate_text_completion(self, model: str, system_prompt: str, user_prompt: str, **kwargs):
        """Send a text completion request."""
        pass