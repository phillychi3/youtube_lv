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
live=lv.ytlk("channel ID")
print(live)
```
