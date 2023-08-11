import requests
import re

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
    if re.search(r'isLiveBroadcast',r.content.decode('utf-8')) is None:
        data={"link":url,"status":"NONE","title":"NONE","picture":"NONE","avatar":"NONE"}
        return data
    try:
        pictureurl=re.findall(r'"thumbnailUrl":\[(.*?)\]',r.content.decode('utf-8'))[0].split(',')[2].strip('"')
    except:
        pictureurl="NONE"
    try:
        avatar = re.findall(r'"twitter:image" content="(.*?)"',r.content.decode('utf-8'))[0]
    except:
        avatar="NONE"
    try:
        title = re.findall(r'twitter:description" content="(.*?)"',r.content.decode('utf-8'))[0]
    except:
        title="NONE"
    data = {"link":url,"status":"LIVE","title":title,"picture":pictureurl,"avatar":avatar}
    return data

def youtube(url) -> dict:
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
    if re.match(r'https://www.youtube.com/channel/[a-zA-Z0-9]*',url):
        match=re.match(r'https://www.youtube.com/channel/[a-zA-Z0-9]*',url)
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
        if  re.search(r'"isLive":true', r.text) is None:
            data={"link":link,"status":"NONE","title":"NONE","picture":"NONE","timestamp":"NONE"}
            return data
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
                else:
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
            data={"link":ftrueurl,"status":status,"title":title,"picture":pictureurl,"timestamp":timestamp}
            return data
    except Exception as e:
        data={"link":link,"status":"ERROR","title":"ERROR","picture":"ERROR","timestamp":"ERROR"}
        return data


if __name__ == "__main__":
    lol=input("thing")
    live=youtube(lol)
    print(live)