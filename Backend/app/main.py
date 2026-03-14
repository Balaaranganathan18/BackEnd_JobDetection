from fastapi import FastAPI
from app.routes import predict

app = FastAPI(title="Fake Job Detection API")

app.include_router(predict.router)

@app.get("/")
def home():
    return {"message": "Fake Job Detection Backend Running"}
