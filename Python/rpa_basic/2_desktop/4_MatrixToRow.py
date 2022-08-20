
import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel(r'.\stockdata\kind_20210520.xlsx', sheet_name='k20210520')
    
    print(len(df.columns))
    
    print(len(df.columns[0]))
    
    
    
    