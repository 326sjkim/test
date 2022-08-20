""" 
# 13교시 셀레니움 기본 : framework
# 클릭(dynamic)하게 처리할 수 있다.
1. pip install selenium
2. 크롬 버전 확인하고, 그에 맞는 크롬 드라이버 설치(지금 사용하고 있는것은 90이다.)
위치 조심해야 된다. 현재 내 위치가 폴더가 Python폴더
1) 잉. run이 안된다. 삼각형(run ~ in terminal) 눌러서 실행은 된다. 왜 그런지?

3. 글자 치려면 Keys 넣어야 한다.
"""

from os import system
import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#import chromedriver_autoinstaller
#chromedriver_autoinstaller.install()

system("cls")

driver = webdriver.Chrome() 
# driver.set_window_size(1024,800)

# #1. 네이버 이동
url = "http://www.naver.com"
driver.get(url)

# class 이름이 classname을 찾을 때까지 5초간 기다려라
# try:
#     element = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.CLASS_NAME , 'classname'))
#     )
# finally:
#     driver.quit()

# # 2. 로그인 버튼 클릭
elem = driver.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력 : 입력 받는 부분 바꼈다.
driver.find_element_by_id("id").send_keys("test_id") 
driver.find_element_by_id("pw").send_keys("test_pass") 

# # 4. 로그인 버튼 클릭
driver.find_element_by_id("log.login").click()  # log_login을 log.login으로 바꿔놨네.

time.sleep(3)  # 3초 기다림

# 5. 아이디를 잘 못 썼다. 새로 입력
driver.find_element_by_id("id").clear()   #지우기.. 
driver.find_element_by_id("id").send_keys("326sjkim") 

# # 6. html 정보 출력
print(driver.page_source)

# # 7. 종료
# #driver.close()   # 탭만 종료


system("pause")
driver.quit()   # 브라우저 전체 종료 

# elem = browser.find_element_by_class_name("link_login")
# elem.click()

# browser.back()
# browser.forward()

# from selenium.webdriver.common.keys import Keys
# elem.send_keys("나도코딩")
# elem.send_keys(keys.ENTER)

# elem = browser.find_element_by_class_name("link_login")
# elem
#elem.click()
#elem.back()
# elem = browser.find_element_by_id("query")
# from selenium.webdriver.common.keys import Keys
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)







