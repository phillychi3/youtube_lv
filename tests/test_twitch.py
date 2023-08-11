from ytlv import Youtube_lv
lv=Youtube_lv()


def test_get_true_func():
    live=lv.twitch("lofi_chill_lounge")
    assert  live["status"]=="LIVE"
