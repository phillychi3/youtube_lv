from ytlv import youtube



def test_noerror():
    live=youtube("UCdn5BQ06XqgXoAxIhbqw5Rg")
    assert live.status !="ERROR"

def test_hyphen():
    live=youtube("https://www.youtube.com/channel/UCvzGlP9oQwU--Y0r9id_jnA")
    assert live.status !="ERROR"


def test_canreadlivestatus():
    live=youtube("https://www.youtube.com/@LofiGirl")
    assert live.status =="LIVE"

def test_canreadlivestatus2():
    live=youtube("@LofiGirl")
    assert live.status =="LIVE"

def test_canreadlivestatus3():
    live=youtube("https://youtube.com/@LofiGirl")
    assert live.status =="LIVE"