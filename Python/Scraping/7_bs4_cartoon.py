"""
7교시. 
"""

from os import system
#import os
#from os import *

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

system("cls")

# html = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=733766")
# print(html)
# soup = BeautifulSoup(html, "lxml")  # lxml, html.parser, html5lib
# print(soup.title)
# print(soup.title.get_text()
# print(soup.a)            #첫번째 a
# print(soup.a.attrs)    # a의 속성정보
# print(soup.a["href"])  # a의 href의 속성 값 정보

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/87.0.4280.66 Safari/537.36"}
url = "https://comic.naver.com/webtoon/weekday.nhn"


res = requests.get(url, headers=headers)
res.raise_for_status()

#html = res.text
soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class": "title"})
for cartoon in cartoons:
    print(cartoon.get_text())
