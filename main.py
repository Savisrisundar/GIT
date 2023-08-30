from fastapi import FastAPI, File, UploadFile
from typing import Annotated

app=FastAPI()
@app.post("/files/")
async def read(files:Annotated[bytes,File()]):
    return {"file":files}
@app.post("/upload/")
async def upload(files:UploadFile):
    return {"file name":files.filename}
