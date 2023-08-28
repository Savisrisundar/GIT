from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl

app = FastAPI()
class IMAGE(BaseModel):
    url:HttpUrl
    name:str
    



class Items(BaseModel):
    name:str
    description: str|None=None
    price:float
    tax:float
    tags:list[str]=[]
    
@app.put("/items/{item_id}")

async def update(item_id:int, item:Items):
    results={"item_id":item_id,"item":item}
    return results
