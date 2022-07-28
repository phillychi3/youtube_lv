# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup
import json

# chid=input("id")
# r = requests.get(f"https://www.youtube.com/channel/{chid}/live")

# fxxk=re.findall(r'rel="canonical" href="(.*?)"', r.text) 
# print(fxxk)


data="['https://www.youtube.com/watch?v=oIqog5CPrio']"


#lol= json.load(data)
print(data)
data1=data.strip().strip("[]'")
print(data1)
data2=data1[32:]
print(data2)
picture=f"https://i.ytimg.com/vi/{data2}/maxresdefault_live.jpg"
print(picture)