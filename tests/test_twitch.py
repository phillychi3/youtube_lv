from ytlv import *
lv=islive()


def test_get_true_func():
    live=lv.twitch("lofi_chill_lounge")
    assert  live["status"]=="LIVE"
