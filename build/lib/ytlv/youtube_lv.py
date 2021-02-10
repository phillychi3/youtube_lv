# coding=utf-8
import requests
import re

class islive():
    
    def ytid(self,chid):
        link=(f"https://www.youtube.com/channel/{chid}/live")
        
        try:
            r = requests.get(link)
            if  re.search(r'"isLive":true', r.text) is None:                
                return("no")
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
                data=[{"link":link,"status":status,"title":title}]  
                return(data)
        except:
            data=[{"link":link,"status":"ERROR","title":"ERROR"}]  
            return(data)
    def ytlk(self,chid):
        link=chid
        
        try:
            r = requests.get(link)
            if  re.search(r'"isLive":true', r.text) is None:                
                return("no")
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
                data=[{"link":link,"status":status,"title":title}]  
                return(data)
        except:
            data=[{"link":link,"status":"ERROR","title":"ERROR"}]  
            return(data)

