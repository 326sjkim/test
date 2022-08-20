
import os, random, time
from datetime import datetime
import pandas as pd  # 판다스
import numpy as np

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import re 

Today = datetime.today().strftime("%Y%m%d")

base_url = 'https://finance.naver.com/sise/sise_group.nhn?type=upjong'

options = webdriver.ChromeOptions()
# options.headless = True
# options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(r'chromedriver.exe', options=options)
# browser.maximize_window()
# browser = Chrome()

browser.get(base_url)
time.sleep(2)

upjonglst = ["다각화된통신서비스", "사무용전자제품", "건강관리업체및서비스", "해운사", "제약", "건강관리장비와용품", "은행", \
"철강", "생물공학", "석유와가스", "가구", "생명보험", "생명과학도구및서비스", "인터넷과카탈로그소매", "손해보험", \
"포장재", "증권", "교육서비스", "호텔,레스토랑,레저", "문구류", "전기장비", "가정용기기와용품", "디스플레이장비및부품", \
"자동차부품", "담배", "항공화물운송과물류", "운송인프라", "종이와목재", "항공사", "기타", "상업서비스와공급품", \
"백화점과일반상점", "복합유틸리티", "무역회사와판매업체", "부동산", "디스플레이패널", "전문소매", "섬유,의류,신발,호화품", \
"기타금융", "화학", "음료", "IT서비스", "건강관리기술", "건축자재", "건축제품", "전기제품", "식품과기본식료품소매", \
"카드", "자동차", "창업투자", "광고", "복합기업", "판매업체", "소프트웨어", "화장품", "우주항공과국방", "기계", \
"도로와철도운송", "전기유틸리티", "비철금속", "통신장비", "양방향미디어와서비스", "가정용품", "컴퓨터와주변기기", \
"건설", "전자제품", "식품", "출판", "핸드셋", "레저용장비와제품", "전자장비와기기", "조선", "가스유틸리티", \
"방송과엔터테인먼트", "무선통신서비스", "에너지장비및서비스", "독립전력생산및에너지거래", "반도체와반도체장비", "게임엔터테인먼트"]

upjongdict = {}
CompanyLst = []

def delay():
    time.sleep(random.uniform(1,5))

f = open(f'업종리스트_{Today}.TXT','w')
for upjong in upjonglst:
    browser.find_element_by_link_text(upjong).click()
    
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    
    CompanyNamelst = soup.find_all("div", attrs={'class':'name_area'})
    
    f.write(upjong) ; f.write('\t')    
    for CompanyName in CompanyNamelst:
        CompanyNameText = CompanyName.get_text()
        CompanyLst.append(CompanyNameText)
        f.writelines(CompanyNameText) ; f.write('\t')
    
    f.write('\n')
        
    upjongdict[upjong] = CompanyLst
        
    # print(upjong)
    # print(CompanyLst)
    CompanyLst=[]
    
    browser.find_element_by_xpath('//*[@id="contentarea"]/div[4]/div/div/a').click()
    delay()

# df = pd.DataFrame(upjongdict)
# df.to_csv('upjong.csv',encoding='utf-8-sig')
f.close()


browser.quit()

print('--------- 종료 ----------')