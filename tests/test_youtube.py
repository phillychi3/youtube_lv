from ytlv import *
lv=islive()


def test_noerror():
    live=lv.ytid("UCdn5BQ06XqgXoAxIhbqw5Rg")
    assert live[0]["status"]!="ERROR"


def test_canreadlivestatus():
    live=lv.ytid("UCSJ4gkVC6NrvII8umztf0Ow")
    assert live[0]["status"]=="OK"

    