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
                        try:
                            timestamp=re.search(r'"scheduledStartTime":"(.*?)"',r.text).group(1)
                        except:
                            timestamp="NONE"
                except:
                    status="NONE"                

                try:
                    picture=re.findall(r'rel="canonical" href="(.*?)"', r.text)
                    picture=str(picture)
                    ftrueurl=picture.strip().strip("[]'")
                    pictureurl=ftrueurl[32:]
                    pictureurl=f"https://i.ytimg.com/vi/{pictureurl}/maxresdefault_live.jpg"

                except:
                    ftrueurl="NONE"
                    pictureurl="NONE"


                
                    

                data=[{"link":ftrueurl,"status":status,"title":title,"picture":pictureurl,"timestamp":timestamp}]
                return(data)
        except Exception as e:
            print(e)
            data=[{"link":link,"status":"ERROR","title":"ERROR","picture":"ERROR","timestamp":"ERROR"}]  
            return(data)
    def ytlk(self,chid):
        link=f"{chid}/live"
        
        try:
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
                        try:
                            timestamp=re.search(r'"scheduledStartTime":"(.*?)"',r.text).group(1)
                        except:
                            timestamp="NONE"                   
                except:
                    status="NONE"
                try:
                    picture=re.findall(r'rel="canonical" href="(.*?)"', r.text)
                    picture=str(picture)
                    ftrueurl=picture.strip().strip("[]'")
                    pictureurl=ftrueurl[32:]
                    pictureurl=f"https://i.ytimg.com/vi/{pictureurl}/maxresdefault_live.jpg"

                except:
                    ftrueurl="NONE"
                    pictureurl="NONE"

                data=[{"link":ftrueurl,"status":status,"title":title,"picture":pictureurl,"timestamp":timestamp}]
                return(data)

        except:
            data=[{"link":link,"status":"ERROR","title":"ERROR","picture":"ERROR","timestamp":"ERROR"}]
            return(data)
#--------------------------------------------------------------------正常--------------------------------------------------------------------  
#--------------------------------------------------------------------天使--------------------------------------------------------------------           
    # def uto(self,chid):
    #     link=chid        
    #     try:
    #         r = requests.get(link)
    #         if  re.search(r'"isLive":true', r.text) is None:                
    #             data=[{"link":link,"status":"NONE","title":"NONE","picture":"NONE"}]
    #             return(data)
    #         else:
    #             try:
    #                 title=re.findall(r'title="(.*?)"',r.text)
    #                 for i in title:
    #                     if i !="YouTube":
    #                         title=i
    #                         break
    #             except:
    #                 title="NONE"
    #             try:
    #                 status=re.search(r'"status":"(.*?)"',r.text).group(1)

    #                 if status=="LIVE_STREAM_OFFLINE":
    #                     status="LIVE_OFFLINE"
    #             except:
    #                 status="NONE"
    #             try:
    #                 picture=re.findall(r'rel="canonical" href="(.*?)"', r.text)
    #                 picture=str(picture)
    #                 ftrueurl=picture.strip().strip("[]'")
    #                 pictureurl=ftrueurl[32:]
    #                 pictureurl=f"https://i.ytimg.com/vi/{pictureurl}/maxresdefault_live.jpg"

    #             except:
    #                 ftrueurl="NONE"
    #                 pictureurl="NONE"

    #             data=[{"link":ftrueurl,"status":status,"title":title,"picture":pictureurl}]
    #             return(data)


    #     except:
    #         data=[{"link":link,"status":"ERROR","title":"ERROR","picture":"ERROR"}]
    #         return(data)
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
            r = requests.get(link,proxies=proxies)
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
                        try:
                            timestamp=re.search(r'"scheduledStartTime":"(.*?)"',r.text).group(1)
                        except:
                            timestamp="NONE"                     
                except:
                    status="NONE"
                try:
                    picture=re.findall(r'rel="canonical" href="(.*?)"', r.text)
                    picture=str(picture)
                    ftrueurl=picture.strip().strip("[]'")
                    pictureurl=ftrueurl[32:]
                    pictureurl=f"https://i.ytimg.com/vi/{pictureurl}/maxresdefault_live.jpg"

                except:
                    ftrueurl="NONE"
                    pictureurl="NONE"

                data=[{"link":ftrueurl,"status":status,"title":title,"picture":pictureurl,"timestamp":timestamp}]
                return(data)

        except:
            data=[{"link":link,"status":"ERROR","title":"ERROR","picture":"ERROR","timestamp":"ERROR"}]
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
            r = requests.get(link,proxies=proxies)
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
                        try:
                            timestamp=re.search(r'"scheduledStartTime":"(.*?)"',r.text).group(1)
                        except:
                            timestamp="NONE"                        
                except:
                    status="NONE"
                try:
                    picture=re.findall(r'rel="canonical" href="(.*?)"', r.text)
                    picture=str(picture)
                    ftrueurl=picture.strip().strip("[]'")
                    pictureurl=ftrueurl[32:]
                    pictureurl=f"https://i.ytimg.com/vi/{pictureurl}/maxresdefault_live.jpg"

                except:
                    ftrueurl="NONE"
                    pictureurl="NONE"

                data=[{"link":ftrueurl,"status":status,"title":title,"picture":pictureurl,"timestamp":timestamp}]
                return(data)

        except:
            data=[{"link":link,"status":"ERROR","title":"ERROR","picture":"ERROR","timestamp":"ERROR"}]
            return(data)
    def lvgetproxy(self):
        path=os.getcwd()
        get_proxy(path)
#--------------------------------------------------------------------代理--------------------------------------------------------------------  

if __name__ == "__main__":
    lol=input("thing")
    lv=islive()
    #lv.lvgetproxy()
    live=lv.ytid(lol)
    print(live)