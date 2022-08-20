
''' 
1. visual studio 2019에서 많이 사용하는 단축키
1) 함수 정의로 이동하기) : ^click, F12, 
2) 뒤로 탐색, 앞으로 탐색 : ^- 호출문장으로 되돌아 가기, 다시 정의로 가기 : ^sh-
3) @키 활용 : 코드 위치 바꾸기 @화살표 위로, @화살표 아래로
4) @드래그
5) 문자열 찾기 : ^F, 한번에 바꾸기 : 모두바꾸기
6) solution에서 문자열 모조리 찾기 : ^sh F
7) 함수명 쉽게 변경하고, 호출하는 부분 이름 바꾸기 : ^RR
8) 자동 정렬하기 : ^KF
9) 코드 자동 완성 : tab, 언어에 따라 두번 눌러야 
10) 주석 설정, 해제 : ^KC, ^KU
11) 모든 참조 찾기 : 버전에 따라 단축키 있는 경우도 있다. 
    없으면 새로 만들자. ^sh g
    
2. 비교하기 
1) ctrl 선택    

3. 윈도우 팁 7가지
1) 화면배치 : 윈도우 화살표, 마우스 드래그로
2) 초간단 스크린샷 : 윈도우 shift s
3) 빠른 실행 : 윈도키 + R, 탐색기 : 윈도키 + E, 윈도키D, 윈도키L
4) 저장 : 단축키
5) 윈도우 잡고 흔들어라
6) ^Tab, ^sh Tab, 
'''

import sys
import os
import time
import random

from datetime import datetime
import pandas as pd  # 판다스
import numpy as np

import requests  # 서버에 접속
from bs4 import BeautifulSoup  # html 가져와서 파싱

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def MyDelay(second):
    time.sleep(random.randint(1, second))


def myselbu(url, lastelement):
    options = webdriver.ChromeOptions()
    # options.headless = True
    #
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

    driver = webdriver.Chrome(
        'd:\Myworkspace\chromedriver.exe', options=options)
    # driver.get("http://somedomain/url_that_delays_loading")
    driver.get(url)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, lastelement))
        )
    finally:
        driver.quit()

    soup = BeautifulSoup(driver.page_source, 'lxml')

    return driver, soup

# 상대경로를 받아서 절대경로로 바꾸어주는 함수


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
