import math


def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    if len(vec_a) != len(vec_b) or not vec_a:
        return 0.0
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def top_k_similar(query: list[float], vectors: list[list[float]], k: int) -> list[int]:
    scores = []
    for i, vec in enumerate(vectors):
        sim = cosine_similarity(query, vec)
        scores.append((i, sim))
    scores.sort(key=lambda x: x[1], reverse=True)
    return [idx for idx, _ in scores[:k]]
