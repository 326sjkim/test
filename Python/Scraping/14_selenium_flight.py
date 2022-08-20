""" 
14교시.
셀레니움을 이용해서 클릭하는데, 같은 정보들이 있을 때, 어떻게 선택하는가?
5월 27일 28일 선택 ~ 6월 27일 28일 선택

"""

# 네이버 항공권

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# USB 에러 메시지 

browser = webdriver.Chrome()
#browser.maximize_window()  #창 최대화

url = "http://flight.naver.com/flights"
browser.get(url)

browser.find_element_by_link_text("가는날 선택").click()

# find_element~ : 단수, find_elements~ : 복수 -> 리스트로 

#이번달  #다음달  같은날 구분
browser.find_elements_by_link_text("27")[0].click()  # [0] 이번달
#browser.find_elements_by_link_text("28")[0].click()  # [0] 이번달

#이번달  #다음달  같은날 구분
#browser.find_elements_by_link_text("27")[1].click()  # [1] 다음달
browser.find_elements_by_link_text("28")[1].click()  # [1] 다음달


#제주도 선택
# browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]/div/a").click()
# 위의 식으로는 안된다. 
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()
browser.find_element_by_link_text("항공권 검색").click()


# 첫번째 결과 출력 browser.find_element_by_???
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li")
# print(elem.text)
# 위에걸로 에러난다.
# 1. 단순히 waiting, 
# 2. 기본 대기시간에 element가 나올때까지 기다린다.

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li" ))
    print(elem.text)

finally:
    browser.quit()        
