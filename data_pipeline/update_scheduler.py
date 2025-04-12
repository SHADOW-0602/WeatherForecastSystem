import time
import schedule
import logging
from datetime import datetime
from ..fetch_data import fetch_historical_data
from ..clean_data import clean_weather_data
from ml_model.train import train_temperature_model, train_condition_model
from ml_model.predict import WeatherPredictor
import pandas as pd
import pytz

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WeatherDataScheduler:
    def __init__(self):
        self.latest_data = None
        self.predictor = None
        self.timezone = pytz.timezone('UTC')
        
    def fetch_and_process_data(self):
        """Fetch new data and process it"""
        try:
            logger.info("Starting scheduled data update")
            
            # 1. Fetch new data
            logger.info("Fetching fresh weather data")
            raw_data = fetch_historical_data(days=1)  # Get just latest day
            
            # 2. Clean and process data
            logger.info("Cleaning and processing data")
            cleaned_data = clean_weather_data(raw_data)
            
            # 3. Update latest data store
            if self.latest_data is None:
                self.latest_data = cleaned_data
            else:
                # Remove duplicates and keep newest
                combined = pd.concat([self.latest_data, cleaned_data])
                combined = combined.drop_duplicates(subset=['time'], keep='last')
                self.latest_data = combined.sort_values('time')
            
            logger.info(f"Data updated. Total records: {len(self.latest_data)}")
            return True
            
        except Exception as e:
            logger.error(f"Data update failed: {str(e)}")
            return False

    def retrain_models(self):
        """Retrain models with latest data"""
        try:
            if self.latest_data is None or len(self.latest_data) < 24:  # At least 1 day of data
                logger.warning("Insufficient data for retraining")
                return False
                
            logger.info("Starting model retraining")
            
            # 1. Prepare features
            X_temp, y_temp = create_features(self.latest_data, target='temperature')
            X_cond, y_cond = create_features(self.latest_data, target='weather_condition')
            
            # 2. Train models
            logger.info("Training temperature model")
            temp_model = train_temperature_model(X_temp, y_temp)
            
            logger.info("Training condition model")
            cond_model = train_condition_model(X_cond, y_cond)
            
            # 3. Update predictor
            self.predictor = WeatherPredictor()
            logger.info("Model retraining completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"Model training failed: {str(e)}")
            return False

    def generate_predictions(self):
        """Generate new predictions with latest models"""
        if self.predictor is None or self.latest_data is None:
            logger.warning("Cannot generate predictions - models or data not available")
            return None
            
        try:
            logger.info("Generating new predictions")
            latest_record = self.latest_data.iloc[[-1]]  # Get most recent observation
            prediction = self.predictor.predict(latest_record)
            
            logger.info(f"New prediction: Temp={prediction['temperature']}°C, Condition={prediction['condition']}")
            return prediction
            
        except Exception as e:
            logger.error(f"Prediction failed: {str(e)}")
            return None

    def run_scheduled_updates(self, update_interval=6):
        """Run the scheduler with specified interval (in hours)"""
        logger.info(f"Starting weather data scheduler (updates every {update_interval} hours)")
        
        # Schedule jobs
        schedule.every(update_interval).hours.do(self.full_update_cycle)
        
        # Initial run
        self.full_update_cycle()
        
        # Run indefinitely
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

    def full_update_cycle(self):
        """Complete update cycle: data -> models -> predictions"""
        success = self.fetch_and_process_data()
        if success:
            # Only retrain models if we have at least 7 days of data
            if len(self.latest_data) >= 24*7:
                self.retrain_models()
            else:
                logger.info(f"Waiting for more data before retraining (current: {len(self.latest_data)} records)")
            
            # Always try to generate predictions if we have any data
            if len(self.latest_data) > 0:
                self.generate_predictions()

if __name__ == "__main__":
    scheduler = WeatherDataScheduler()
    
    # Example usage:
    # scheduler.run_scheduled_updates(update_interval=6)  # Updates every 6 hours
    
    # For testing, run one update cycle immediately
    scheduler.full_update_cycle()
