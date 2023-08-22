from fastapi import FastAPI
from pydantic import  BaseModel,Field,HttpUrl

app = FastAPI()
class IMAGE(BaseModel):
    url:HttpUrl
    name:str
    
class ITEM(BaseModel):
    name:str
    price:float
    tax:float|None=None
    description:float|None= Field(default=None,title="description",max_length=50)
    tag:list[str]=[]
    image:list[IMAGE]|None=None
class USER(BaseModel):
    username:str
    fullname:str|None
    
@app.put("/items/{item_id}")

async def update(item_id:int, item:ITEM, user:USER):
    results={"item_id":item_id,"item":item,"user":user}
    return results
