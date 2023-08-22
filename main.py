from fastapi import FastAPI, Body
from datetime import datetime, time, timedelta
from uuid import UUID
from typing import Annotated
app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
    item_id:UUID,
    start_date_time:Annotated[datetime|None, Body()]=None,
    end_time:Annotated[time|None,Body()]=None,
    q: str | None = None):
    return {"item_id": item_id,
        "start_datetime": start_date_time,
        "end_datetime": end_time}

