import re
from urllib import parse
from pprint import pprint
import requests
import urllib # 打开网页链接

url = "https://www.douyin.com/search/%E7%AF%AE%E7%90%83?aid=a5c50525-5c37-4f29-96f8-555e4d31c379&publish_time=0&sort_type=0&source=normal_search&type=general"

headers = {
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                'Sec-Fetch-Dest':'empty',
                'Sec-Fetch-Mode':'cors',
                'Sec-Fetch-Site':'same-origin',
                'cookie': 'xgplayer_user_id=87532903329; ttwid=1%7CIZ9z_fzonOI1w0M0WkZRJ3H7m9c5oXqR9ueVwlRu7Rk%7C1679712264%7C589fb18c65b7ff361661cc2a50719509733648630258ba7475684f7d88007625; passport_csrf_token=96001efe794a5a80eb7f59e4d53843e5; passport_csrf_token_default=96001efe794a5a80eb7f59e4d53843e5; __bd_ticket_guard_local_probe=1687606845237; s_v_web_id=verify_ljiod9k3_QHLpy1vp_peBu_4343_85ox_odUkK4YNKxTO; strategyABtestKey=%221688164978.907%22; download_guide=%223%2F20230701%2F0%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; SEARCH_RESULT_LIST_TYPE=%22multi%22; pwa2=%220%7C0%7C3%7C1%22; passport_assist_user=CjwjGSpftw_P7OeSFdWhIJFEc7HoN0s8mQMFzKd6einiH0GiCfvI-ZojSjXMX24LgiB3tljHhGEkRAdChBMaSAo8BPQ0vu1FcgycyUso5N0DnBq9lyXe4LH_C3xFZiRtRlIgDnvULWwOc3tKdwEO6npYeNselTD9uKNp7-lLELmntQ0Yia_WVCIBA4NA3Jw%3D; n_mh=Y4mnv0O1fs1r21s6RJ1i417fc86gMq6iIw0ek-d4nLc; sso_uid_tt=ba41ca0cc1e3c863d61b2d002b064b9f; sso_uid_tt_ss=ba41ca0cc1e3c863d61b2d002b064b9f; toutiao_sso_user=349b9c1d52e7d033d4812fbf6ec395c4; toutiao_sso_user_ss=349b9c1d52e7d033d4812fbf6ec395c4; sid_ucp_sso_v1=1.0.0-KGVlNjFmNzdjMTA2ZDFkZWUxYmM3N2E3OThhY2I4YTAwZTU3YjgwZTcKHQjV59SS3QEQkvf-pAYY7zEgDDDmvfHHBTgGQPQHGgJscSIgMzQ5YjljMWQ1MmU3ZDAzM2Q0ODEyZmJmNmVjMzk1YzQ; ssid_ucp_sso_v1=1.0.0-KGVlNjFmNzdjMTA2ZDFkZWUxYmM3N2E3OThhY2I4YTAwZTU3YjgwZTcKHQjV59SS3QEQkvf-pAYY7zEgDDDmvfHHBTgGQPQHGgJscSIgMzQ5YjljMWQ1MmU3ZDAzM2Q0ODEyZmJmNmVjMzk1YzQ; odin_tt=3e92e36be9f00231b87a35ed9b4bfa59241c8f909c682ae0e8f8fdc9c8de83d9c79e97bc58ddaa84bd9511d0231456e7; passport_auth_status=4805b41034a7290c25be14f05c011110%2C; passport_auth_status_ss=4805b41034a7290c25be14f05c011110%2C; uid_tt=e2fe5494da4fc8813d6fabbc78754747; uid_tt_ss=e2fe5494da4fc8813d6fabbc78754747; sid_tt=e305851a1174258581b1b57372fb4352; sessionid=e305851a1174258581b1b57372fb4352; sessionid_ss=e305851a1174258581b1b57372fb4352; bd_ticket_guard_server_data=; __security_server_data_status=1; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtY2xpZW50LWNlcnQiOiItLS0tLUJFR0lOIENFUlRJRklDQVRFLS0tLS1cbk1JSUNGRENDQWJ1Z0F3SUJBZ0lWQUlDZncrSjA1T0tSM3NJc3BCZHRwN2gxZElzck1Bb0dDQ3FHU000OUJBTUNcbk1ERXhDekFKQmdOVkJBWVRBa05PTVNJd0lBWURWUVFEREJsMGFXTnJaWFJmWjNWaGNtUmZZMkZmWldOa2MyRmZcbk1qVTJNQjRYRFRJek1EY3dNVEExTXpjeU5sb1hEVE16TURjd01URXpNemN5Tmxvd0p6RUxNQWtHQTFVRUJoTUNcblEwNHhHREFXQmdOVkJBTU1EMkprWDNScFkydGxkRjluZFdGeVpEQlpNQk1HQnlxR1NNNDlBZ0VHQ0NxR1NNNDlcbkF3RUhBMElBQkF1dWhaczNHQ3JIMGFWaUo0YU8zMnFIdE5FRFRPVWpES0lLQ0NldTZXUWcwdGhiZnlOdVhlTlFcbjYwZWN0VXM3ZERQSkI2ekFVV04rTVdDQkdjeXhKT2VqZ2Jrd2diWXdEZ1lEVlIwUEFRSC9CQVFEQWdXZ01ERUdcbkExVWRKUVFxTUNnR0NDc0dBUVVGQndNQkJnZ3JCZ0VGQlFjREFnWUlLd1lCQlFVSEF3TUdDQ3NHQVFVRkJ3TUVcbk1Da0dBMVVkRGdRaUJDQy8vbzd4eWxnbGF4WnRsMEJvU2QrU0diYldGdzdkdko1NXF6L2p2dWtnOERBckJnTlZcbkhTTUVKREFpZ0NBeXBXZnFqbVJJRW8zTVRrMUFlM01VbTBkdFUzcWswWURYZVpTWGV5SkhnekFaQmdOVkhSRUVcbkVqQVFnZzUzZDNjdVpHOTFlV2x1TG1OdmJUQUtCZ2dxaGtqT1BRUURBZ05IQURCRUFpQlRkZU1WcS8vbHY4ZkpcbmZZVHdXN1hpVFFDd3lrSU4ySnVDNU5Xd0ptcWhZQUlnZGRWcWYwUW9iTUVydmdXNHhqa2Q5WklGOU9LenhNQmtcbjloOFJHaHQ2MnVRPVxuLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLVxuIn0=; publish_badge_show_info=%220%2C0%2C0%2C1688189848844%22; sid_guard=e305851a1174258581b1b57372fb4352%7C1688189851%7C5183994%7CWed%2C+30-Aug-2023+05%3A37%3A25+GMT; sid_ucp_v1=1.0.0-KDQ4ZjIzODgyODBlYTQxNDQwZTEwODM4MzM3MjJjMjA4ZmFlZTFjYTkKGQjV59SS3QEQm_f-pAYY7zEgDDgGQPQHSAQaAmxxIiBlMzA1ODUxYTExNzQyNTg1ODFiMWI1NzM3MmZiNDM1Mg; ssid_ucp_v1=1.0.0-KDQ4ZjIzODgyODBlYTQxNDQwZTEwODM4MzM3MjJjMjA4ZmFlZTFjYTkKGQjV59SS3QEQm_f-pAYY7zEgDDgGQPQHSAQaAmxxIiBlMzA1ODUxYTExNzQyNTg1ODFiMWI1NzM3MmZiNDM1Mg; LOGIN_STATUS=1; store-region=cn-hk; store-region-src=uid; csrf_session_id=ba6c9d229ec0314e986b6b5c0a9fb8e0; douyin.com; device_web_cpu_core=12; device_web_memory_size=8; webcast_local_quality=null; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAA2Yc1luIyAuTBbKz9OqSyuxsows61q16KNKwfQvSZtvA%2F1688227200000%2F0%2F0%2F1688199170111%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1688809292197%2C%22type%22%3Anull%7D; __ac_nonce=0649ffe3a00bcd9ec3421; __ac_signature=_02B4Z6wo00f0145joJQAAIDCcC.cpWdPUCeOU6QAAIcPQHFj7EtVB3cYbQjZ7y5Vteij2LkvjCUpj.X8pwL8L8NZlBgxQAHxMJkT-CuZipnSgTypSTGZWuG12B7KoXJCMsuExm9kn4oEQB4Ba1; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA2Yc1luIyAuTBbKz9OqSyuxsows61q16KNKwfQvSZtvA%2F1688227200000%2F0%2F1688206908301%2F0%22; msToken=W3Ds-XGE2e3ZHiDIbvcVQmcm9cG0Hf8Glx-WglCaxpMW1BWC5_3tFroSPdCT8FJHUDmz9w_I6O9XtIPzuzQ7km4U39dxEG5wLgbZfYaBg3M9MJ5E1ePadWk=; home_can_add_dy_2_desktop=%221%22; tt_scid=dyNfcKDyU8XK.ftoAq7Qu5p3pGg9ruUQY7.WzIfPvHllOmeyatn86y5RGoE1fCpu5b99; passport_fe_beating_status=false; msToken=e2eu-iHzX-wWTsCugXdLlSVVVJybrnyPCsyCEM1cPgRLwi0rxTmnTWgz1OBeJRCmgPCtZd2oWU1e7btbdcQveaMoD0DhC6UQ8t4DBA2RHXYgeuCUEB2qHOk='
            }

result =requests.get(url).content
 
# 读取网页内容
html = result #response.read()

htmlContent = open(f"content.txt", 'wb')
htmlContent.write(str(html).encode())