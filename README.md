# youtube_live_status

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

