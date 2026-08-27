from bs4 import BeautifulSoup
import os, re, json
import pandas as pd
from urllib import request
from openpyxl import load_workbook
from  bilibili.append_xlsx import append_df_to_excel


# 获取页面的所有的avid, title, url
def parse_html(content):
    arr = []
    # 使用beautifulsoup解析html文档
    soup = BeautifulSoup(content)
    # 获取指定标签
    tag_list = soup.find_all("a", attrs={'title': True, 'href': True, "class": "title"})
    # tag_list = soup.find_all("span", attrs={'class': 'type avid'})
    for tag in tag_list:
        # print(tag.get("title"), tag.get("href"))
        # 获取标签内容，并去除首尾空格
        title = tag.get("title")
        href = tag.get("href")[2:]
        avid = re.search("av([0-9]*)", href).group(0)
        base_dict[avid] = [avid, title, href]
    return base_dict.keys()

# 读取路径文件名
def read_path(path):
    path_set = set()
    dir_path = os.listdir(path)
    for item in dir_path:
        child = os.path.join('%s/%s' % (path, item))
        path_set.add(child)
    return path_set

# 提取html文件
def filter(path_set):
    filterable = []
    pattern = re.compile(r'.*\.[html|htm]+', re.I)
    for path in path_set:
        m = pattern.match(path)
        if m:
            filterable.append(m.group(0).strip())
    return filterable

# 读取文件内容
def read_html(path):
    file = open(path.encode('utf-8').strip(), 'r', encoding="utf-8")
    content = file.read()
    return content

# 写入csv
def storeCSV(filename=r'/Users/robbin/Desktop/bilibili/bilibili.xlsx'):
    df_base = pd.DataFrame.from_dict(base_dict, orient="index")
    df_base.columns = ['avid', 'title', 'href']
    df_tags = pd.DataFrame.from_dict(tags_dict, orient="index")
    df_tags.columns = ['tags']
    df_info = pd.DataFrame.from_dict(info_dict, orient='index')
    df_info.columns = ['like', 'his_rank', 'view', 'now_rank', 'coin', 'reply', 'aid', 'no_reprint', 'favorite', 'danmaku', 'copyright', 'share']
    df = df_base.join([df_tags, df_info])
    append_df_to_excel(filename, df, index=False)

#  根据avid请求api获得视频信息
def query_info(avid):
    stat_url = "https://api.bilibili.com/x/web-interface/archive/stat?aid="
    id = avid[2:]
    url = stat_url + id
    response = request.urlopen(url)
    return response.read().decode("utf-8")

#  根据avid请求api获得视频标签
def query_tags(avid):
    stat_url = "https://api.bilibili.com/x/tag/archive/tags?aid="
    id = avid[2:]
    url = stat_url + id
    response = request.urlopen(url)
    return response.read().decode("utf-8")

if __name__ == '__main__':
    print("now read folder...")
    path_set = read_path("/Users/robbin/Desktop/bilibili")
    print("parse file path finshed...")
    filterable = filter(path_set)

    for path in filterable:
        base_dict = {}
        tags_dict = {}
        info_dict = {}
        print("now parse the file:", path)
        content = read_html(path)
        avid_list = parse_html(content)

        for avid in avid_list:
            print("Proccessing:", avid)
            tags_json = query_tags(avid)
            tags_obj = json.loads(tags_json)
            tags_row_list = tags_obj.get("data")
            if tags_row_list:
                # print(data)
                tag_list = []
                for item in tags_row_list:
                    tag_name = item.get("tag_name")
                    tag_list.append(tag_name)
                tag = ",".join(tag_list)
                tags_dict[avid] = tag

            info_json = query_info(avid)
            info_obj = json.loads(info_json)
            info_row_dict = info_obj.get("data")
            if info_row_dict:
                info_dict[avid] = list(info_row_dict.values())
        print("Start to writing ", path, " to xls")
        storeCSV()
        print("End of writing ", path, " to xls")
