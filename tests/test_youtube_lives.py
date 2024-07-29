from ytlv import youtube_lives



def test_noerror():
    try:
        _ = youtube_lives("https://www.youtube.com/@tomorrowland/streams")
    except:  # noqa: E722
        assert False