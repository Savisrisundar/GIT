from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

app=FastAPI()
OAuth2=OAuth2PasswordBearer(tokenUrl="token")

@app.get("/items/")
async def read(token:Annotated[str,Depends(OAuth2)]):
    return {"token":token}

