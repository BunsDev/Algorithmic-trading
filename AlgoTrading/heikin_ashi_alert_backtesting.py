from asyncore import read
import pandas as pd

def read_csv():
    df = pd.read_csv("stock_data_save.csv")
    heikin_ashi(df)
    

def heikin_ashi(df):
    HA_Close = (df['Open']+ df['High']+ df['Low']+df['Close'])/4.0
    ha_cl1 = round(HA_Close/ 0.05) * 0.05
    df['HA_Close'] = round(ha_cl1, 2)
    print("Close ->", df['HA_Close'])


read_csv()
