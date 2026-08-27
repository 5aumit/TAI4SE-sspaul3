# -*-coding:utf-8-*-
import requests



url = 'https://www.baidu.com/s?wd=IP'
headers = {
    'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/89.0.4389.90Safari/537.36'
}
# 25.122.144.141	9999
res_text = requests.get(url=url,headers=headers,proxies={'http':'25.122.144.141:9999'}).text
print(res_text)

with open('ip.html','w') as f:
    f.write(res_text.encode('gbk').decode('utf-8'))

