

import xlwings as xw
import pandas as pd

if __name__ == '__main__':
    # wb = load_workbook("fnguide_100_20210520.xlsx")
    wb = xw.Book.caller()
    df = pd.read_csv(r'd:\MyWorkspace\Python\MyStock\test.csv')
    
    print(df)
    

    # 1. 빈 데이터 채우기

    # 2. 


    print('--- 종료 ---')
    