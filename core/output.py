# src/core/output.py

def write_markdown(filename: str, brief: str):
    """
    Writes the research brief (already a string) into a Markdown file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Research Brief\n\n")
        f.write(brief)






