"""
AI 场景 01: RAG 文本分块
将长文本按 chunk_size 分块，支持 overlap 重叠
"""


def chunk_text(text: str, chunk_size: int, overlap: int = 0) -> list[str]:
    """
    将文本按字符数分块。
    - chunk_size: 每块最大字符数
    - overlap: 相邻块之间的重叠字符数
    - 返回分块列表
    """
    # TODO: 实现
    if not text or chunk_size <= 0:
        return []
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
        if start >= len(text) or overlap >= chunk_size:
            break
    return chunks

