import requests
from pprint import pprint
import os
import re

url = 'https://www.douyin.com/aweme/v1/web/general/search/single/'

headers = {
    "Cookie": "ttwid=1%7CBK2p53A197CIWEGrDH5gA19A3p84dQjC5acbGGPSphU%7C1678195316%7C301754a19a8b5cf7a87b648d2543aa5ee29b9340023cc0f2582d86288c71ce8a; s_v_web_id=verify_leya5uxw_m8TG03a9_EwOm_4NQU_8cbo_LYlbbp0NkJ7o; passport_csrf_token=4166f3687cc7a7986caa9c325e908a1c; passport_csrf_token_default=4166f3687cc7a7986caa9c325e908a1c; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%222%2F20230307%22; xgplayer_user_id=160327433710; douyin.com; strategyABtestKey=%221678245442.754%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1678850242765%2C%22type%22%3A1%7D; csrf_session_id=3d9e68b36ad5232858f8bcfca516008c; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWNsaWVudC1jc3IiOiItLS0tLUJFR0lOIENFUlRJRklDQVRFIFJFUVVFU1QtLS0tLVxyXG5NSUlCRGpDQnRRSUJBREFuTVFzd0NRWURWUVFHRXdKRFRqRVlNQllHQTFVRUF3d1BZbVJmZEdsamEyVjBYMmQxXHJcbllYSmtNRmt3RXdZSEtvWkl6ajBDQVFZSUtvWkl6ajBEQVFjRFFnQUUyckNPQXRLd29NYlI0eVN0L04yeFJ4WjFcclxuWWJVOXdYUWFwcG9xT3FUZ29wbTFqbzI3eGwyQmFxVDFFYWdEMnV0ZDNQdXBsNVJxelJqMXZkeWxvRnU5Q3FBc1xyXG5NQ29HQ1NxR1NJYjNEUUVKRGpFZE1Cc3dHUVlEVlIwUkJCSXdFSUlPZDNkM0xtUnZkWGxwYmk1amIyMHdDZ1lJXHJcbktvWkl6ajBFQXdJRFNBQXdSUUloQUtMblB5OENsY2l0a2IxRDBmYzRlcVRWNjNDWnIyb2Rla0lvL1F2aWMrS2RcclxuQWlBa0huSTlIbGtaaGcvOFFORUJDYXFFeHNHandZMzZHMk00dHJZTnluSTJsQT09XHJcbi0tLS0tRU5EIENFUlRJRklDQVRFIFJFUVVFU1QtLS0tLVxyXG4ifQ==; msToken=UP9W0jpOaYm7ycv2EFHyx240HSL1xLc02lOBquYxqrKfW55wgj5H63ZpbUdfDR5IatBf3bMZWC_Nw192B7rGMY4z47OeqBX5S3EeDMOQYiGyEltj-t03yg==; __ac_nonce=06407fe480012e4f532fa; __ac_signature=_02B4Z6wo00f01LI9B-wAAIDBR0LtcE9ytMCyHQNAAEiNcIrqPEC01kmlN7BfJOuHiDZYqPuofWutxf2WPlsCKLH3yk3tAvR7NkRZc54gDeF9y7N1rYXTBy4ZalmbX8pN76-ivVfzJ8sZeUy2dd; tt_scid=-pI0H.3c5NeTmMt1AANbdwdC.g0swd6WhF6kI.1qXIsiTsNv1v9UyyNutg7iqezk0fa1; msToken=1Uj4907rZHA9WavFbdijUUY9v510qtTlKXaI0gL1o5bmRRcBK3Rc2AUygY4KlydTgcrTmStDFsDB24p2FPGQ6h0Q7q77sQUEv3VLGIsB3cMSrDMrPAbkjA==; home_can_add_dy_2_desktop=%220%22",
    "referer": "https://www.douyin.com/search/%E5%84%BF%E5%AD%90?aid=165d20aa-17b3-4b63-b831-645b2eb7f064&publish_time=0&sort_type=1&source=tab_search&type=general",
    "User-Agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
}

search = input('请输入你想搜索的名称：')
dian_zhan = int(input('请输入点赞数量：'))

while True:
    params = {
        'platform': 'PC',
        'aid': '6383',
        'channel': 'aweme_general',
        'type': '4g',
        'time': '50',
        'keyword': search,
        'source': 'tab_search',
        'search': '0',
        'id': '',
        'offset': '0',
        'count': '10',
        'sort': 1,
        'sort_type':1,
    }

    html = requests.get(url=url, headers=headers, params=params)
    json_url = html.json()
    print(json_url)
    for i in json_url['data'][:-1]:
        try:
            url = i['aweme_info']['video']['play_addr']['url_list'][0]
            name = i['aweme_info']['desc']
            aweme_id = i['aweme_info']['aweme_id']
            bofangliang = i['aweme_info']['statistics']['digg_count']
            if bofangliang > dian_zhan and search in name:
                if not os.path.exists(f'./{search}'):
                    os.mkdir(f'./{search}')
                video_name = name
                video_name = video_name.replace('\n', ' ')
                video_name = re.sub(r'[\/:*?"<>|]', '-', video_name)
                resp = requests.get(url)
                file_object = open(f'./{search}/{bofangliang}_{video_name}.mp4', mode='wb')
                file_object.write(resp.content)
                file_object.close()
                print(f'名称：{bofangliang}_{video_name}下载完成')
        except:
            pass