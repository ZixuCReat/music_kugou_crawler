import urllib.parse
from urllib.request import urlretrieve
import requests
import json

music_name = input()
music_rid = list()
keyword = urllib.parse.quote(music_name)
url = 'https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&httpsStatus=1'.format(keyword)
referer = 'https://www.kuwo.cn/search/list?key={}'.format(keyword)


headers = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
    'Cookie':'_ga=GA1.2.2021007609.1602479334; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1602479334,1602673632; _gid=GA1.2.168402150.1602673633; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1602673824; kw_token=ZTHBRQZ3JCQ',
    "csrf": "ZTHBRQZ3JCQ",
    "Referer": "{}".format(referer)
}

headers2 = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
}

list_resp = requests.get(url=url, headers=headers)

#音乐列表
music_list = json.loads(list_resp.text)['data']['list']
rids = list()
names = list()
for i, s in enumerate(music_list):
  print(f'{i+1}  {s.get("name")}  {s.get("artist")}')
  rids.append(music_list[i]['rid'])
  names.append(music_list[i]['name'])
num = int(input())
music_rid = rids[num - 1]

#音乐url
music_url = 'https://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&t=1602674521838&httpsStatus=1'.format(music_rid)
music_resp = requests.get(music_url, headers=headers2)

'''
#下载
download_url = json.loads(music_resp.text)['url']
path = 'D:\PycharmProjects\pythonProject1\music'
urlretrieve(url=download_url, filename=path+f'\{names[id-1]}.mp3')
'''