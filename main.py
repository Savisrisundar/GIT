from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Items(BaseModel):
    name:str
    description: str|None=None
    price:float
    tax:float
    tags:list[str]=[]
    
@app.post("/items/")
async def create_item(item:Items)->Items:
    return item

@app.get("/items/")
async def read_item()->list[Items]:
    return [Items(name="tom",price=50.5)]
    