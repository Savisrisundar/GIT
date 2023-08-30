from fastapi import FastAPI, HTTPException

app=FastAPI()
items={"item 1": "Number 1","item 2": "Number 2"}

@app.get("/items/{item_id}")
async def read(item_id:str):
    if item_id not in items:
        return HTTPException(status_code=400,detail="item not found")
    return {"item":items[item_id]}