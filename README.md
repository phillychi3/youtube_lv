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
{
  "link": "url",
  "status": "live status",
  "title": "live title",
  "picture": "live image",
  "timestamp": "timestamp"
}
```

Twitch

```python
from ytlv import twitch
live=twitch("iitifox")
print(live)
{
   "link":"url",
   "status":"LIVE",
   "title":"title",
   "picture":"pictureurl",
   "avatar":"avatar"
}
```
