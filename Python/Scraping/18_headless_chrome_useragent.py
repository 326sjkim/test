''' 
18. 
주의 사항.
17교시처럼 하면 
 Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36  (KHTML, like Gecko) HeadlessChrome/90.0.4430.212 Safari/537.36
HeadlessChrome라는 정보가 넘어간다. 

해결책은 options에 "user-agent"를 추가시켜준다.
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36
처럼 chrome가 넘어간다.

추가로 공부하려면 selenium with python 사이트에 정보가 많다.


'''
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
# 원래는 여기까지만 하면 되는데, 명시적으로 윈도우 사이즈를 알려준다.
# options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

browser = webdriver.Chrome('d:\Myworkspace\chromedriver.exe', options=options)
#browser = webdriver.Chrome()
# browser.maximize_window()

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 
# (KHTML, like Gecko) HeadlessChrome/90.0.4430.212 Safari/537.36

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
browser.get(url)

detected_value = browser.find_element_by_id('detected_value')
print(detected_value.text)

browser.quit()












