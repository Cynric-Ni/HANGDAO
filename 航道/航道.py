#conding=utf-8

import urllib.request

import requests

from bs4 import BeautifulSoup

import urllib.parse



cookie_str=r'Hm_lvt_421a98029ee1737df6d51923f48767b0=1586613569,1587829077,1588784211; bdshare_firstime=1588784243754; Hm_lpvt_421a98029ee1737df6d51923f48767b0=1588785286'

cookies = {}

for line in cookie_str.split(';'):

    key, value = line.split('=', 1)

    cookies[key] = value

url='http://www.cjhdj.com.cn/zzq/whhdj/xwzx/hdyw/'

###def get_one_page(url):###
headers = {

   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"

}

###req = requests.get(url)###
req = urllib.request.Request(url=url,headers=headers)
rsp=urllib.request.urlopen(req)

html=rsp.read().decode('utf-8','ignore')

print(html)

html=BeautifulSoup(html,'html.parser')



