__version__ = "0.0.1"

from .agents.agent import Agent
from aibackends.tasks.llm.text_completion_task import TextCompletionTask

from aibackends.llm.lmstudio import LMStudioClient
from aibackends.llm.ollama import OllamaClient

__all__ = ['Agent',
           'TextCompletionTask',
           'LMStudioClient',
           'OllamaClient']