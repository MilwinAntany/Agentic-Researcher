# src/utils/llm.py

import ollama

def call_llm(prompt: str, model: str = "phi3:mini") -> str:
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

ask_llm = call_llm
