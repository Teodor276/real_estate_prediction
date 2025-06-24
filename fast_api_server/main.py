
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import util
from pydantic import BaseModel
import numpy as np
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a basic route
@app.get("/get_location_names")
def get_location_names():
    location_names = util.get_location_names()

    response = JSONResponse(content={"location": location_names})

    response.headers['Access-Control-Allow-Origin'] = '*'

    return response


class HomePriceRequest(BaseModel):
    location: str
    sqft: float
    bhk: int
    bath: int

@app.post("/predict_home_price")
def predict_home_price(request: HomePriceRequest):
    location = request.location
    sqft = request.sqft
    bhk = request.bhk
    bath = request.bath

    predicted_price = util.get_estimated_price(location, sqft, bhk, bath)

    return JSONResponse(content={"predicted_price": predicted_price})
