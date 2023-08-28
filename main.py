from fastapi import FastAPI, Body
from datetime import datetime, time, timedelta
from uuid import UUID
from typing import Annotated
from pydantic import BaseModel
app = FastAPI()

class Items(BaseModel):
    name:str
    description: str|None=None
    price:float
    tax:float
    tags:list[str]=[]
    
@app.post("/items/")
async def create_item(item:Items)->Items:
    return item

@app.put("/items/{item_id}")
async def read_items(
    item_id:UUID,
    start_date_time:Annotated[datetime|None, Body()]=None,
    end_time:Annotated[time|None,Body()]=None,
    q: str | None = None):
    return {"item_id": item_id,
        "start_datetime": start_date_time,
        "end_datetime": end_time}

@app.get("/items/")
async def read_items(q: Annotated[str | None , Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
