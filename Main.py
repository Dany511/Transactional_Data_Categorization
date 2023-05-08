from array import array
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import predict

app=FastAPI()

@app.get('/')
def home():
    return{"home":"Transaction data Categorization api"}

class InputIn(BaseModel):
    description:array



class OutputOut(InputIn):
    forecast: array


@app.post("/predict", response_model=OutputOut, status_code=200)
def get_prediction(payload: InputIn):
    data = payload.data

    prediction_list = predict(description)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"forecast":prediction_list }
    return response_object