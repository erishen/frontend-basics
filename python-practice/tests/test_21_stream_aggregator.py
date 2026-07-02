from src.ex21_stream_aggregator import StreamAggregator


def test_feed_and_get_text():
    agg = StreamAggregator()
    agg.feed("Hello")
    agg.feed(" ")
    agg.feed("World")
    assert agg.get_text() == "Hello World"


def test_callback():
    agg = StreamAggregator()
    received = []
    agg.on_token(lambda t: received.append(t))
    agg.feed("a")
    agg.feed("b")
    assert received == ["a", "b"]


def test_multiple_callbacks():
    agg = StreamAggregator()
    log1, log2 = [], []
    agg.on_token(lambda t: log1.append(t))
    agg.on_token(lambda t: log2.append(t.upper()))
    agg.feed("hi")
    assert log1 == ["hi"]
    assert log2 == ["HI"]


def test_split():
    agg = StreamAggregator()
    for token in ["line1\n", "line2\n", "line3"]:
        agg.feed(token)
    assert agg.split("\n") == ["line1", "line2", "line3"]


def test_reset():
    agg = StreamAggregator()
    agg.feed("data")
    agg.reset()
    assert agg.get_text() == ""
