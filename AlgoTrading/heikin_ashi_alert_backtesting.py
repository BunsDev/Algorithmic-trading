from asyncore import read
import pandas as pd

def read_csv():
    df_StockList = pd.read_csv("StockList.csv")
    Heikin_Ashi(df_StockList)
    

def Heikin_Ashi(df_StockList):
    df_stock_data_save = pd.read_csv("stock_data_save.csv")
    
    
    ################## Heikin Ashi Close Candle ##########################
    HA_Close = (df_stock_data_save['Open']+ df_stock_data_save['High']+ df_stock_data_save['Low']+df_stock_data_save['Close'])/4.0
    ha_cl1 = round(HA_Close/ 0.05) * 0.05
    df_stock_data_save['HA_Close'] = round(ha_cl1, 2)
    # print("Close ->", df_stock_data_save['HA_Close'])


    ################## Heikin Ashi Open Candle ##########################
    Stock_Name = list(df_StockList["Name"])
    print(type(Stock_Name))    



read_csv()
