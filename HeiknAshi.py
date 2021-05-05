import pandas as pd

def fileread():
    try:
        excel_file = 'ACC30JAN201440.csv' #file present in same directory so its realtive path
        
    except IOError:
        print("ACC30JAN201440.csv' file does not exist")
    df = pd.read_excel(excel_file)

    print(df)

fileread()