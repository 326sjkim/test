""" 9교시
쿠팡에서 노트북 사기 위한 정보 추출하기
첫페이지에 페이지 정보가 없다, 두번째 페이지부터 정보가 나온다. 
page1은 없고 page2만 나온다.
get : url에 정보를 넣어서 보냄
https://www.coupang.com/np/search?minPrice=1000&maxPrice=2000
post : 정보를 숨겨서 보낼때
https://www.coupang.com/np/search?id=kkk&pass=1234
웹스크레핑은 get 사용하는 사이트가 쉽다.

* 정보를 가지고 있는 태그를 정확하게 구분하고 찾는 것이 중요하다. 
-> 정규식으로 만들어야 된다.
1. 리스트를 만들고
2. 필요한 정보들만 추려낸다.
3. 첫 페이지만 검사하는 거다.
 """

import requests
import re
from bs4 import BeautifulSoup

# url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=& \
# eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36 \
# &filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
url = "https://www.coupang.com/np/search? \
    q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')
# print(res.text)

with open("./scraping/쿠팡2.html", "w", encoding="utf-8-sig") as f:
    f.write(res.text)

print("\n--------------- 쿠팡 노트북 검색  -----------------------")
items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

# 리뷰 100개 이상, 평점 4.5 이상
for item in items:
    # 광고 제품 제외
    ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
    if ad_badge:
        # print("<광고 상품 제외>")
        continue

    name = item.find("div", attrs={"class": "name"}).get_text()  # 이름
    # 애플 제품 제외
    if "Apple" in name:
        # print("<Apple 제외>")
        continue

    price = item.find("strong", attrs={"class": "price-value"}).get_text()  # 가격

    # 리뷰 100개 이상, 평점 4.5이상
    rate = item.find("em", attrs={"class": "rating"})  # 평점
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"
        # print("<평점 없는 상품 제외>")
        continue

    rate_cnt = item.find("span", attrs={"class": "rating-total-count"})  # 리뷰수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()  # 형식 (36)
        rate_cnt = rate_cnt[1:-1]   # (빼고,  뒤에꺼 빼고)

    else:
        rate = "평점 수 없음"
        # print("<평점 수 없는 상품 제외>")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) > 100:
        print(name, price, rate, rate_cnt)
