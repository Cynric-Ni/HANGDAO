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

i=0

info_link={}

info_text={}

for link in html.find_all('a'):
    
    i+=1
   
    #把href中的内容赋值给info_link##
    info_link[i]=link.get('href')
    
    #把a标签中的文字赋值给info_text,并去除空格###
    info_text[i]=link.get_text(strip=True)
    
    #打印出info_text和info_link，并换行
    #数组第28位为第一个##
print(info_text[28])

print(info_link[28]+'\n')

##补全./202005/t20200506_119416.htm##
print('http://www.cjhdj.com.cn/zzq/whhdj/xwzx/hdyw'+info_link[28][2:29]+'\n')