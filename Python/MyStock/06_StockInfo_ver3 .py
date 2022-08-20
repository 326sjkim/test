
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
    
    KospiFile = "kospi.xlsx"  # 종목 확인
    ReadCodeNum = pd.read_excel(KospiFile, sheet_name="kospi",engine='openpyxl', dtype={"종목코드": str})
    CodeNums = ReadCodeNum["종목코드"].tolist()
    CompanyNames = ReadCodeNum["회사명"].tolist()

    KospiFile = 'kosdaq.xlsx'  # 종목 확인
    ReadCodeNum = pd.read_excel(KospiFile, sheet_name="kosdaq",engine='openpyxl', dtype={"종목코드": str})
    CodeNums.extend(ReadCodeNum["종목코드"].tolist())
    CompanyNames.extend(ReadCodeNum["회사명"].tolist())

    return CodeNums, CompanyNames

def TitleLst():
    titlelst = ["idx","종목코드","회사명","현재가","발행주식수","자사주", \
        "매출_16","매출_17","매출_18","매출_19","매출_20","매출_21","매출_22","매출_23", \
        "영이_16","영이_17","영이_18","영이_19","영이_20","영이_21","영이_22","영이_23", \
        "당순_16","당순_17","당순_18","당순_19","당순_20","당순_21","당순_22","당순_23", \
        "자산_16","자산_17","자산_18","자산_19","자산_20","자산_21","자산_22","자산_23", \
        "부채_16","부채_17","부채_18","부채_19","부채_20","부채_21","부채_22","부채_23", \
        "자본_16","자본_17","자본_18","자본_19","자본_20","자본_21","자본_22","자본_23", \
        "지배_16","지배_17","지배_18","지배_19","지배_20","지배_21","지배_22","지배_23", \
        "자본금_16","자본금_17","자본금_18","자본금_19","자본금_20","자본금_21","자본금_22","자본금_23", \
        "ROA_16","ROA_17","ROA_18","ROA_19","ROA_20","ROA_21","ROA_22","ROA_23", \
        "ROE_16","ROE_17","ROE_18","ROE_19","ROE_20","ROE_21","ROE_22","ROE_23", \
        "EPS_16","EPS_17","EPS_18","EPS_19","EPS_20","EPS_21","EPS_22","EPS_23", \
        "PER_16","PER_17","PER_18","PER_19","PER_20","PER_21","PER_22","PER_23", \
        "PBR_16","PBR_17","PBR_18","PBR_19","PBR_20","PBR_21","PBR_22","PBR_23", \
        "발주_16","발주_17","발주_18","발주_19","발주_20","발주_21","발주_22","발주_23"]
    
    return titlelst


def delay(sec):
    time.sleep(random.randint(1, sec))

