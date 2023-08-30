from fastapi import FastAPI, File, UploadFile, Form
from typing import Annotated

app=FastAPI()
@app.post("/files/")
async def read(files:Annotated[bytes,File()],
               token:Annotated[str, Form()],
               filesb:UploadFile):
    return {"file":files,"token":token,"file content":filesb.content_type}

