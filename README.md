https://shields.io/pypi/pyversions/youtube-lv

### how to download
`pip install youtube-lv`
### how to update
`pip install --upgrade youtube-lv`
### how to use

use ID
```python
from ytlv import *
lv=islive()
live=lv.ytid("channel ID")
print(live)
```

use LINK
```python
from ytlv import *
lv=islive()
live=lv.ytlk("channel link")
<<<<<<< HEAD
print(live)
```

get proxy server

```python
lvgetproxy(self)
```
use proxy server to get youtube status
```python
from ytlv import *
lv=islive()
live=lv.prytid("channel id")
print(live)
```
```python
from ytlv import *
lv=islive()
live=lv.prytlk("channel link")
print(live)
```

return:
```json
[
   {
      "link":"url",
      "status":"live status",
      "title":"live title",
      "picture":"live image"
   }
]
```
