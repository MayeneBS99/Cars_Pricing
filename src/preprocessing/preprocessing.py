import pandas as pd
import numpy as np
import joblib
from src.API.config import IMPUTER_PATH, ENCODER_PATH

encoder = joblib.load(ENCODER_PATH)
imputer = joblib.load(IMPUTER_PATH)

def format_value(value):
    if not pd.isnull(value):
        try:
            value = value.split(" ")[0]
            return float(value)
        except ValueError:
            return np.nan
    else :
        return value


def preprocess_data(input_data : pd.DataFrame) -> pd.DataFrame:
    """
    Apply necessaries transformations to our data before 
    prediction

    input_data : Dataframe which contains raw data
    return : DataFrame transformed et ready to be used by the model
    """
    categoricals_variables = ['Location','Year','Fuel_Type',
                          'Transmission','Owner_Type']
    quantitatives_variables = [ 'Kilometers_Driven', 'Mileage','Engine','Power','Seats']

    # patch values format for one variables
    for var in ['Mileage','Engine','Power']:
        input_data[var] = input_data[var].apply(format_value)

    # patch values "Year" which didn't appear in the train set
    input_data["Year"]  = input_data["Year"].astype("category")
    input_data = input_data[input_data["Year"] != 1996]
    input_data["Year"] = input_data["Year"].cat.remove_unused_categories() 

    # preprocessing on quantitatives variables
    input_data_quant = imputer.transform(input_data[quantitatives_variables])
    input_data_quant = pd.DataFrame(input_data_quant, columns = quantitatives_variables )

    # preprocessing on categoricals variables
    input_data_cat = encoder.transform(input_data[categoricals_variables])
    variables = encoder.get_feature_names_out(categoricals_variables)
    input_data_cat = pd.DataFrame(input_data_cat, columns = variables)
    
    for var in variables:
        input_data_cat[var] = input_data_cat[var].apply(int)

    # final dataset
    input_data_final = pd.concat([input_data_quant, input_data_cat], axis = 1)

    return input_data_final

    




