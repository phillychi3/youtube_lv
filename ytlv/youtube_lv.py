# coding=utf-8
import requests
import re
from getproxy import get_proxy
class islive():
    def random_line(fname):
        lines = open(fname).read().splitlines()
        return(lines)




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
        proxy = random_line('proxy.txt')
        proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy,
         }

        try:
            r = requests.get(link,proxies=proxies)
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
        link=f"{chid}/live"
        proxy = random_line('proxy.txt')
        proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy,
         }

        try:
            r = requests.get(link,proxies=proxies)
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
    def lvgetproxy():
        get_proxy()
#--------------------------------------------------------------------代理--------------------------------------------------------------------  