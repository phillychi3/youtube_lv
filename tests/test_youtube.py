from ytlv import Youtube_lv
lv=Youtube_lv()


def test_noerror():
    live=lv.youutbe("UCdn5BQ06XqgXoAxIhbqw5Rg")
    assert live["status"]!="ERROR"


def test_canreadlivestatus():
    live=lv.youutbe("UCSJ4gkVC6NrvII8umztf0Ow")
    assert live["status"]=="OK"

    