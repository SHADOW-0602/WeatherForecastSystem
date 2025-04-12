from flask import Flask, render_template
import pandas as pd
from ml_model.predict import WeatherPredictor
from data_pipeline.fetch_data import fetch_historical_data

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Get latest data
    df = fetch_historical_data(days=7)
    
    # Make predictions
    predictor = WeatherPredictor()
    predictions = predictor.predict(df.iloc[[-1]])  # Predict for most recent data
    
    return render_template('dashboard.html', 
                         temperature=predictions['temperature'],
                         condition=predictions['condition'],
                         data=df.to_dict('records'))

if __name__ == '__main__':
    app.run(debug=True)
