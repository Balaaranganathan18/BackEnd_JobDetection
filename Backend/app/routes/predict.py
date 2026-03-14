from fastapi import APIRouter
from pydantic import BaseModel
from app.services import prediction_service

router = APIRouter()

class JobInput(BaseModel):
    text: str

@router.post("/predict")
def predict_job(input: JobInput):

    result = prediction_service.predict_text(input.text)

    return result
