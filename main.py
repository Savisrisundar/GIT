from fastapi import FastAPI, Depends, Header, HTTPException
from typing import Annotated

app= FastAPI()

async def verifytoken(xt: Annotated[str,Header()]):
    if xt !="fake":
        raise HTTPException(status_code=404,detail="invalid sry!!")
    
async def verifykey(xk:Annotated[str,Header()]):
    if xk!="fake":
        raise HTTPException(status_code=401,detail="invalid")
    return xk

@app.get("/items/",dependencies=[Depends(verifytoken),Depends(verifykey)])
async def read():
    return {"foo":"item"}