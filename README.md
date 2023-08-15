![image](https://shields.io/pypi/pyversions/youtube-lv)

### how to download

`pip install youtube-lv`

### how to update

`pip install --upgrade youtube-lv`

### how to use

Youtube

```python
from ytlv import youtube
live=youtube("https://www.youtube.com/@ShirakamiFubuki")
print(live)
# return Youtube class
```

#### Youtube class

    channellink :str
    link: str | None
    status: str | None
    islive: bool
    title: str | None
    picture: str | None
    timestamp: float | None

#### Youtube status

      "LIVE" | "READY_TO_LIVE" | "ERROR"| None

#### Youtube class

Twitch

```python
from ytlv import twitch
live=twitch("iitifox")
print(live)
# return twitch class
```

#### Twitch class

    link: str
    status: str | None
    islive: bool
    title: str | None
    picture: str | None
    avatar: str | None

#### Twitch status

      "LIVE" | "ERROR" | None 
