from fastapi import FastAPI
import uvicorn 

app=FastAPI()

@app.get("/")

def root_fun():
    return "hello world"