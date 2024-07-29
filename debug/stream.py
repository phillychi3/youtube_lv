import requests
import json
import re

req = requests.get("https://www.youtube.com/@tomorrowland/streams")

# save html

# with open("tomorrowland.html", "w",encoding="utf8") as f:
#     f.write(req.text)

# for i in re.findall(r"\"thumbnailOverlays\":\[(.*?)\]", req.text):
#     print(i)
#     print(json.loads(i))

# tt2 = re.search(r'sectionListRenderer":{"contents":\[(.*?)\],"trackingParams":"(.*?)","targetId":"(.*?)","disablePullToRefresh":(.*?)}', req.text)

# print(tt2)
# print(tt2.group(1))
# with open("tomo.json", "w", encoding="utf8") as f:
#     f.write(tt2.group(1))


pattern = r'"content":{"sectionListRenderer":{"contents":(.*?),"trackingParams":"[^"]*","targetId":"[^"]*"[^}]*}'

tt2 = re.search(pattern, req.text, re.DOTALL)

if tt2:
    print("find")
    content = tt2.group(1)
    with open("tomo.json", "w", encoding="utf8") as f:
        f.write(content)
else:
    print("not find")

try:
    data = json.loads(content)
except json.JSONDecodeError as e:
    print("JSON error lol", e)

for i in data:
    try:
        for items in i["itemSectionRenderer"]["contents"][0]["shelfRenderer"]["content"]["horizontalListRenderer"]["items"]:
            print(items["gridVideoRenderer"]["thumbnailOverlays"][0]["thumbnailOverlayTimeStatusRenderer"]["style"])
            video = items["gridVideoRenderer"]
            # if items["gridVideoRenderer"]["thumbnailOverlays"][0]["thumbnailOverlayTimeStatusRenderer"]["style"] == "LIVE":
            #     video = items["gridVideoRenderer"]
            #     print(video["title"]["simpleText"])
            #     print(video["thumbnail"]["thumbnails"])
            #     print("https://youtube.com"+video["navigationEndpoint"]["commandMetadata"]["webCommandMetadata"]["url"])
            #     print("https://youtube.com"+i["itemSectionRenderer"]["contents"][0]["shelfRenderer"]["endpoint"]["browseEndpoint"]["canonicalBaseUrl"])
            print(video["title"]["simpleText"])
            print(video["thumbnail"]["thumbnails"])
            print("https://youtube.com"+video["navigationEndpoint"]["commandMetadata"]["webCommandMetadata"]["url"])
            if "shortBylineText" not in video:
                print("https://youtube.com"+i["itemSectionRenderer"]["contents"][0]["shelfRenderer"]["endpoint"]["browseEndpoint"]["canonicalBaseUrl"])
            else:
                print("https://youtube.com"+video["shortBylineText"]["runs"][0]["navigationEndpoint"]["browseEndpoint"]["canonicalBaseUrl"])
            # print("https://youtube.com"+i["itemSectionRenderer"]["contents"][0]["shelfRenderer"]["endpoint"]["browseEndpoint"]["canonicalBaseUrl"])
    except AttributeError as e:
        print("找不到對應的屬性", e)

