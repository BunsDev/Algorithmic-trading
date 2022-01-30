# from fyers_api import fyersModel
# from fyers_api import accessToken
# import webbrowser

# redirect_uri= "https://www.google.co.in/"  ## redircet_uri you entered while creating APP.
# id = "VHPC1DCHNN-100"                                          ## Client_id here refers to APP_ID of the created app
# secret_key = "GSURDCM63E"                                           ## app_secret key which you got after creating the app 
# grant_type = "authorization_code"                  ## The grant_type always has to be "authorization_code"
# response_type = "code"                             ## The response_type always has to be "code"
# state = "sample"                                   ##  The state field here acts as a session manager. you will be sent with the state field after successfull generation of auth_code 


# ### Connect to the sessionModel object here with the required input parameters
# appSession = accessToken.SessionModel(id = id, redirect_uri = redirect_uri,response_type=response_type,state=state,secret_key=secret_key,grant_type=grant_type)

# ### Make  a request to generate_authcode object this will return a login url which you need to open in your browser from where you can get the generated auth_code 
# generateTokenUrl = appSession.generate_authcode()

# """There are two method to get the Login url if  you are not automating the login flow
# 1. Just by printing the variable name 
# 2. There is a library named as webbrowser which will then open the url for you without the hasel of copy pasting
# both the methods are mentioned below"""
# print((generateTokenUrl))  
# webbrowser.open(generateTokenUrl,new=1)


moduleName = "getAccessToken"
"""
    1.We need to first install fyers-apiv2(can be installed as 'pip install fyers-apiv2)
    2.We then need to import accesToken module from fyers_api directory(as done below)
    3.We also need to import webbrowser to preform an action while generating authcode
"""
from fyers_api import accessToken

import webbrowser




def getauthToken(appId, redirect_uri):
    functionName = "getauthToken"
    """
        :param app_id: "XXXXXXXXXXX"
        :param redirect_url: "https://XXXXXX.com"
		 1. This function open this url in the browser.
		 2. This will ask you to login and will ask you to approve the app if it is not approved already.
		 3. Once that is done, it will redirect to a url (added while app creation) with the auth_code. The url will look like
		    https://www.google.com/?auth_code=eyJ0eXAiOiXXXXXGciOiJIUzI1NiJ9.eyXXXXXXXXXXXXXInN1YiI6ImF1dGhDb2XXXXXXXXXXXXXXXXXX2lkIjoiQjhQV0xWSDhUNiIsImlzcyI6ImFwaS5sb2dpbi5meWVycy5pbiIsImF1ZCI6WyJ4OjAiLCJ4OjEiLCJ4OjIiXSwidXVpZCI6ImZhOGNhYjE3ZWU4OTQzMGRhZjA1YWUxNDI2YWVkYzI4IiwiaXBBZGRyIjoiMjIzLjIzMy40Mi40NiIsImRpc3BsYXlfbmFtZSI6IkRQMDA0MDQiLCJpYXQiOjE1OTM1ODYzNzEsIm5iZiI6MTU5MzU4NjM3MX0.IMJHzQGHQgyXt_XN0AgDrMN1keR4qolFFKO6cyXTnTg&user_id=DP00404
		 4. You have to take the auth_code from the url and use that token in your generate_access_token function.
	"""
    response_type="code"
    grant_type="authorization_code"
    # creating an instance appSession to generate the auth code by passing app id and redirect url as parameter
    appSession = accessToken.SessionModel(id=id,redirect_uri=redirect_uri,response_type=response_type, grant_type=grant_type,state="state",scope="",nonce="")
    print("app ->", appSession)
    # The variable `generateTokenUrl` will have a url like https://uat-api.fyers.in/api/dev/generate-authcode?appId=B8PXXXH8T6&redirectUrl=https%3A%2F%2Fgoogle.com
    generateTokenUrl = appSession.generate_authcode()
    print("url->", generateTokenUrl)

    # This command is used to open the url in default system brower
    webbrowser.open(generateTokenUrl, new=1)

    return generateTokenUrl

id = "VHPC1DCHNN-100"
redirect_uri = "https://www.google.co.in/"

print(getauthToken(id, redirect_uri))
