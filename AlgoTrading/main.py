# main.py

from fastapi import FastAPI
from fastapi import Response
from nsepy import get_history
from datetime import date
import numpy as np
import pandas as pd
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector


app = FastAPI()

# MySQL Configuration
# config = {
#     'user': 'u683660902_algo',
#     'password': 'Vodafone1!',
#     'host': 'sql362.main-hosting.eu',
#     'database': 'u683660902_algo'
# }

# Establishing a connection to the MySQL database
mydb = mysql.connector.connect(
  host="sql362.main-hosting.eu",
  user="u683660902_algo",
  password="Vodafone1!",
  database="u683660902_algo"
)


# MySQL Connection Pool
# cnx_pool = mysql.connector.pooling.MySQLConnectionPool(pool_size=5, pool_name='my_pool', **config)
# print("cnx_pool ->", cnx_pool)

origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/nifty-opt-ce")
async def root():
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM BankNiftyCall")
    data = mycursor.fetchall()
    mycursor.close()
    columns = [desc[0] for desc in mycursor.description]
    return {"columns": columns, "data": data}

@app.get("/nifty-opt-pe")
async def root():
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM BankNiftyPut")
    data = mycursor.fetchall()
    mycursor.close()
    columns = [desc[0] for desc in mycursor.description]
    return {"columns": columns, "data": data}