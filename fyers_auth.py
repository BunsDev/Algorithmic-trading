from urllib import response
from fyers_api import fyersModel
from fyers_api import accessToken
import requests

redirect_uri= "https://www.google.co.in/"  ## redircet_uri you entered while creating APP.
app_id = ""                                          ## Client_id here refers to APP_ID of the created app
key = ""                                           ## app_secret key which you got after creating the app 
grant_type = "authorization_code"                  ## The grant_type always has to be "authorization_code"
response_type = "code"                             ## The response_type always has to be "code"
state = "sample"                                   ##  The state field here acts as a session manager. you will be sent with the state field after successfull generation of auth_code 

auth_code = "https://api.fyers.in/api/v2/generate-authcode?client_id="+ app_id +"&redirect_uri="+ redirect_uri +"&response_type=code&state=sample_state"
# response = requests.get(auth_code)
# print("Auth Code ->", auth_code)
# print("Response ->", response)

code = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NDM1NDM2MzYsImV4cCI6MTY0MzU3MzYzNiwibmJmIjoxNjQzNTQzMDM2LCJhdWQiOiJbXCJkOjFcIiwgXCJkOjJcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYVTAwMDMxIiwibm9uY2UiOiIiLCJhcHBfaWQiOiJWSFBDMURDSE5OIiwidXVpZCI6IjY0ZDAyOTdlNzAzMDQ1NTY5ODdlNzczZjRmY2EzNDdiIiwiaXBBZGRyIjoiMC4wLjAuMCIsInNjb3BlIjoiIn0.9dddAhezGkHhTXqqJRdO2iH3-VH2xKNX-1zPZ26baFI"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NDM1NDQ4ODEsImV4cCI6MTY0MzU4OTA0MSwibmJmIjoxNjQzNTQ0ODgxLCJhdWQiOlsiZDoxIiwiZDoyIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaDlvRXhXb1hYNzVhcWdqQUJuT09TUFRERDBqbTlDNEFRcTZ3VVUtbUZTbVVPOGFqRWtpQnd2c1BqYldpeXBnZXhxRkhzblhoZnN3N3RnZ1hFcXV0NlFybmFLTjNVTVloZEtqM3NIYlNCVnVqYkhUQT0iLCJkaXNwbGF5X25hbWUiOiJVUEVORFJBIFNJTkdIIiwiZnlfaWQiOiJYVTAwMDMxIiwiYXBwVHlwZSI6MTAwLCJwb2FfZmxhZyI6Ik4ifQ.QED9R_G5s0g-IOgR3NOvQX2kUJNfGJO1k-As4QtK26Q"
# https://api.fyers.in/api/v2/generate-authcode?client_id=VHPC1DCHNN-100&redirect_uri=https://www.google.co.in/&response_type=code&state=sample_state
fyers.get_profile()



