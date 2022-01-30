from fyers_api import accessToken
from fyers_api import fyersModel
import pandas as pd
import datetime
from datetime import datetime
from datetime import timedelta
from datetime import date
import time

client_id = ""                       # Client_id here refers to APP_ID of the created app
op = 0
cl = 0

access_token = open("token.txt", "r").read()

fyers = fyersModel.FyersModel(token=access_token,is_async=False,client_id=client_id,log_path="/Users/upendrasingh/Documents/GitHub/Algorithmic-trading/AlgoTrading/")
v = fyers.get_profile()

print("V ->", v)

def read_csv():
    df = pd.read_csv("StockList.csv")
    timeConvert(df)
    
def fetchData(time_from,time_to,df):
    for row in df.iterrows():
        global name
        name=row[1][0]
        stock="NSE:"+name+"-EQ"
        print("Stock ->", stock)
        op=row[1][1]
        print("op ->", op)
        cl=row[1][2]
        print("cl ->", cl)
        cashValue=row[1][3]
        print("cashValue ->", cashValue)

        print("TIME_FROM -->", time_from)
        print("TIME_TO -->", time_to)

        data2 = fyers.get_profile()
        data1 = fyers.history(
        data = {
        "symbol" : stock,
        "resolution" : "10",
        "date_format" : "1",
        "range_from" : time_from ,
        "range_to" : time_to,
        "cont_flag" : "1"

        }
        )

        print("Output1 ->",data1)
        print("Output2 ->",data2)

def timeConvert(df):
    day = datetime.today() - timedelta(days=2)  #if you want to work on previoius day data
    # day = datetime.now()  #for current day data
    # print("now ->",previous_day)

    format_date = day.strftime("%Y-%m-%d")
    date_time = format_date
    time_from=str(date_time)
    time_to=str(date_time)

    fetchData(time_from,time_to,df)

    # tim=10 # time change time is now 10
    
    # for _ in range(42):
    #     fetchData(time_from,time_to,tim,df)
    #     time_from=str(int(time_from)+600)
    #     time_to=str(int(time_to)+600)
    #     time.sleep(1)


# data = {"symbol":"NSE:SBIN-EQ","resolution":"15","date_format":"1","range_from":"2022-01-28","range_to":"2022-01-28","cont_flag":"1"}
# print(fyers.history(data))


read_csv()