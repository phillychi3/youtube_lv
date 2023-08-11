from ytlv import twitch


def test_get_true_func():
    live=twitch("leekbeats")
    assert  live["status"]=="LIVE"
