import math
from src.ex15_cosine_similarity import cosine_similarity, top_k_similar


def test_identical_vectors():
    assert abs(cosine_similarity([1, 2, 3], [1, 2, 3]) - 1.0) < 1e-9


def test_orthogonal():
    assert abs(cosine_similarity([1, 0], [0, 1])) < 1e-9


def test_opposite():
    assert abs(cosine_similarity([1, 0], [-1, 0]) - (-1.0)) < 1e-9


def test_zero_vector():
    assert cosine_similarity([0, 0], [1, 2]) == 0.0


def test_top_k():
    query = [1, 0, 0]
    vectors = [
        [0.9, 0.1, 0],   # 最相似
        [0, 0.9, 0.1],   # 最不相似
        [0.8, 0.2, 0],   # 次相似
    ]
    result = top_k_similar(query, vectors, k=2)
    assert result == [0, 2]


def test_top_k_all():
    query = [1, 1]
    vectors = [[1, 1], [0, 1], [1, 0]]
    result = top_k_similar(query, vectors, k=3)
    assert result[0] == 0  # [1,1] 与 [1,1] 最相似
