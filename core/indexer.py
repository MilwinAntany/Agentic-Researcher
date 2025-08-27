import chromadb


def build_index(docs):
    client = chromadb.PersistentClient(path="./chroma_db")

    # If collection exists, delete and recreate
    try:
        client.delete_collection("research")
    except Exception:
        pass  # if not exists, ignore

    collection = client.create_collection("research")

    for i, doc in enumerate(docs):
        collection.add(
            documents=[doc["text"]],
            metadatas=[{"source": doc["url"]}],
            ids=[str(i)]
        )

    return client, collection

