import argparse
import pathlib
from src.core import planner, search, crawler, indexer, reason, output

def main():
    parser = argparse.ArgumentParser(description="Agentic AI Researcher")
    parser.add_argument("command", choices=["research"])
    parser.add_argument("topic", help="Research topic")
    parser.add_argument("--max-pages", type=int, default=10)
    parser.add_argument("--fresh-days", type=int, default=365)
    parser.add_argument("--k", type=int, default=4)
    args = parser.parse_args()

    if args.command == "research":
        print(f"[+] Starting research on: {args.topic}")

        # 1. Plan sub-questions
        questions = planner.plan(args.topic)
        print(f"[+] Planned {len(questions)} sub-questions")

        # 2. Search
        urls = search.search_urls(args.topic, max_results=args.max_pages)
        print(f"[+] Got {len(urls)} URLs")

        # 3. Crawl
        docs = crawler.crawl(urls, fresh_days=args.fresh_days)
        print(f"[+] Extracted {len(docs)} documents")

        # 4. Index
        client, collection = indexer.build_index(docs)

        # 5. Reason
        brief = reason.synthesize(args.topic, questions, collection, k=args.k)

        # 6. Output
        path = pathlib.Path("outputs")
        path.mkdir(exist_ok=True)
        filename = path / f"{args.topic.replace(' ', '_')}.md"
        output.write_markdown(filename, brief)

        print(f"[+] Wrote report: {filename}")

if __name__ == "__main__":
    main()

