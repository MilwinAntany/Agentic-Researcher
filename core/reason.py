def synthesize(topic, questions, collection, k=3):
    from src.utils.llm import ask_llm

    results = collection.query(
        query_texts=[topic],
        n_results=k
    )

    docs = results["documents"][0]
    sources = [m["source"] for m in results["metadatas"][0]]  # ✅ FIXED

    text = "\n".join(docs)

    prompt = f"""
    Topic: {topic}
    Sub-questions: {questions}
    Sources: {sources}
    Text: {text}

    Summarize the findings and provide actionable insights.
    """

    return ask_llm(prompt)

