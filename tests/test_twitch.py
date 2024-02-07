from ytlv import twitch


def test_get_true_func():
    live=twitch("leekbeats")
    assert  live.status =="LIVE"

def test_twitch_url_true():
    try:
        live=twitch("https://www.twitch.tv/utonyan")  # noqa: F841
    except:  # noqa: E722
        assert False