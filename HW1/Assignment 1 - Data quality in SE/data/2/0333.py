
# coding: utf-8

# In[61]:


import requests
import time
import lxml
from lxml import etree


# In[62]:


def Get_Html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36 Edg/86.0.622.63'}
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        print("请求失败")


# In[63]:


def Get_Info(html):
    html = etree.HTML(html)
    Mlt = html.xpath('//*[@id="__layout"]/div/div[2]/div[3]/table/tbody/tr')
    for ls in Mlt:
        rank = ls.xpath('./td[1]/text()')[0]
        name = ls.xpath('./td[2]/a/text()')[0]
        province = ls.xpath('./td[3]/text()')[0]
        score = ls.xpath('./td[4]/text()')[0]
        data = {'rank':rank.replace('\n','').replace(' ',''),'name':name,'province':province.replace('\n','').replace(' ',''),
                'score':score.replace('\n','').replace(' ','')}
        print(data)


# In[64]:


url = 'https://www.shanghairanking.cn/rankings/bcur/2020'
html = Get_Html(url)
Get_Info(html)
time.sleep(1)

