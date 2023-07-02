import json
import os
import re
import time
import requests
import urllib.parse




nn = 1
sun_s = 0
gjc_name = "足球"#input("输入关键词")
max_bofangliang = 1#int(input('点赞量'))
key = urllib.parse.quote(gjc_name)
# print(key)
while True:
    url = f'https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_general&sort_type=1&publish_time=0&keyword={key}&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=&offset={sun_s * 10}&count=10&search_id=202209151332480101402051633D0E8650&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=2560&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=105.0.0.0&browser_online=true&engine_name=Blink&engine_version=105.0.0.0&os_name=Windows&os_version=10&cpu_core_num=12&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7129806389195458082&msToken=20jBGIfrrkKSgtlRmqkkoaFZIj-hQEwWI2LVMn4kASh_Jg_VAJCVGW9q5gwmCLXQnEFn8KdqlEJxrjF7geVghbpbUDCgZS5GJhVjGsTSrXE382FG5H-sKFM=&X-Bogus=DFSzswVLF50ANydASsRgAKXAIQ-S'
    headers = {
        "Cookie": 'xgplayer_user_id=87532903329; ttwid=1%7CIZ9z_fzonOI1w0M0WkZRJ3H7m9c5oXqR9ueVwlRu7Rk%7C1679712264%7C589fb18c65b7ff361661cc2a50719509733648630258ba7475684f7d88007625; passport_csrf_token=96001efe794a5a80eb7f59e4d53843e5; passport_csrf_token_default=96001efe794a5a80eb7f59e4d53843e5; __bd_ticket_guard_local_probe=1687606845237; s_v_web_id=verify_ljiod9k3_QHLpy1vp_peBu_4343_85ox_odUkK4YNKxTO; download_guide=%223%2F20230701%2F0%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; SEARCH_RESULT_LIST_TYPE=%22multi%22; pwa2=%220%7C0%7C3%7C1%22; passport_assist_user=CjwjGSpftw_P7OeSFdWhIJFEc7HoN0s8mQMFzKd6einiH0GiCfvI-ZojSjXMX24LgiB3tljHhGEkRAdChBMaSAo8BPQ0vu1FcgycyUso5N0DnBq9lyXe4LH_C3xFZiRtRlIgDnvULWwOc3tKdwEO6npYeNselTD9uKNp7-lLELmntQ0Yia_WVCIBA4NA3Jw%3D; n_mh=Y4mnv0O1fs1r21s6RJ1i417fc86gMq6iIw0ek-d4nLc; sso_uid_tt=ba41ca0cc1e3c863d61b2d002b064b9f; sso_uid_tt_ss=ba41ca0cc1e3c863d61b2d002b064b9f; toutiao_sso_user=349b9c1d52e7d033d4812fbf6ec395c4; toutiao_sso_user_ss=349b9c1d52e7d033d4812fbf6ec395c4; sid_ucp_sso_v1=1.0.0-KGVlNjFmNzdjMTA2ZDFkZWUxYmM3N2E3OThhY2I4YTAwZTU3YjgwZTcKHQjV59SS3QEQkvf-pAYY7zEgDDDmvfHHBTgGQPQHGgJscSIgMzQ5YjljMWQ1MmU3ZDAzM2Q0ODEyZmJmNmVjMzk1YzQ; ssid_ucp_sso_v1=1.0.0-KGVlNjFmNzdjMTA2ZDFkZWUxYmM3N2E3OThhY2I4YTAwZTU3YjgwZTcKHQjV59SS3QEQkvf-pAYY7zEgDDDmvfHHBTgGQPQHGgJscSIgMzQ5YjljMWQ1MmU3ZDAzM2Q0ODEyZmJmNmVjMzk1YzQ; passport_auth_status=4805b41034a7290c25be14f05c011110%2C; passport_auth_status_ss=4805b41034a7290c25be14f05c011110%2C; uid_tt=e2fe5494da4fc8813d6fabbc78754747; uid_tt_ss=e2fe5494da4fc8813d6fabbc78754747; sid_tt=e305851a1174258581b1b57372fb4352; sessionid=e305851a1174258581b1b57372fb4352; sessionid_ss=e305851a1174258581b1b57372fb4352; bd_ticket_guard_server_data=; __security_server_data_status=1; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtY2xpZW50LWNlcnQiOiItLS0tLUJFR0lOIENFUlRJRklDQVRFLS0tLS1cbk1JSUNGRENDQWJ1Z0F3SUJBZ0lWQUlDZncrSjA1T0tSM3NJc3BCZHRwN2gxZElzck1Bb0dDQ3FHU000OUJBTUNcbk1ERXhDekFKQmdOVkJBWVRBa05PTVNJd0lBWURWUVFEREJsMGFXTnJaWFJmWjNWaGNtUmZZMkZmWldOa2MyRmZcbk1qVTJNQjRYRFRJek1EY3dNVEExTXpjeU5sb1hEVE16TURjd01URXpNemN5Tmxvd0p6RUxNQWtHQTFVRUJoTUNcblEwNHhHREFXQmdOVkJBTU1EMkprWDNScFkydGxkRjluZFdGeVpEQlpNQk1HQnlxR1NNNDlBZ0VHQ0NxR1NNNDlcbkF3RUhBMElBQkF1dWhaczNHQ3JIMGFWaUo0YU8zMnFIdE5FRFRPVWpES0lLQ0NldTZXUWcwdGhiZnlOdVhlTlFcbjYwZWN0VXM3ZERQSkI2ekFVV04rTVdDQkdjeXhKT2VqZ2Jrd2diWXdEZ1lEVlIwUEFRSC9CQVFEQWdXZ01ERUdcbkExVWRKUVFxTUNnR0NDc0dBUVVGQndNQkJnZ3JCZ0VGQlFjREFnWUlLd1lCQlFVSEF3TUdDQ3NHQVFVRkJ3TUVcbk1Da0dBMVVkRGdRaUJDQy8vbzd4eWxnbGF4WnRsMEJvU2QrU0diYldGdzdkdko1NXF6L2p2dWtnOERBckJnTlZcbkhTTUVKREFpZ0NBeXBXZnFqbVJJRW8zTVRrMUFlM01VbTBkdFUzcWswWURYZVpTWGV5SkhnekFaQmdOVkhSRUVcbkVqQVFnZzUzZDNjdVpHOTFlV2x1TG1OdmJUQUtCZ2dxaGtqT1BRUURBZ05IQURCRUFpQlRkZU1WcS8vbHY4ZkpcbmZZVHdXN1hpVFFDd3lrSU4ySnVDNU5Xd0ptcWhZQUlnZGRWcWYwUW9iTUVydmdXNHhqa2Q5WklGOU9LenhNQmtcbjloOFJHaHQ2MnVRPVxuLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLVxuIn0=; publish_badge_show_info=%220%2C0%2C0%2C1688189848844%22; sid_guard=e305851a1174258581b1b57372fb4352%7C1688189851%7C5183994%7CWed%2C+30-Aug-2023+05%3A37%3A25+GMT; sid_ucp_v1=1.0.0-KDQ4ZjIzODgyODBlYTQxNDQwZTEwODM4MzM3MjJjMjA4ZmFlZTFjYTkKGQjV59SS3QEQm_f-pAYY7zEgDDgGQPQHSAQaAmxxIiBlMzA1ODUxYTExNzQyNTg1ODFiMWI1NzM3MmZiNDM1Mg; ssid_ucp_v1=1.0.0-KDQ4ZjIzODgyODBlYTQxNDQwZTEwODM4MzM3MjJjMjA4ZmFlZTFjYTkKGQjV59SS3QEQm_f-pAYY7zEgDDgGQPQHSAQaAmxxIiBlMzA1ODUxYTExNzQyNTg1ODFiMWI1NzM3MmZiNDM1Mg; LOGIN_STATUS=1; store-region=cn-hk; store-region-src=uid; csrf_session_id=ba6c9d229ec0314e986b6b5c0a9fb8e0; douyin.com; device_web_cpu_core=12; device_web_memory_size=8; webcast_local_quality=null; strategyABtestKey=%221688271800.378%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1688898483554%2C%22type%22%3Anull%7D; odin_tt=02fe7fdafd16798667cb374ba37f592186a248e6e1c2f904a5c22cd68fc602d7faed0e3d8fd03922267536c1fed48798; __ac_nonce=064a151600034d4bcf5dd; __ac_signature=_02B4Z6wo00f01rYhkhQAAIDDSG3uJA3BF9q2AZaAAMk1bTqNXaH6SXvKJ8Bp4ROjXjWfnU6l4qId9dtPH6eTX.EsFUvNYAhtzpqFoiAYbDBI9iG1V2xMWbbGkgtJVGhfzz5se5UdCbc9U4ETc1; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA2Yc1luIyAuTBbKz9OqSyuxsows61q16KNKwfQvSZtvA%2F1688313600000%2F0%2F0%2F1688294863997%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAA2Yc1luIyAuTBbKz9OqSyuxsows61q16KNKwfQvSZtvA%2F1688313600000%2F0%2F0%2F1688295463997%22; msToken=uu0JtKIYX2n2KXkdac5t5XnvsTWNmaNueh-2jSgbdvGn5gQr9YIeB4EAmpqM0QjxMs6V_V6zO68DhPvRxdLj0aOyGA8E-Bl_dHqK6Cm0EYDXtMYMN5pQ0lA=; msToken=dEEnLKdO36QhlEzPxVj0i-6PIWQ6KW7_EGL6106-hwVQVSbM9A_8sBmADlMrSw2P-G3n8XKRMSj2NkX5PZeYyqJfOQ0JOLNvQ2SgudLGQRnJ99FOIBOhfCQ=; home_can_add_dy_2_desktop=%221%22; tt_scid=INpaDenhobVjRhJ5e2gwB4F6a15LJYfPO4QQLbnAZ1ZgycFirToucdeFfmi3fpgpe20f; passport_fe_beating_status=false',  # 登录后输入自己的Cookie
        "referer": "https://www.douyin.com/search/%E8%B6%B3%E7%90%83?publish_time=0&sort_type=1&type=aweme_general",
        "User-Agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    }
    #
    resp = requests.get(url, headers=headers)
    respss = json.loads(resp.text)
    writeContent = ""
    for i in respss['data'][:-1]:
        try:
            url = i['aweme_info']['video']['play_addr']['url_list'][0]
            name = i['aweme_info']['desc']
            aweme_id = i['aweme_info']['aweme_id']
            bofangliang = i['aweme_info']['statistics']['digg_count']
            print(name)
            if bofangliang > max_bofangliang and gjc_name in name:
                if not os.path.exists(f'./{gjc_name}'):  # 如果作者文件夹不存在，就创建
                    os.mkdir(f'./{gjc_name}')  # 如果作者文件夹不存在，就创建一个
                video_name = name  # 获取视频名称
                video_name = video_name.replace('\n', ' ')  # 吧\n替换成空格
                video_name = re.sub(r'[\/:*?"<>|]', '-', video_name)  # 替换文件名中的特殊字符
                writeContent = writeContent + "名字:"+video_name+" 播放量:"+bofangliang
                #resp = requests.get(url)
                #file_object = open(f'./{gjc_name}/{bofangliang}_{video_name}.mp4', mode='wb')
                #file_object.write(resp.content)
                #file_object.close()
                print(f'第{nn}个视拼，名称：{bofangliang}_{video_name}')
                nn += 1
        except:
            print("pass")
            pass
    htmlContent = open(f"content.txt", 'wb')
    print(writeContent)
    htmlContent.write(writeContent.encode())
    #htmlContent.write(str(respss).encode())
    break
    time.sleep(5)
    sun_s += 1
    print(sun_s)