import math
from collections import Counter


class BM25Retriever:
    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.documents: list[list[str]] = []
        self.doc_lens: list[int] = []
        self.avg_dl: float = 0
        self.df: Counter = Counter()

    def add_documents(self, documents: list[str]):
        for doc in documents:
            tokens = doc.lower().split()
            self.documents.append(tokens)
            self.doc_lens.append(len(tokens))
            # 每个词在当前文档中只计一次（文档频率）
            unique_tokens = set(tokens)
            for token in unique_tokens:
                self.df[token] += 1
        total = sum(self.doc_lens)
        self.avg_dl = total / len(self.documents) if self.documents else 0

    def search(self, query: str, top_k: int = 3) -> list[tuple[int, float]]:
        query_tokens = query.lower().split()
        n = len(self.documents)
        scores = []

        for doc_idx, doc in enumerate(self.documents):
            doc_len = self.doc_lens[doc_idx]
            term_freq = Counter(doc)
            score = 0.0
            for token in query_tokens:
                if self.df[token] == 0:
                    continue
                # IDF
                idf = math.log((n - self.df[token] + 0.5) / (self.df[token] + 0.5) + 1)
                # TF 部分
                tf = term_freq.get(token, 0)
                numerator = tf * (self.k1 + 1)
                denominator = tf + self.k1 * (1 - self.b + self.b * doc_len / self.avg_dl)
                score += idf * numerator / denominator
            scores.append((doc_idx, score))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]
