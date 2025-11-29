from aibackends.llm.lmstudio import LMStudioClient

def test_lmstudio_client():
    model_name = "qwen/qwen3-coder-30b"
    client = LMStudioClient()
    result = client.generate_text_completion(model=model_name, message="how many Rs in Strawberry")
    print(result)
    pass