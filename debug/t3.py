# coding=utf-8
import requests
import re
from ytlv.proxy_stell import get_proxy
import random
import os

class islive():


#--------------------------------------------------------------------正常--------------------------------------------------------------------    
    def ytid(self,chid):
        link=(f"https://www.youtube.com/channel/{chid}/live")
        
        
        r = requests.get(link)
        if  re.search(r'"isLive":true', r.text) is None:
            data=[{"link":link,"status":"NONE","title":"NONE","picture":"NONE"}]  
            return(data)
        else:
            try:
                title=re.findall(r'title="(.*?)"',r.text)
                for i in title:
                    if i !="YouTube":
                        title=i
                        break
            except:
                title="NONE"
            try:
                status=re.search(r'"status":"(.*?)"',r.text).group(1)
                if status=="LIVE_STREAM_OFFLINE":
                    status="LIVE_OFFLINE"
            except:
                status="NONE"                

            
            picture=re.findall(r'rel="canonical" href="(.*?)"', r.text)
            picture=str(picture)
            ftrueurl=picture.strip().strip("[]'")
            pictureurl=ftrueurl[32:]
            pictureurl=f"https://i.ytimg.com/vi/{pictureurl}/maxresdefault_live.jpg"



            data=[{"link":ftrueurl,"status":status,"title":title,"picture":pictureurl}]
            return(data)


if __name__ == "__main__":
    lol=input("thing")
    lv=islive()
    #lv.lvgetproxy()
    live=lv.ytid(lol)
    print(live)