if __name__ == '__main__':
    
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    
    TableTitle = TitleLst() ;
    ResultDatadf = pd.DataFrame(columns=TableTitle)  # 판다스 컬럼 초기화   
    print(len(TableTitle))
    
    (CodeNums, CompanyNames) = ReadCode() # 코스피 종목코드, 회사명        
        
    #start for    
    
    LenCodeNums = len(CodeNums)
    # Debug
    InputData=[]
    
    # Debug
    # start_idx = 0 ; end_idx = 15    
    # for idx in range(start_idx, end_idx):  
    
    idx=0     
    for idx in range(idx, LenCodeNums):      
        CodeNum = CodeNums[idx]
        CompanyName = CompanyNames[idx]
        
        headers = "User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
        url = f"http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A{CodeNum}&cID=&MenuYn=Y&ReportGB=D&NewMenuID=Y&stkGb=701"
        
        # executable_path="/Users/ssamko/Downloads/chromedriver"
        options = webdriver.ChromeOptions()
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.headless = True
        # 원래는 여기까지만 하면 되는데, 명시적으로 윈도우 사이즈를 알려준다.
        options.add_argument("window-size=1920x1080")
        options.add_argument(headers)
        driver = webdriver.Chrome(options=options)
        
        # 막힐때.
        """ 
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options)
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        """
        
        #driver = webdriver.Chrome()
        # driver.maximize_window()    
        driver.get(url)
        
        delay(2)
        try:
            driver.find_element_by_link_text("연결").click()    
        except:
            delay(1)
        
        delay(1)    
        try:
            driver.find_element_by_link_text("연간").click()    
        except:
            delay(1)
                
        delay(3)        
        soup = BeautifulSoup(driver.page_source, "lxml")
        dom = etree.HTML(str(soup))  
                        
        # Enter key를 전달하고 싶다면, send_key(Keys.ENTER)라고 사용하면 된다.
        # 조금더 효과적으로 넣는 방법은 없을까???????    
        # "idx","종목코드","회사명","현재가","발행주식수","자사주", 
        InputData.append(idx) # index
        InputData.append(CodeNum) # 종목코드
        InputData.append(CompanyName)  # 회사명
        InputData.append(driver.find_element_by_xpath('//*[@id="svdMainGrid1"]/table/tbody/tr[1]/td[1]').text)        
        # //*[@id="svdMainGrid1"]/table/tbody/tr[1]/td[1]/text()
        InputData.append(driver.find_element_by_xpath('//*[@id="svdMainGrid1"]/table/tbody/tr[7]/td[1]').text) # 발행주식수
        # //*[@id="svdMainGrid1"]/table/tbody/tr[7]/td[1]
        
        #자사주 : 없을 때는 어떻게 하나?
        try:
            InputData.append(driver.find_element_by_xpath('//*[@id="svdMainGrid4"]/table/tbody/tr[3]/td[1]').text)  
        except:            
            InputData.append("0")
            
        try:
            driver.find_element_by_link_text("연간").click()    
        except:
            delay(2)
        
        #매출액(매출)  # //*[@id="highlight_D_Y"]/table/tbody/tr[1]/td[1]
        for j in range(1,9):
            try:
                temp = driver.find_element_by_xpath(f'//*[@id="highlight_D_Y"]/table/tbody/tr[1]/td[{j}]').text 
                InputData.append(temp)
                # print(temp)  
            except:            
                InputData.append("0")
        
        #영업이익(영이)  //*[@id="highlight_D_Y"]/table/tbody/tr[2]/td[8]
        for j in range(1,9):
            try:
                temp = driver.find_element_by_xpath(f'//*[@id="highlight_D_Y"]/table/tbody/tr[2]/td[{j}]').text 
                InputData.append(temp)
                # print(temp)  
            except:            
                InputData.append("0")
                
        # 당기순이익(당순)  //*[@id="highlight_D_Y"]/table/tbody/tr[4]/td[8]              
        for j in range(1,9):
            try:
                temp = driver.find_element_by_xpath(f'//*[@id="highlight_D_Y"]/table/tbody/tr[4]/td[{j}]').text 
                InputData.append(temp)
                # print(temp)  
            except:            
                InputData.append("0")                
            
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
        # 자본  //*[@id="highlight_D_Y"]/table/tbody/tr[9]/td[1]        
        for j in range(1,9):
            try:
                temp = driver.find_element_by_xpath(f'//*[@id="highlight_D_Y"]/table/tbody/tr[9]/td[{j}]').text 
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
                
        # 자본금 //*[@id="highlight_D_Y"]/table/tbody/tr[12]/td[1]                
        for j in range(1,9):
            try:
                temp = driver.find_element_by_xpath(f'//*[@id="highlight_D_Y"]/table/tbody/tr[12]/td[{j}]').text 
                InputData.append(temp)
                # print(temp)  
            except:            
                InputData.append("0")
                    
        # ROA //*[@id="highlight_D_Y"]/table/tbody/tr[17]/td[1]       
        for j in range(1,9):
            try:
                temp = driver.find_element_by_xpath(f'//*[@id="highlight_D_Y"]/table/tbody/tr[17]/td[{j}]').text 
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
            ResultDatadf.to_csv(f'Stock_{idx}_{nowDate}.csv', encoding='utf-8-sig')    
            delay(10)
            print(f'{idx}')
    # end for idx            
    
    ResultDatadf.to_csv(f'Stock_final_{nowDate}.csv', encoding='utf-8-sig')    
    print('------------- 끝났다. -------------')
    



