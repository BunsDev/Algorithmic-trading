from fyers_api.Websocket import ws

def run_process_foreground_symbol_data(access_token):
    '''This function is used for running the symbolData in foreground 
    1. log_path here is configurable this specifies where the output will be stored for you
    2. data_type == symbolData this specfies while using this function you will be able to connect to symbolwebsocket to get the symbolData
    3. run_background = False specifies that the process will be running in foreground'''
    data_type = "symbolData"
    # symbol = ["NSE:SBIN-EQ","NSE:ONGC-EQ"]   ##NSE,BSE sample symbols
    symbol =["NSE:SBIN-EQ"]
    # symbol =["MCX:SILVERMIC21NOVFUT","MCX:GOLDPETAL21SEPTFUT"]
    fs = ws.FyersSocket(access_token=access_token,run_background=False,log_path="/Users/upendrasingh/Documents/GitHub/Algorithmic-trading/AlgoTrading/")
    fs.websocket_data = custom_message
    fs.subscribe(symbol=symbol,data_type=data_type)
    fs.keep_running()

def custom_message(msg):
    print (f"Custom:{msg}") 


def main():
    ### Insert the accessToken and app_id over here in the following format (APP_ID:access_token) 
    access_token= "V******NN-100:***********.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2ND********TAzMCwibmJmIjoxNjQzNTU3NzcwLCJhdWQ*********MDMxIiwiYXBwVHlwZSI6MTAwLCJwb2FfZmxhZyI6Ik4ifQ.krq2YDfYd******E"

    ## run a specific process you need to connect to get the updates on
    run_process_foreground_symbol_data(access_token)
    # run_process_foreground_order_update(access_token)
    
if __name__ == '__main__':
	main()
