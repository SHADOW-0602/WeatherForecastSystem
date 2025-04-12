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

#Quick Start
1. Install dependencies
   pip install -r requirements.txt
2.  Run the system
   python weather_forecast.py
3. Follow the prompts
Enter your location (e.g., "New York, USA" or postal code)

Choose a prediction date or press Enter for tomorrow's forecast

View your weather prediction!

#Sample Output
=== Weather Prediction ===
Location: Mumbai, Maharashtra, India
Date/Time: 2023-07-15 14:00:00
Predicted Temperature: 32.5°C
Predicted Conditions: Partly Cloudy

Condition Probabilities:
- Clear: 45.2%
- Partly Cloudy: 32.1%
- Cloudy: 12.4%
- Light Rain: 10.3%

#Contributing
Contributions are welcome! Please open an issue or PR for:

Bug fixes

New features

Documentation improvements
