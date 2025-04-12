import requests
import pandas as pd
import yaml
from datetime import datetime, timedelta

with open('config/api_config.yaml') as f:
    config = yaml.safe_load(f)

API_URL = config['openmeteo']['base_url']

def fetch_historical_data(days=30):
    params = {
        "latitude": config['location']['latitude'],
        "longitude": config['location']['longitude'],
        "hourly": "temperature_2m,relative_humidity_2m,dew_point_2m,pressure_msl,cloud_cover",
        "timezone": "auto",
        "start_date": (datetime.now() - timedelta(days=days-1)).strftime('%Y-%m-%d'),
        "end_date": datetime.now().strftime('%Y-%m-%d')
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    return pd.DataFrame(data["hourly"])
