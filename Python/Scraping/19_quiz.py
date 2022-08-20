''' 
19 교시. 
때에 따라 셀레니움이 필요한지는 모른다.
user-agent를 넣어야 될 수도 있다.

1. requests와 soup을 이용해서 정보가 있는지 출력해본다.

2. table에 있는 아래 정보다.

1) find
data1 = find("table",attrs={"class":"클래스명"})
data2 = data.find("~~~")
data3 = data2.find~~~
2)find_all
    soup에서는 xpath가 안된다.ㅠㅠ 비슷하게 흉내는 낼수 있다. [0]



'''

from os import write
import requests
from bs4 import BeautifulSoup

url='https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# 1) 원하는 정보가 있는지 html로 출력해본다.
# with open("./scraping/quiz.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())
# f.close()    

# table = soup.find("table", attrs={'class':"tbl"})
data_rows = soup.find("table", attrs={'class':"tbl"}).find("tbody").find_all("tr")
for idx, row in enumerate(data_rows):
    columns = row.find_all("td")
    
    print(f"========== 매물 {idx+1}===========")
    print("거래 :"+ columns[0].get_text().strip())
    print("면적 :"+ columns[1].get_text()+"(공급/전용)")
    print("가격 :"+ columns[2].get_text()+"만원")
    print("동 :"+ columns[3].get_text())
    print("층 :"+ columns[4].get_text())
    