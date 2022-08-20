''' 
17. 
1) 굳이 화면을 볼필요가 없을 때,  크롬이 없는 크롬 (background에서 동작한다.)
예제는 앞에꺼 그대로 가지고 와서.

2) 아래쪽에서 스크린 샷을 찍는다.
'''
from selenium import webdriver

# 17교시~~~ Keypoint 
# 크롬띄우기 전에
options = webdriver.ChromeOptions()
options.headless = True
# 원래는 여기까지만 하면 되는데, 명시적으로 윈도우 사이즈를 알려준다.
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
#browser = webdriver.Chrome()
browser.maximize_window()

url = "https://play.google.com/store/movies/top"

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

# 17교시 스크린샷 찍자
browser.get_screenshot_as_file(r"./scraping/google_movie.png")

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
    17교시 2번 : 할인된 영화 정보 가져오기 
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
        
    
        
        









