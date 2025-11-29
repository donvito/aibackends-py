__version__ = "0.0.1"

from .agents.agent import Agent
from aibackends.tasks.summarize_text import SummarizeText
from aibackends.tasks.translate_text import TranslateText

from aibackends.llm.lmstudio import LMStudioClient
from aibackends.llm.ollama import OllamaClient

__all__ = ['Agent',
           'SummarizeText',
           'TranslateText',
           'LMStudioClient',
           'OllamaClient']