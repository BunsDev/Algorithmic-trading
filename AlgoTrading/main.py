# main.py

from fastapi import FastAPI
from fastapi import Response
from nsepy import get_history
from datetime import date
import numpy as np
import pandas as pd
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()


BankNiftyCE = {
    "stikeprice": {
        "8200",
        "8300",
        "8400",
        "8500"
    },
    "price": {
        "222",
        "432",
        "567",
        "111"
    }
}

BankNiftyPE = {
    "stikeprice": {
        "8200",
        "8300",
        "8400",
        "8500"
    },
    "price": {
        "212",
        "462",
        "527",
        "11"
    }
}


@app.get("/")
async def root():
    sbin = get_history(symbol='SBIN',
                   start=date(2015,1,1),
                   end=date(2015,1,10))
    print(type(sbin))

    dfToJson = sbin.to_json()
    print(dfToJson)

    return Response(content=dfToJson, media_type="application/json")


@app.get("/nifty-opt-ce")
async def root():
    json_compatible_item_data = jsonable_encoder(BankNiftyCE)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/nifty-opt-pe")
async def root():
    json_compatible_item_data = jsonable_encoder(BankNiftyPE)
    return JSONResponse(content=json_compatible_item_data)