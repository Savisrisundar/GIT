from fastapi import FastAPI,Path
from typing import Annotated


app = FastAPI()


@app.get("/items/")
async def read_items(q: str, item_id: Annotated[int,Path(title="get the string", gt=1,le=100)]):
    results = {"items":item_id}
    if q:
        results.update({"q": q})
    return results
