from fastapi import FastAPI
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fakedb={}

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None
    
    
app=FastAPI()
@app.put("/items/{id}")
async def read(id:str,item:Item):
    jsoncom=jsonable_encoder(item)
    fakedb[id]=jsoncom
    return fakedb