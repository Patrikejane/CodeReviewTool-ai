from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral")

def review_code(code: str, standards: str) -> str:
    """
    Review the given source code using provided coding standards.
    Returns a summary of issues and suggestions.
    """
    prompt = f"""
You are a code reviewer.

Coding Standards:
{standards}

Code:
{code}

Please identify any issues, list violated standards, and provide improvement suggestions.
"""
    return llm.invoke(prompt)