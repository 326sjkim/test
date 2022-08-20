"""
8교시. 가우스 전자 
웹툰 링크 가져오기.
"""

from os import system
import requests
from bs4 import BeautifulSoup

system("cls")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/87.0.4280.66 Safari/537.36"}
url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class": "title"})
title = cartoons[0].a.get_text()
link = cartoons[0].a["href"]
print(title)
print("http://comic.naver.com/"+link)


# for cartoon in cartoons:
#     print(cartoon)
