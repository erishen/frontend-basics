def chunk_text(text: str, chunk_size: int, overlap: int = 0) -> list[str]:
    if not text or chunk_size <= 0:
        return []
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
        if start >= len(text):
            break
        # 防止 overlap >= chunk_size 导致死循环
        if overlap >= chunk_size:
            break
    return chunks
