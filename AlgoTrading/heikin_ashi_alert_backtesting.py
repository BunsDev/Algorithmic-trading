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

def read_csv():
    df = pd.read_csv("StockList.csv")
    fetchData(df)
    timeConvert()
    
def fetchData(df):
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


def timeConvert():
    day = datetime.today() - timedelta(days=2)  #if you want to work on previoius day data
    # day = datetime.now()  #for current day data
    # print("now ->",previous_day)

    format_date = day.strftime("%Y-%m-%d")
    date_time = format_date + " 09:15:00"
    pattern = '%Y-%m-%d %H:%M:%S'
    time_from = int(time.mktime(time.strptime(date_time, pattern)))
    time_from=str(time_from)
    print("time_from ->", time_from)

    format_date = day.strftime("%Y-%m-%d")
    date_time = format_date + " 09:25:00"
    pattern = '%Y-%m-%d %H:%M:%S'
    time_to = int(time.mktime(time.strptime(date_time, pattern)))
    time_to=str(time_to)
    print("time_to ->", time_to)


# data = {"symbol":"NSE:SBIN-EQ","resolution":"15","date_format":"1","range_from":"2022-01-28","range_to":"2022-01-28","cont_flag":"1"}
# print(fyers.history(data))


read_csv()