from fastapi import FastAPI
from pydantic import  BaseModel,Field,HttpUrl

app = FastAPI()
class IMAGE(BaseModel):
    url:HttpUrl
    name:str
    
class ITEM(BaseModel):
    name:str=Field(examples="SAVITHA")
    price:float=Field(examples="20.7")
    tax:float|None=None,Field(exaples="10.0")
    description:float|None= Field(default=None,title="description",max_length=50,examples="hey here")
    tag:list[str]=[]
    image:list[IMAGE]|None=None
class USER(BaseModel):
    username:str
    fullname:str|None
    
@app.put("/items/{item_id}")

async def update(item_id:int, item:ITEM, user:USER):
    results={"item_id":item_id,"item":item,"user":user}
    return results