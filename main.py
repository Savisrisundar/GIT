from fastapi import FastAPI, Query
from typing import Annotated
app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str, Query(max_length=50)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
