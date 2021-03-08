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
        
        try:
            r = requests.get(link)
            if  re.search(r'"isLive":true', r.text) is None:                
                data=[{"link":link,"status":"NONE","title":"NONE"}]  
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
                data=[{"link":link,"status":status,"title":title}]  
                return(data)
        except:
            data=[{"link":link,"status":"ERROR","title":"ERROR"}]  
            return(data)
    def ytlk(self,chid):
        link=f"{chid}/live"
        
        try:
            r = requests.get(link)
            if  re.search(r'"isLive":true', r.text) is None:                
                data=[{"link":link,"status":"NONE","title":"NONE"}]  
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
                data=[{"link":link,"status":status,"title":title}]  
                return(data)
        except:
            data=[{"link":link,"status":"ERROR","title":"ERROR"}]  
            return(data)
#--------------------------------------------------------------------正常--------------------------------------------------------------------  
#--------------------------------------------------------------------天使--------------------------------------------------------------------           
    def uto(self,chid):
        link=chid        
        try:
            r = requests.get(link)
            if  re.search(r'"isLive":true', r.text) is None:                
                data=[{"link":link,"status":"NONE","title":"NONE"}]  
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
                data=[{"link":link,"status":status,"title":title}]  
                return(data)


        except:
            data=[{"link":link,"status":"ERROR","title":"ERROR"}]  
            return(data)
#--------------------------------------------------------------------天使--------------------------------------------------------------------  
#--------------------------------------------------------------------代理--------------------------------------------------------------------  
    def prytid(self,chid):
        link=(f"https://www.youtube.com/channel/{chid}/live")
        path=os.getcwd()
        lines =  open(f"{path}\proxy.txt").read().splitlines()
        proxy= random.choice(lines)
        proxies = {
        'http': 'http://' + proxy        
         }

        try:
            r = requests.get(link,proxies=proxies,verify=False)
            if  re.search(r'"isLive":true', r.text) is None:                
                data=[{"link":link,"status":"NONE","title":"NONE"}]  
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
                data=[{"link":link,"status":status,"title":title}]  
                return(data)
        except:
            data=[{"link":link,"status":"ERROR","title":"ERROR"}]  
            return(data)
    def prytlk(self,chid):
        path=os.getcwd()
        link=f"{chid}/live"
        lines =  open(f"{path}\proxy.txt").read().splitlines()
        proxy= random.choice(lines)
        
        proxies = {
        'http': 'http://' + proxy        
         }

        try:
            r = requests.get(link,proxies=proxies,verify=False)
            if  re.search(r'"isLive":true', r.text) is None:                
                data=[{"link":link,"status":"NONE","title":"NONE"}]  
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
                data=[{"link":link,"status":status,"title":title}]  
                return(data)
        except:
            data=[{"link":link,"status":"ERROR","title":"ERROR"}]  
            return(data)
    def lvgetproxy(self):
        path=os.getcwd()
        get_proxy(path)
#--------------------------------------------------------------------代理--------------------------------------------------------------------  

if __name__ == "__main__":
    lol=input("thing")
    lv=islive()
    #lv.lvgetproxy()
    live=lv.prytid(lol)
    print(live)