# src/core/planner.py

from src.utils.llm import call_llm

def plan(topic: str) -> list[str]:
    prompt = f"""Break down the following research topic into 3-5 precise sub-questions:
    Topic: {topic}
    """
    resp = call_llm(f"You are a research planner.\n\n{prompt}")
    return [q.strip("-• ") for q in resp.split("\n") if q.strip()]
