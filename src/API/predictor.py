import joblib
import pandas as pd
from src.preprocessing.preprocessing import preprocess_data
from src.API.config import MODEL_PATH

def load_model():
    """
    charge le model entrainé
    """
    return joblib.load(MODEL_PATH)

def predict_price(input_data : dict):

    df_preprocessed = pd.DataFrame([input_data])

    df_preprocessed = preprocess_data(df_preprocessed)

    model = load_model()

    prediction = model.predict(df_preprocessed)

    return prediction[0]