import pandas as pd

def clean_weather_data(df):
    # Rename columns
    column_map = {
        "temperature_2m": "temperature",
        "relative_humidity_2m": "humidity",
        "dew_point_2m": "dew_point",
        "pressure_msl": "pressure",
        "cloud_cover": "cloud_cover"
    }
    df = df.rename(columns=column_map)
    
    # Handle missing values
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)
    
    return df
