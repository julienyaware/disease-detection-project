from fastapi import FastAPI, File , UploadFile
import uvicorn
import numpy as npj

app = FastAPI()
@app.get("/ping")
async def ping():
    return "Hello"

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    bytes = await file.read()
    return


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)