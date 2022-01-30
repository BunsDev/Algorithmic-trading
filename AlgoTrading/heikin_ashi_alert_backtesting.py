from fyers_api import accessToken
from fyers_api import fyersModel

client_id = ""                       # Client_id here refers to APP_ID of the created app


access_token = open("token.txt", "r").read()

fyers = fyersModel.FyersModel(token=access_token,is_async=False,client_id=client_id,log_path="/Users/upendrasingh/Documents/GitHub/Algorithmic-trading/AlgoTrading/")


data = {"symbol":"NSE:SBIN-EQ","resolution":"15","date_format":"1","range_from":"2022-01-28","range_to":"2022-01-28","cont_flag":"1"}
print(fyers.history(data))