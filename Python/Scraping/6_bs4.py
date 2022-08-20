"""
6교시. beautiful soup
설치 : pip install beautifulsoup4
 pip install lxml --upgrade (업그레이드 할려면.)  lxml : 파서
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

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
url = "https://comic.naver.com/webtoon/list.nhn?titleId=733766"
# print(url)

# url="https://www.naver.com/"
# url="https://comic.naver.com/webtoon/weekday.nhn"
# url = "https://comic.naver.com/webtoon/list.nhn?titleId=733766"
# res=requests.get(url, headers = {"User-Agent":headers})

res = requests.get(url, headers=headers)
res.raise_for_status()

#html = res.text
soup = BeautifulSoup(res.text, "lxml")
"""
res.text를 lxml 파서를 이용해서 객체로 만들어 준다. 여기서 원하는 정보를 꺼내면 된다. 
예.
soup.title, soup.title.get_text()
soup.a : 첫번째 a,  soup.a.attrs, soup.a["href"] : 원하는 속성 값만 
페이지에 대한 이해가 높을 때다. 안 그러면 findall, find

통상 잘 모른다. 유일한 정보를 이용한다. ->
soup.find("a", attrs={"class":"Nbtn_upload"})  // class의 값이 ~인 a를 찾아줘.
soup.find(attrs={"class":"Nbtn_upload"})   // 유일하다. class의 값이 ~인 어떤 element를 찾아줘.
"""

# print('\n'*100)
# 4부 필요한 정보 가져오기 - 평점 가져오기
# cartoons = soup.find_all("div", attrs={"class":"rating_type"})
# for cartoon in cartoons:
#     rate = cartoon.find("strong").get_text()
#     print(rate)

"""
네이버 카툰에서 인기급상승 만화 랭킹대로 가져오기한다.
"""
rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a.get_text())
rank2 = rank1.find_next_sibling()    # siblingm next_siblings("li")
print(rank2.a.get_text())

# rank2 = rank1.next_sibling.next_sibling  # 다음 형제로, 전 형제로, 부모로, 자식으로
# rank2 = rank1.previous_sibling# .previous_sibling
# rank2 = rank1.find_next_siblings("li")  # 조건에 맞는 시블링을 찾아라.
# print(rank2)

print('\n')
rank3s = rank1.find_next_siblings("li")   # rank1을 기준으로 모두 가져온다.
for rank3 in rank3s:
    print(rank3.a.get_text())

# 알고 있는 문자열을 이용해서 태그 가져오기
webtoon = soup.find("a", text="독립일기-91화 밥도둑 만들기")
print(webtoon)

# print(rank1.next_sibling.next_sibling.get_text())
print("----- 종료 ------")


'''
#3부 필요한 값들 읽어오기
cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com"+link)
# 만화 제목 링크 가져오기
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)
'''
'''
#2부 a태그의 class이름이 title인것 가져오기 : fina_all


cartoons = soup.find_all("a",attrs={"class":"title"})
# print(cartoons)
for cartoon in cartoons:
    print(cartoon.get_text())

'''

'''
# 1부 기본 연습
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)  # 첫번째 a 출력
# #print(soup.a)
# print(soup.a.attrs)
# print(soup.a["href"])

print(soup.find("a",attrs={"class":"Nbtn_upload"}))
print(soup.find({"class":"Nbtn_upload"}))
#webtoon = soup.find("a", text="프리드로우")
webtoon = soup.find("a", text="프리드로우-제363화 한태성의 집과 가족 (1)")
print(webtoon)

# rank1 = soup.find("li",attrs={"class":"rank01"})
# print(rank1.a)
'''
