from ddgs import DDGS

def search_urls(query: str, max_results: int = 10) -> list[str]:
    urls = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results, region="in-en"):
            urls.append(r["href"])
    return urls
