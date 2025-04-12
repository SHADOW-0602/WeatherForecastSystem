import pandas as pd

def create_features(df, target='temperature'):
    df = df.copy()
    df['time'] = pd.to_datetime(df['time'])
    df = df.set_index('time').sort_index()
    
    # Common features
    df['hour'] = df.index.hour
    df['day_of_week'] = df.index.dayofweek
    df['month'] = df.index.month
    
    if target == 'temperature':
        # Temperature-specific features
        for lag in [1, 24]:
            df[f'temperature_lag_{lag}'] = df['temperature'].shift(lag, freq='h')
        df['temperature_rolling_avg_24h'] = df['temperature'].rolling(window='24h').mean()
        features = [col for col in df.columns if col != 'temperature']
        return df[features], df['temperature']
    
    else:
        # Condition-specific features
        for lag in [1, 24]:
            df[f'precipitation_lag_{lag}'] = df['precipitation'].shift(lag, freq='h')
            df[f'cloud_cover_lag_{lag}'] = df['cloud_cover'].shift(lag, freq='h')
        features = [col for col in df.columns if col != 'weather_condition']
        return df[features], df['weather_condition']
