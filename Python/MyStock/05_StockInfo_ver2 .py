
from urllib.request import urlopen
from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup
import pandas as pd  # 판다스
import time, datetime, random
from lxml import etree

from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def ReadCode():
    # sheet 이름 확인하자.
    KospiFile = "kospi.xlsx"
    ReadCodeNum = pd.read_excel(KospiFile, sheet_name="kospi",engine='openpyxl', dtype={"종목코드": str})
    CodeNums = ReadCodeNum["종목코드"].tolist()
    CompanyNames = ReadCodeNum["회사명"].tolist()

    KospiFile = 'kosdaq.xlsx'
    ReadCodeNum = pd.read_excel(KospiFile, sheet_name="kosdaq",engine='openpyxl', dtype={"종목코드": str})
    CodeNums.extend(ReadCodeNum["종목코드"].tolist())
    CompanyNames.extend(ReadCodeNum["회사명"].tolist())

    return CodeNums, CompanyNames

def TitleLst():
    titlelst = ["idx","종목코드","회사명","현재가","발행주식수","자사주", \
        "자산_2016","자산_2017","자산_2018","자산_2019","자산_2020","자산_2021","자산_2022","자산_2023", \
        "부채_2016","부채_2017","부채_2018","부채_2019","부채_2020","부채_2021","부채_2022","부채_2023", \
        "지배_2016","지배_2017","지배_2018","지배_2019","지배_2020","지배_2021","지배_2022","지배_2023", \
        "ROE_2016","ROE_2017","ROE_2018","ROE_2019","ROE_2020","ROE_2021","ROE_2022","ROE_2023", \
        "EPS_2016","EPS_2017","EPS_2018","EPS_2019","EPS_2020","EPS_2021","EPS_2022","EPS_2023", \
        "PER_2016","PER_2017","PER_2018","PER_2019","PER_2020","PER_2021","PER_2022","PER_2023", \
        "PBR_2016","PBR_2017","PBR_2018","PBR_2019","PBR_2020","PBR_2021","PBR_2022","PBR_2023", \
        "발주_2016","발주_2017","발주_2018","발주_2019","발주_2020","발주_2021","발주_2022","발주_2023"]    
    return titlelst


def delay2():
    time.sleep(random.randint(1, 2))

def delay3():
    time.sleep(random.randint(1, 3))

def delay5():
    time.sleep(random.randint(1, 5))    

