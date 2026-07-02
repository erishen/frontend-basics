"""
AI 场景 08: BM25 关键词检索
经典的稀疏检索算法，RAG 中常与向量检索混合使用
"""
import math
from collections import Counter


class BM25Retriever:
    """
    简易 BM25 实现。
    BM25(q, d) = Σ IDF(qi) * (f(qi,d) * (k1+1)) / (f(qi,d) + k1*(1 - b + b*|d|/avgdl))
    """

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.documents: list[list[str]] = []  # 分词后的文档
        self.doc_lens: list[int] = []
        self.avg_dl: float = 0
        self.df: Counter = Counter()  # 每个词的文档频率

    def add_documents(self, documents: list[str]):
        """添加文档（按空格简单分词）"""
        # TODO: 实现
        pass

    def search(self, query: str, top_k: int = 3) -> list[tuple[int, float]]:
        """
        搜索返回 top-k 结果。
        返回: [(doc_index, score), ...] 按分数降序
        """
        # TODO: 实现
        pass
