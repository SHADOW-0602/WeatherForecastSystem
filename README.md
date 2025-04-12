# WeatherForecastSystem
A machine learning-powered weather forecasting system that predicts temperature and weather conditions using historical and real-time data from the Open-Meteo API.

#Features
Accurate predictions of temperature and weather conditions (Clear, Rainy, Cloudy, etc.)

Automated data pipeline for fetching and updating weather data

Interactive visualizations of weather trends and predictions

Geolocation support - enter any city or postal code

Scheduled updates to keep forecasts fresh

#Tech Stack
Python 3.8+

Scikit-learn (Random Forest, Ridge Regression)

Pandas & NumPy for data processing

Open-Meteo API for weather data

Geopy for location services

Plotly for interactive visualizations

Logging for error tracking

## Installation
1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up configuration in `config/` files

## Usage
- Train models: `python ml_model/train.py`
- Run dashboard: `python dashboard/app.py`
- Schedule updates: Configure in `data_pipeline/scheduler/`

## Requirements
- Python 3.8+
- See requirements.txt for dependencies
