

import xlwings as xw
from xlwings import Range, constants
import math 

import pandas as pd
import numpy as np

if __name__ == '__main__':
    '''  
    # wb = load_workbook("fnguide_100_20210520.xlsx")
    # wb = xw.Book.caller()
    wb = xw.Book(r'd:\MyWorkspace\Python\MyStock\test.xlsx')
    sht1 =  xw.sheets[0]
    sht = xw.sheets.active
    #df = pd.read_csv(r'd:\MyWorkspace\Python\MyStock\test.csv') '''
    
    # wb = xw.Book()  # this will create a new workbook
    # wb = xw.Book('FileName.xlsx')  # connect to a file that is open or in the current working directory
    # wb = xw.Book(r'C:\path\to\file.xlsx')  # on Windows: use raw strings to escape backslashes
    wb = xw.Book(r'd:\MyWorkspace\Python\MyStock\test.xlsx')
    # sht = wb.sheets['Sheet1']
    
    # rows = wb.sheets[0].range('A' + str(wb.sheets[0].cells.last_cell.row)s).end('up').row
    # print(rows)
    
    df = pd.read_excel(r'd:\MyWorkspace\Python\MyStock\test.xlsx')
    df['총점']  = df['영어'] + df['수학']
    # xw.view(df)
    
    sht = wb.sheets['sheet2']
    # sht["A1"].options(pd.DataFrame, header=1, index=True, expand='table').value = df
    sht.range('A1')
    
    
    # print(df)
    

    # 1. 빈 데이터 채우기

    # 2. 


    print('--- 종료 ---')
    