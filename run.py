import TikTokDownload as TK
import os
import re

if not os.path.exists("下载"):
    os.mkdir("下载")
with open("downLoadList.txt") as file:
    for item in file:
        t = re.findall('(https://v.douyin.com/.*?/)', item, re.S)
        if len(t)!=0:
            os.system('python3 TikTokDownload.py -u '+ t[0] + ' -m yes')
        else:
            print("不是分享地址:"+item)