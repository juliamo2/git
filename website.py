#导入需要的模块
import requests
import random
import re

def getweb():
    url='https://api.live.bilibili.com/room/v1/Room/room_init?id=673595'
    #准备浏览器头部
    User_Agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    ips=[ {'HTTPS':'121.228.64.21 808','HTTP':'124.235.181.175 80'}]
    response=requests.get(
        url,
        headers={'User-Agent':random.choice(User_Agent)},
        proxies=random.choice(ips) # 把代理IP增加进去
    )
    html=response.text
    return html

def main():

    html = getweb()
    for i in range(len(html)):
        if html[i] == 'l' and html[i+1] == 'i' and html[i+2] == 'v' and html[i+3] == 'e' and html[i+5] == 's' and html[i+6] == 't':
            print(html[i+13])


    print(html)

main()
##"live_status":0