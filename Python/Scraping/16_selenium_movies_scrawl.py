''' 
    16교시
    1) 동적 홈페이지 정보 가져오기
    스크롤하고 조금 기다렸다가, 스크롤 제일 아래까지 이동    
    동적페이지에서 제일 아래까지 이동    
    셀레니움에서 자바스크립트도 사용가능하다. 
    
    16교시 
    2). 셀레니움으로 받아온 페이지에서 원하는 정보 추출하기
    

'''

from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
''' 
페이지 접속하고 나서 조금 기다려야 된다.
'''

# 1. 지정된 위치로 스크롤 내리기
# 모니터 해상도 높이이 1080위치로 스크롤 내리기
# 1.browser.execute_script("window.scrollTo(0, 1080)")
# browser.execute_script("window.scrollTo(0, 2080)")

# 2. 화면 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초에 한번씩 스크롤 내리기

# 3. 화면 제일 아래로 스크롤 내리기
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    
    if curr_height == prev_height:
        break
    
    prev_height = curr_height
    
print("스크롤 완료")    

# 16-2)교시
''' 
import requests  # 서버에 접속
from bs4 import BeautifulSoup # html 가져와서 파싱

soup = BeautifulSoup(browser.page_source, 'lxml')

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)
 '''
# 1) 10개 밖에 못 가져 왔다.
# 2) 확인해보면 10번째 다음 영화부터 태그이름이 바뀐다.
# - 해결책은 클래스명을 리스트로 만들면 된다.
# 3) 트롤(같은 영화가 두번 가져온다.)
# Vpfmgd가 두개 있다.  -> 

import requests  # 서버에 접속
from bs4 import BeautifulSoup # html 가져와서 파싱

soup = BeautifulSoup(browser.page_source, 'lxml')

# class 속성을 리스트로 만들면 된다. 
# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    
    '''
    결과 : 1개씩 가져와서 200개 가져온다. 
    16교시 
    3) 할인된 영화 정보 가져오기 
    
    주석도 들여쓰기를 해야 한다.
    '''
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title,"<할인되지 않은 영화 제외>")
        continue
    
    #할인된 가격
    price=movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"})
    
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    # http://play.google.com + link
    
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print(f"링크 : ", "https://play.google.com" + link)
    print("-" * 120)

browser.quit()
        
    
        
        








