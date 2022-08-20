""" 
10교시.
페이지가 여러페이지다.
쿠팡은 막아버리넹...
"""

import requests
import re
from bs4 import BeautifulSoup

from os import system
system('cls')

# 막아 버려서..
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/87.0.4280.66 Safari/537.36"}


print("\n------------- 10. 쿠팡 노트북 페이지 바꿔가면서 검색  ------------------")
for i in range(1, 6):  # for1
    #url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page="+str(i)+"&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81& \
        hannel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc \
            &minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false \
                &brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')

    if res.status_code != 200:
        print("응답코드 : ", res.status_code)  # 200이면 정상, 다른값이면 비정상
        break

    # print(res.text)

    # print("\n --- [{} 페이지] --- ".format(i))
    print(f"\n --- [{i}] 페이지 ---")
    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
    for item in items:  # for2

        # 광고 제품 제외
        ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
        if ad_badge:
            #print("<광고 상품 제외>")
            continue

        name = item.find("div", attrs={"class": "name"}).get_text()  # 이름
        # 애플 제품 제외
        if "Apple" in name:
            #print("<Apple 제외>")
            continue

        price = item.find(
            "strong", attrs={"class": "price-value"}).get_text()  # 가격

        # 리뷰 100개 이상, 평점 4.5이상
        rate = item.find("em", attrs={"class": "rating"})  # 평점
        if rate:
            rate = rate.get_text()
        else:
            rate = "평점없음"
            #print("<평점 없는 상품 제외>")
            continue

        rate_cnt = item.find(
            "span", attrs={"class": "rating-total-count"})  # 리뷰수
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()  # 형식 (36)
            rate_cnt = rate_cnt[1:-1]   # (빼고,  뒤에꺼 빼고)

        else:
            rate_cnt = "평점 수 없음"
            #print("<평점 수 없는 상품 제외>")
            continue

        link = item.find("a", attrs={"class": "search-product-link"})["href"]
        if float(rate) >= 4.5 and int(rate_cnt) > 50:
            # print(name, price, rate, rate_cnt)  #test
            # 마무리
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt}개 )")
            print("바로가기 : {}".format("https://www.coupang.com"+link))
            print("-"*50)  # 줄긋기
    # end for2
# end for1

print("검색 끝")
