from pydantic import BaseModel

class CarFeatures(BaseModel):
    Kilometers_Driven : int
    Mileage :str
    Engine : str
    Power : str
    Seats :float
    Location :  str
    Year : int
    Fuel_Type : str 
    Transmission :str
    Owner_Type : str
