""" 
12교시. 네이버에서 시가 총액 가져와서 csv로 저장하기

1. 페이지당 50위, 1 ~ 200위까지 가지고 온다. 4페이지까지
1페이지는 페이지 정보가 안 나온다.
https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0
2페이지에 페이지 정보가 있다
https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=2

2. 데이터 추출해서 정리한다. 빈칸은 없애고, 좌우 공백 지우고
빈데이터, 공백, \n, \t
data = [column.get_text().strip() for column in columns]  # ********** 한줄 for
tr에 대해 td가 하나만 있으면 스킵

3. 제목을 리스트로 만들기 웹문서에서 복붙하여 정리

"""

import csv  # comma seprated value
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "./scraping/시가총액1-200.csv"
fcsv = open(filename, "w", encoding="utf-8-sig", newline="")  # newline을 지우자.
writer = csv.writer(fcsv)
# 아래쪽에서 리스트를 한 줄씩 넣자. writer.writerow(data), writerow는 리스트 출력하는거다.
# utf8 -> 엑셀에서 한글이 깨지면 utf-8-sig
#f = open("./scraping/주식.html", "w+", encoding="utf-8-sig")
# with open("주식.html", "w", encoding="utf-8") as f:
#     f.write(res.text)


# 3. 제목을 리스트로 만들기.
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
# .split("\t")을 이용해서 리스트로 만든다. ["N","종목명","현재가",....]
writer.writerow(title) 

# td를 바로 가져오기 힘들기 때문에, table을 가져와서 td를 추출한다.
# table을 가져와서 td를 추출한다.
# th에도 td가 있고, tbody에도 td가 있으니 원하는 자료를 추출할려면 어떻게 해야 할까?
for page in range(1, 3):
    res = requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    #f.write(res.text)

    # table정보를 가지고 온다.
    data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:
            continue
        data = [column.get_text().strip() for column in columns]  # ********** 한줄 for
        # print(data)
        writer.writerow(data)

    # endfor
# endfor
fcsv.close()
#f.close()

print("완료")
