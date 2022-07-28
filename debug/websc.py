# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup
import json
chid=input("id")
r = requests.get(f"https://www.youtube.com/channel/{chid}/live")

# f=open('lol.html',"w",encoding="utf-8")
# f.write(r.text)

tt=re.search(r'"status":"(.*?)"',r.text).group(1)
print(tt)

tt2=re.findall(r'title="(.*?)"',r.text)
print(tt2)

for i in tt2:
    if i !="YouTube":
        tt3=i
        break
print(tt3)


if  re.search(r'"isLive":true', r.text) is None:
    print("no")
else:
    print("yes")

