# main.py

from fastapi import FastAPI
from fastapi import Response
from nsepy import get_history
from datetime import date
import numpy as np
import pandas as pd

app = FastAPI()

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
    nifty_opt = get_history(symbol="NIFTY",
                            start=date(2015,1,1),
                            end=date(2015,1,10),
                            index=True,
                            option_type='CE',
                            strike_price=8200,
                            expiry_date=date(2015,1,29))
    print(nifty_opt)

    nifty_df_to_json = nifty_opt.to_json()
    print(nifty_df_to_json)
    return Response(content=nifty_df_to_json, media_type="application/json")

@app.get("/nifty-opt-pe")
async def root():
    nifty_opt_pe = get_history(symbol="NIFTY",
                            start=date(2015,1,1),
                            end=date(2015,1,10),
                            index=True,
                            option_type='PE',
                            strike_price=8200,
                            expiry_date=date(2015,1,29))
    print(nifty_opt_pe)

    nifty_pe_df_to_json = nifty_opt_pe.to_json()
    print(nifty_pe_df_to_json)
    return Response(content=nifty_pe_df_to_json, media_type="application/json")