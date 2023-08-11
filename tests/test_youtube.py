from ytlv import youtube



def test_noerror():
    live=youtube("UCdn5BQ06XqgXoAxIhbqw5Rg")
    assert live["status"]!="ERROR"


def test_canreadlivestatus():
    live=youtube("https://www.youtube.com/@LofiGirl")
    assert live["status"]=="OK"

    