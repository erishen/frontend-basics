from src.ex13_text_chunking import chunk_text


def test_basic_chunking():
    assert chunk_text("abcdefgh", 3) == ["abc", "def", "gh"]


def test_with_overlap():
    result = chunk_text("abcdefgh", 4, overlap=2)
    assert result == ["abcd", "cdef", "efgh", "gh"]


def test_exact_size():
    assert chunk_text("abcdef", 3) == ["abc", "def"]


def test_single_chunk():
    assert chunk_text("abc", 10) == ["abc"]


def test_empty():
    assert chunk_text("", 5) == []


def test_overlap_larger_than_chunk():
    # overlap >= chunk_size 不应死循环
    result = chunk_text("abcdef", 2, overlap=2)
    assert len(result) > 0
