from fastapi import FastAPI
from src.API.schemas import CarFeatures
from src.API.predictor import predict_price

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "API de prediction du prix des voitures"}

@app.post("/predict/")
def predict(car : CarFeatures):
    """
    Endpoint permettant de prédire le prix d'un vehicule
    """

    input_data = car.model_dump()
    predicted_price = predict_price(input_data)
    return {"Predicted_price": predicted_price}