"""
# 15교시. 동적페이지 만들기

검색어 넣고, 인기차트 키워드 넣고, 필요한 정보 가져오자.
구글 검색에서 할인하는 영화정보만 가져온다. 
"""

import requests  # 서버에 접속
from bs4 import BeautifulSoup # html 가져와서 파싱

''' 
1. html 구조를 먼저 파악해야 한다.
2. 각각의 div가 하나의 영화를 의미한다. 
3. 서버에서 거부할 때는 파일로 저장하고 무슨 이유때문인지 확인한다.
4. 확인해 봤더니, 
5. res.text를 그냥 찍으면 너무 복잡하니, soup.prettify()를 이용해서 정리하자.
6. 검색하니 정보가 나오지 않는다. 이상하다.
7. Top chart에 따라 다르다. 화면이 다르다. 
8. requests로 접속하니 미국에서 접속한 것으로 판단해 미국 정보를 보여준다.
9. user agent를 이용해서 한국에서 접속하는 것처럼 보여줘야 한다.
10. "Accept-Language":"ko-KR, ko"를 이용해서 한글 페이지를 요구한다.
11. 글자는 깨지지만, 어쨌던 정보는 나온다.
12. 문제: 받아온 html에는 영화가 10개만 뜬다. 원래는 매우 많다.
13. 스크롤을 내리면 거기에 맞추어서 새롭게 로딩한다. (마지막까지) - 동적 페이지다!!!
14. 이럴 때, 필요한 것이 셀레니움이다.
15. 순환문을 이용해서, div 혹은 text 정보를 이용해서 가져온다.
16. requests는 10개만 가져온다.
17. 구글은 header 정보에 맞추어서 웹문서를 보여준다. 대단하네!!! 
'''


url = "https://play.google.com/store/movies/top"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36", \
            "Accept-Language":"ko-KR,ko"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

# google서버에서 뷰티풀숲으로 접근시 미국으로 인식하고 서로 다른 Header 정보를 준다.
# with open("영화리스트.html", "w", encoding="utf-8") as f:
#     #f.write(res.text)
#     f.write(soup.prettify())  

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)