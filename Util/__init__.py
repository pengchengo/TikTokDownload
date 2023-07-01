#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:__init__.py
@Date       :2022/07/29 23:20:56
@Author     :JohnserfSeed
@version    :1.3.0.90
@License    :(C)Copyright 2019-2022, Liugroup-NLPR-CASIA
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/07/29 23:20:56 : Init
2022/08/16 18:34:27 : Add moudle Log
2023/03/10 15:27:18 : Add rich download progress
-------------------------------------------------
'''

import re
import os
import json
import time
import rich
import signal
import random
import asyncio
import logging
import requests
import platform
import argparse
import configparser

from lxml import etree
from TikTokUpdata import Updata
from functools import partial
from threading import Event
from urllib.request import urlopen
from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)
from concurrent.futures import ThreadPoolExecutor

from .XB import XBogus
from .Log import Log
from .Urls import Urls
from .Lives import Lives
from .Check import CheckInfo
from .Config import Config
from .Images import Images
from .Command import Command
from .Cookies import Cookies
from .Profile import Profile
from .Download import Download


progress = Progress(
    TextColumn("{task.description}[bold blue]{task.fields[filename]}", justify="left"),
    BarColumn(bar_width=20),
    "[progress.percentage]{task.percentage:>3.1f}%",
    "•",
    DownloadColumn(),
    "•",
    TransferSpeedColumn(),
    "•",
    TimeRemainingColumn(),
)

done_event = Event()


def handle_sigint(signum, frame):
    done_event.set()


signal.signal(signal.SIGINT, handle_sigint)


def copy_url(task_id: TaskID, url: str, name: str, path: str) -> None:
    response = urlopen(url)
    progress.update(task_id, total=int(
        response.info()["Content-length"]))
    with open(path, "wb") as dest_file:
        progress.start_task(task_id)
        for data in iter(partial(response.read, 32768), b""):
            dest_file.write(data)
            progress.update(task_id, advance=len(data))
            if done_event.is_set():
                return


# 日志记录
log = Log()

def replaceT(obj):
    """
    替换文案非法字符
    Args:
        obj (_type_): 传入对象
    Returns:
        new: 处理后的内容
    """
    if len(obj) > 100:
        obj = obj[:100]
    reSub = r"[^\u4e00-\u9fa5^a-z^A-Z^0-9^#]"
    new = []
    if type(obj) == list:
        for i in obj:
            # 替换为下划线
            retest = re.sub(reSub, "_", i)
            new.append(retest)
    elif type(obj) == str:
        # 替换为下划线
        new = re.sub(reSub, "_", obj, 0, re.MULTILINE)
    return new


def Status_Code(code: int):
    if code == 200:
        return
    else:
        log.info('[  提示  ]:该视频%i，暂时无法解析！' % code)
        print('[  提示  ]:该视频%i，暂时无法解析！' % code)
        return


def reFind(strurl):
    """
    匹配分享的url地址
    Args:
        strurl (string): 带文案的分享链接
    Returns:
        result: url短链
    """
    # 空数据判断
    if strurl == '':
        return strurl
    result = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', strurl)
    return result

# 检查版本
#Updata().get_Updata()
