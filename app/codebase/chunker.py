def chunk_text(text: str, file_path: str, max_lines: int = 20):
    lines = text.split("\n")
    chunks = []

    for i in range(0, len(lines), max_lines):
        chunk = "\n".join(lines[i : i + max_lines])
        if chunk.strip():
            chunks.append(f"File: {file_path}\n{chunk}")

    return chunks
