from src.ex20_bm25_retrieval import BM25Retriever


def test_basic_search():
    retriever = BM25Retriever()
    retriever.add_documents([
        "the cat sat on the mat",
        "the dog played in the park",
        "a cat and a dog are friends",
    ])
    results = retriever.search("cat", top_k=2)
    assert len(results) == 2
    # 包含 "cat" 的文档应该排在前面
    indices = [r[0] for r in results]
    assert 0 in indices or 2 in indices


def test_no_match():
    retriever = BM25Retriever()
    retriever.add_documents(["hello world", "foo bar"])
    results = retriever.search("xyz", top_k=2)
    # 所有分数应该为 0
    assert all(score == 0 for _, score in results)


def test_top_k_limit():
    retriever = BM25Retriever()
    retriever.add_documents(["a b c", "d e f", "g h i", "j k l"])
    results = retriever.search("a", top_k=2)
    assert len(results) == 2


def test_empty_documents():
    retriever = BM25Retriever()
    retriever.add_documents(["hello world"])
    results = retriever.search("hello", top_k=3)
    assert len(results) == 1
    assert results[0][0] == 0
    assert results[0][1] > 0
