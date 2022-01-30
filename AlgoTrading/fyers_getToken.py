from urllib import response
from fyers_api import fyersModel
from fyers_api import accessToken

redirect_uri= "https://www.google.co.in/"          # redircet_uri you entered while creating APP.
client_id = ""                       # Client_id here refers to APP_ID of the created app
secret_key = ""                          # app_secret key which you got after creating the app 
grant_type = "authorization_code"                  # The grant_type always has to be "authorization_code"
response_type = "code"                             # The response_type always has to be "code"
state = "sample"                                   #  The state field here acts as a session manager. you will be sent with the state field after successfull generation of auth_code 

session=accessToken.SessionModel(client_id=client_id,secret_key=secret_key,redirect_uri=redirect_uri,response_type=response_type, grant_type=grant_type,state=state)

# After succesfull login the user can copy the generated auth_code over here and make the request to generate the accessToken 
auth_code = open("AuthCode.txt", "r").read()
session.set_token(auth_code)
response = session.generate_token()

# There can be two cases over here you can successfully get the acccessToken over the request or you might get some error over here. so to avoid that have this in try except block
try: 
    access_token = response["access_token"]
    print("token: ", access_token)
except Exception as e:
    print(e,response)  ## This will help you in debugging then and there itself like what was the error and also you would be able to see the value you got in response variable. instead of getting key_error for unsuccessfull response.

bn = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NDM1NTc3NzAsImV4cCI6MTY0MzU4OTAzMCwibmJmIjoxNjQzNTU3NzcwLCJhdWQiOlsiZDoxIiwiZDoyIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaDlyT0s4TkRGbjBLdlVKQ2ZJTXc1ekZheFF3aDhKLVk2YmM1NkZNTUFROEswMXoxSmxlOTUtS1lnNzRzbXhzaF9kZ1ZoQUhwa1FvWUxhSk5JYkJUZEtsS0RFcHk1c3B2bTRhcGhDMDhoZFVTTVc3WT0iLCJkaXNwbGF5X25hbWUiOiJVUEVORFJBIFNJTkdIIiwiZnlfaWQiOiJYVTAwMDMxIiwiYXBwVHlwZSI6MTAwLCJwb2FfZmxhZyI6Ik4ifQ.krq2YDfYdbVE3L2TaqamSMnAFGZ6OCL9AVfz1E28M5E"
fyers = fyersModel.FyersModel(token=access_token,is_async=False,client_id=client_id,log_path="/Users/upendrasingh/Documents/GitHub/Algorithmic-trading/AlgoTrading/")
print(fyers)

# data = {"symbol":"NSE:SBIN-EQ","resolution":"D","date_format":"0","range_from":"1622097600","range_to":"1622097685","cont_flag":"1"}

# print(fyers.history(data))

data = {"symbol":"NSE:SBIN-EQ","resolution":"15","date_format":"1","range_from":"2022-01-28","range_to":"2022-01-28","cont_flag":"1"}
print(fyers.history(data))