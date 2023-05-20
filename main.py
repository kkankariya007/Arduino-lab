from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
   
app = FastAPI()
   
@app.get("/")
async def root():
    return {"He":"Uds"}

@app.get("/2")
async def des():
    file_p="./e2.pdf"
    return FileResponse(file_p)

@app.get("/3")
async def des():
    file_p="./e3.pdf"
    return FileResponse(file_p)

@app.get("/4")
async def des():
    file_p="./e4.pdf"
    return FileResponse(file_p)

@app.get("/5")
async def des():
    file_p="./e5.pdf"
    return FileResponse(file_p)

@app.get("/6")
async def des():
    file_p="./e6.pdf"
    return FileResponse(file_p)

@app.get("/7")
async def des():
    file_p="./e7.pdf"
    return FileResponse(file_p)

@app.get("/8")
async def des():
    file_p="./e8.pdf"
    return FileResponse(file_p)

@app.get("/9")
async def des():
    file_p="./e9.pdf"
    return FileResponse(file_p)

@app.get("/10")
async def des():
    file_p="./e10.pdf"
    return FileResponse(file_p)

@app.get("/11")
async def des():
    file_p="./e11.pdf"
    return FileResponse(file_p)

@app.get("/12")
async def des():
    file_p="./e12.pdf"
    return FileResponse(file_p)