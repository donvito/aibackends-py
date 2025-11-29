from aibackends import Agent
from aibackends.llm.lmstudio import LMStudioClient
from aibackends.tasks.summarize_text import SummarizeText
from aibackends.tasks.translate_text import TranslateText


def test_agent_with_tasks():
    text = """The rapid diffusion of large language models (LLMs) is mediated by an emerging market for AI inference. 
    However, its economic structure is poorly understood due to challenges in measuring LLM usage. 
    While some fear AI will inevitably evolve into an oligopolistic structure with winner-take-most dynamics, 
    others argue that the rapid emergence of capable open models will inevitably commoditize AI inference. 
    Leveraging data on model-level usage and prices from OpenRouter comprising just under 1% of the total market for LLM inference, 
    we empirically uncover the latent role of open models relative to closed models. Closed models dominate, 
    with on average 80% of monthly LLM tokens using closed models despite much higher prices - 
    on average 6x the price of open models - and only modest performance advantages.
    Frontier open models typically rtest__agent.pyeach performance parity with frontier closed models within months, suggesting relatively fast 
    convergence. Nevertheless, users continue to select closed models even when open alternatives are cheaper and 
    offer superior performance. This systematic underutilization is economically significant: reallocating demand 
    from observably dominated closed models to superior open models would reduce average prices by over 70% and, 
    when extrapolated to the total market, generate an estimated $24.8 billion in additional consumer savings across 2025. 
    These results suggest that closed model dominance reflects powerful drivers beyond model capabilities 
    and price - whether switching costs, brand loyalty, or information frictions - with the economic magnitude of these 
    hidden factors proving far larger than previously recognized, reframing open models as a largely latent, but high-potential, 
    source of value in the AI economy.
    """
    model = "qwen/qwen3-coder-30b"

    llm = LMStudioClient()

    tasks = [
        SummarizeText(
            provider=llm,
            model=model,
            text=text),
        TranslateText(
            provider=llm,
            model=model,
            text=text,
            target_language="chinese")
    ]

    agent = Agent(name="DocumentAssistant", tasks=tasks)
    agent.run_tasks()
    results = agent.get_results()

    print("RESULTS\n============================\n")
    for result in results:
        print(result)