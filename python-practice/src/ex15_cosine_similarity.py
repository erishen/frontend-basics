"""
AI 场景 03: 余弦相似度
计算两个向量的余弦相似度，用于语义检索
"""
import math


def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    """
    计算两个向量的余弦相似度。
    cos(a, b) = dot(a, b) / (|a| * |b|)
    返回 [-1, 1] 之间的值。
    """
    # TODO: 实现
    pass


def top_k_similar(query: list[float], vectors: list[list[float]], k: int) -> list[int]:
    """
    在 vectors 中找与 query 最相似的 top-k 个向量，返回索引列表（按相似度降序）。
    """
    # TODO: 实现
    pass
