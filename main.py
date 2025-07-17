from fastapi import FastAPI, File, UploadFile
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from MediScan!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    file_location = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "message": "File received successfully"}
