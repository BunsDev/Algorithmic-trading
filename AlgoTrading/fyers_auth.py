from urllib import response
from fyers_api import fyersModel
from fyers_api import accessToken

import webbrowser

redirect_uri= ""          # redircet_uri you entered while creating APP.
client_id = ""                       # Client_id here refers to APP_ID of the created app
secret_key = ""                          # app_secret key which you got after creating the app 
grant_type = "authorization_code"                  # The grant_type always has to be "authorization_code"
response_type = "code"                             # The response_type always has to be "code"
state = "sample"                                   #  The state field here acts as a session manager. you will be sent with the state field after successfull generation of auth_code 

session=accessToken.SessionModel(client_id=client_id,secret_key=secret_key,redirect_uri=redirect_uri,response_type=response_type, grant_type=grant_type,state=state)

response = session.generate_authcode()
webbrowser.open(response,new=1)






