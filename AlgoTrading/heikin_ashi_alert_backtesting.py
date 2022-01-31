import pandas as pd

def read_files(path1, path2):
    df_StockList = pd.read_csv("StockList.csv")
    df_stock_data_save = pd.read_csv("stock_data_save.csv")
    Heikin_Ashi(df_StockList, df_stock_data_save)
    


def Heikin_Ashi(df_StockList, df_stock_data_save):


   
    ################## Heikin Ashi Close Candle ##########################
    # HA_Close = (df_stock_data_save['Open']+ df_stock_data_save['High']+ df_stock_data_save['Low']+df_stock_data_save['Close'])/4.0
    # ha_cl1 = round(HA_Close/ 0.05) * 0.05
    # df_stock_data_save['HA_Close'] = round(ha_cl1, 2)
    # print("Close ->", df_stock_data_save['HA_Close'])


    ################## Heikin Ashi Open Candle ##########################
    # Open_Previous_Value = df_StockList["HA_Open"]
    # print(len(Stock_Name))

    # for i in range(0, len(df_StockList)):
    #     if i <= len(Open_Previous_Value):
    #         print(Open_Previous_Value)

    # i = len(Open_Previous_Value)

    # while i <= len(Open_Previous_Value):
    #     i += 1
    #     open = Open_Previous_Value
    #     print(open)

    # Close_Previous_Value = df_StockList["HA_Close"]
    # # print(len(Stock_Name))
    # i = len(Close_Previous_Value)
    # while i <= len(Close_Previous_Value):
    #     i += 1
    #     close = Close_Previous_Value
    #     print(close)
    



read_csv()
