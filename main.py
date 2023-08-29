from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse

app= FastAPI()

@app.get("/items/",response_model=None)
async def getitems(teleport:bool=False)->Response|dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        return JSONResponse(content={"message": "Here's your interdimensional portal."})