if __name__ == '__main__':
    
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    
    TableTitle = TitleLst() ;
    ResultDatadf = pd.DataFrame(columns=TableTitle)  # 판다스 컬럼 초기화   
    print(len(TableTitle))
    
    (CodeNums, CompanyNames) = ReadCode() # 코스피 종목코드, 회사명        
        
    #start for    
    
    CodeNum = CodeNums[0]  
    
    url = f"http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A{CodeNum}&cID=&MenuYn=Y&ReportGB=D&NewMenuID=Y&stkGb=701"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
    
    # executable_path="/Users/ssamko/Downloads/chromedriver"
    options = webdriver.ChromeOptions()
    options.headless = True
    # 원래는 여기까지만 하면 되는데, 명시적으로 윈도우 사이즈를 알려준다.
    options.add_argument("window-size=1920x1080")
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    
    '''
    res = driver.get(url, headers=headers)    
    res.raise_for_status()
    
    if driver.sta.status_code == requests.codes.ok:
        print("정상입니다.")
    else: 
        print("문제 발생. [에러코드 : ", res.status_code, "]")
        exit()
    '''
    soup = BeautifulSoup(driver.page_source, "html.parser")
    dom = etree.HTML(str(soup))

    idx = 0 
    LenCodeNums = len(CodeNums)
    # Debug
    InputData=[]
    for idx in range(1199, LenCodeNums):      
        CodeNum = CodeNums[idx]
        elem = driver.find_element_by_id('SearchText')        
        elem.send_keys(CodeNum)        
        delay2()
        KeyTest = elem.send_keys(Keys.RETURN)
        delay3()
        
        # Enter key를 전달하고 싶다면, send_key(Keys.ENTER)라고 사용하면 된다.
        # 조금더 효과적으로 넣는 방법은 없을까???????    
        # "idx","종목코드","회사명","현재가","발행주식수","자사주", 
        InputData.append(idx) # index
        InputData.append(CodeNum) # 종목코드
        InputData.append(driver.find_element_by_xpath('//*[@id="giName"]').text)  # 회사명
        InputData.append(driver.find_element_by_xpath('//*[@id="svdMainChartTxt11"]').text) #현재가    
        InputData.append(driver.find_element_by_xpath('//*[@id="svdMainGrid1"]/table/tbody/tr[7]/td[1]').text) # 발행주식수
        
        #자사주 : 없을 때는 어떻게 하나. 막히네!!
        try:
            InputData.append(driver.find_element_by_xpath('//*[@id="svdMainGrid4"]/table/tbody/tr[3]/td[1]').text)  
        except:            
            InputData.append("0")
            
        try:
            driver.find_element_by_link_text("연간").click()    
        except:
            time.sleep(0.5)   

        # 자산  
        for j in range(1,9):
            try:
                temp = driver.find_element_by_xpath(f'//*[@id="highlight_D_Y"]/table/tbody/tr[7]/td[{j}]').text 
                InputData.append(temp)
                # print(temp)  
            except:            
                InputData.append("0")
            
        # 부채          
        for j in range(1,9):
            try:
                temp = driver.find_element_by_xpath(f'//*[@id="highlight_D_Y"]/table/tbody/tr[8]/td[{j}]').text 
                InputData.append(temp)
                # print(temp)  
            except:            
                InputData.append("0")       

        # 지배 주주 지분        
        for j in range(1,9):
            try:
                temp = driver.find_element_by_xpath(f'//*[@id="highlight_D_Y"]/table/tbody/tr[10]/td[{j}]').text 
                InputData.append(temp)
                # print(temp)  
            except:            
                InputData.append("0")
                
        # ROE        
        for j in range(1,9):
            try:
                temp = driver.find_element_by_xpath(f'//*[@id="highlight_D_Y"]/table/tbody/tr[18]/td[{j}]').text 
                InputData.append(temp)
                # print(temp)  
            except:            
                InputData.append("0")
        
        # EPS
        for j in range(1,9):
            try:
                temp = driver.find_element_by_xpath(f'//*[@id="highlight_D_Y"]/table/tbody/tr[19]/td[{j}]').text 
                InputData.append(temp)
                # print(temp)  
            except:            
                InputData.append("0")         
                
        # PER
        for j in range(1,9):
            try:
                temp = driver.find_element_by_xpath(f'//*[@id="highlight_D_Y"]/table/tbody/tr[22]/td[{j}]').text 
                InputData.append(temp)
                # print(temp)  
            except:            
                InputData.append("0")      
        
        # PBR
        for j in range(1,9):
            try:
                temp = driver.find_element_by_xpath(f'//*[@id="highlight_D_Y"]/table/tbody/tr[23]/td[{j}]').text 
                InputData.append(temp)
                # print(temp)  
            except:            
                InputData.append("0")                                     
        
        # 발행주식수
        for j in range(1,9):
            try:
                temp = driver.find_element_by_xpath(f'//*[@id="highlight_D_Y"]/table/tbody/tr[24]/td[{j}]').text 
                InputData.append(temp)
                # print(temp)  
            except:            
                InputData.append("0")                 
        
        # print(InputData )
        # print(f"길이 : {len(InputData)}")
        
        ResultDatadf = ResultDatadf.append(pd.Series(InputData, index=ResultDatadf.columns), ignore_index=True)
                
        idx += 1
        InputData.clear()       
        if idx % 100 == 0:            
            ResultDatadf.to_csv(f'Result_{idx}_{nowDate}.csv', encoding='utf-8-sig')    
    # end for idx            
    
    ResultDatadf.to_csv(f'Result_final_{nowDate}.csv', encoding='utf-8-sig')    
    print('------------- 끝났다. -------------')
    



