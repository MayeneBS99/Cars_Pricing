import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# __file__ : chemin relatif
# os.path.abspath : chemin absolue (c/users/etc)
# base_dir : chemin avec uniquement des dossiers

MODEL_PATH = os.path.join(BASE_DIR, "../model/rf_model.joblib")
IMPUTER_PATH = os.path.join(BASE_DIR, "../model/imputer.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "../model/encoder.pkl")