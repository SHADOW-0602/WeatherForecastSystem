import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from .utils.feature_engineering import create_features
from config.model_params import RANDOM_FOREST_PARAMS

def train_temperature_model(X, y):
    model = make_pipeline(
        StandardScaler(),
        RandomForestRegressor(**RANDOM_FOREST_PARAMS)
    )
    model.fit(X, y)
    joblib.dump(model, "ml_model/saved_models/temperature_model.joblib")
    return model

def train_condition_model(X, y):
    model = make_pipeline(
        StandardScaler(),
        RandomForestClassifier(**RANDOM_FOREST_PARAMS)
    )
    model.fit(X, y)
    joblib.dump(model, "ml_model/saved_models/condition_model.joblib")
    return model

if __name__ == "__main__":
    from data_pipeline.fetch_data import fetch_historical_data
    df = fetch_historical_data(days=30)
    X_temp, y_temp = create_features(df, target='temperature')
    X_cond, y_cond = create_features(df, target='weather_condition')
    
    temp_model = train_temperature_model(X_temp, y_temp)
    cond_model = train_condition_model(X_cond, y_cond)
