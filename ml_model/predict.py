import joblib
import pandas as pd
from .utils.feature_engineering import create_features

class WeatherPredictor:
    def __init__(self):
        self.temp_model = joblib.load("ml_model/saved_models/temperature_model.joblib")
        self.cond_model = joblib.load("ml_model/saved_models/condition_model.joblib")
        
    def predict(self, df):
        X_temp, _ = create_features(df, target='temperature')
        X_cond, _ = create_features(df, target='weather_condition')
        
        temp_pred = self.temp_model.predict(X_temp)
        cond_pred = self.cond_model.predict(X_cond)
        cond_proba = self.cond_model.predict_proba(X_cond)
        
        return {
            'temperature': temp_pred[0],
            'condition': cond_pred[0],
            'probabilities': cond_proba[0]
        }
