import requests
import re
from dataclasses import dataclass

@dataclass
class Twitch:
    """
    twitch dataclass
    """
    link:str
    status:str | None
    islive:bool    
    title:str | None
    picture:str | None
    avatar:str | None

@dataclass
class Youtube:
    """
    youtube dataclass
    """
    channellink:str
    link:str | None
    status:str | None
    islive:bool
    title:str | None
    picture:str | None
    timestamp:float | None

def twitch(url:str) -> dict:
    """_summary_

    Args:
        url (str): twitch channel name or link

    Returns:
        dict: {"link":url,"status":"LIVE","title":title,"picture":pictureurl,"avatar":avatar}
    """
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    URL = "https://www.twitch.tv/"
    if "https://www.twitch.tv/" not in url:
        url=URL+url
    r = requests.get(url, headers={'User-Agent': user_agent})
    if r.status_code != 200:
        raise Exception("url error")
    if re.search(r'isLiveBroadcast',r.content.decode('utf-8')) is None:
        data=Twitch(url,None,False,None,None,None)
        return data
    try:
        pictureurl=re.findall(r'"thumbnailUrl":\[(.*?)\]',r.content.decode('utf-8'))[0].split(',')[2].strip('"')
    except:
        pictureurl=None
    try:
        avatar = re.findall(r'"twitter:image" content="(.*?)"',r.content.decode('utf-8'))[0]
    except:
        avatar=None
    try:
        title = re.findall(r'twitter:description" content="(.*?)"',r.content.decode('utf-8'))[0]
    except:
        title=None
    data = Twitch(url,"LIVE",True,title,pictureurl,avatar)
    return data

def youtube(url:str) -> dict:
    """__summary__
    Args:
        url (str): youtube channel name or link
        example: https://www.youtube.com/@ShirakamiFubuki
        example: @ShirakamiFubuki
        example: https://www.youtube.com/channel/UCdn5BQ06XqgXoAxIhbqw5Rg
        example: UCdn5BQ06XqgXoAxIhbqw5Rg
    Returns:
        dict: {"link":url,"status":"LIVE","title":title,"picture":pictureurl,"avatar":avatar}
    """
    if re.match(r'https://www.youtube.com/channel/[-a-zA-Z0-9_]*',url):
        match=re.match(r'https://www.youtube.com/channel/[-a-zA-Z0-9_]*',url)
        link=match.group(0)+"/live"
    elif re.match(r"https://www.youtube.com/@[-a-zA-Z0-9_]*",url):
        match=re.match(r"https://www.youtube.com/@[-a-zA-Z0-9_]*",url)
        link=match.group(0)+"/live"
    elif re.match(r"[-a-zA-Z0-9_@]*",url):
        match=re.match(r"[-a-zA-Z0-9_@]*",url)
        if "@" in url:
            link="https://www.youtube.com/"+url+"/live"
        else:
            link="https://www.youtube.com/channel/"+url+"/live"
    
    try:
        r = requests.get(link)
        
        if r.status_code != 200:
            raise Exception("url error")
        link = link.replace("/live","")        
        if  re.search(r'"isLive":true', r.text) is None:
            data = Youtube(link,None,None,False,None,None,None)
            return data
        else:
            statusbool=False
            try:
                title=re.findall(r'title="(.*?)"',r.text)
                for i in title:
                    if i !="YouTube":
                        title=i
                        break
            except:
                title=None
            try:
                status=re.search(r'"status":"(.*?)"',r.text).group(1)
                if status=="OK":
                    status="LIVE"
                    statusbool=True
                    timestamp=None
                elif status=="LIVE_STREAM_OFFLINE":
                    status="READY_TO_LIVE"
                    try:
                        timestamp=re.search(r'"scheduledStartTime":"(.*?)"',r.text).group(1)
                        timestamp=float(timestamp)
                    except:
                        timestamp=None
                else:
                    timestamp=None

            except:
                status=None
                timestamp=None
            try:
                picture=re.findall(r'rel="canonical" href="(.*?)"', r.text)
                picture=str(picture)
                ftrueurl=picture.strip().strip("[]'")
                pictureurl=ftrueurl[32:]
                pictureurl=f"https://i.ytimg.com/vi/{pictureurl}/maxresdefault_live.jpg"

            except:
                ftrueurl=None
                pictureurl=None                         
            data=Youtube(link,ftrueurl,status,statusbool,title,pictureurl,timestamp)
            return data
    except Exception as e:
        raise Exception(e)


if __name__ == "__main__":
    lol=input("thing")
    live=youtube(lol)
    print(live)