from fastapi import FastAPI
from pydantic import  BaseModel

app = FastAPI()

class ITEM(BaseModel):
    name:str
    price:float
    tax:float|None=None
    description:float|None=None
    
class USER(BaseModel):
    username:str
    fullname:str|None
    
@app.put("/items/{item_id}")

async def update(item_id:int, item:ITEM, user:USER):
    results={"item_id":item_id,"item":item,"user":user}
    return results