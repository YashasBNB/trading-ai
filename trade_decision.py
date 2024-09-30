# trade_decision.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Function to create features and labels for ML
def create_features_and_labels(data):
    # Use technical indicators and candlestick patterns as features
    features = data[['MACD', 'Signal', 'RSI', 'BB_upper', 'BB_lower']]  # Add more features if necessary

    # Define the labels (for binary trading: 1 for buy, 0 for sell)
    data['Label'] = (data['close'].shift(-1) > data['close']).astype(int)
    labels = data['Label']

    return features, labels

# Example ML model training
def train_ml_model(data):
    features, labels = create_features_and_labels(data)

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Initialize and train the RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Optionally, evaluate the model (you can add more evaluation metrics here)
    score = model.score(X_test, y_test)
    print(f"Model Accuracy: {score * 100:.2f}%")

    return model

# Function to make a trade decision based on the ML model
def make_ml_trade_decision(model, data):
    features, _ = create_features_and_labels(data)

    # Get the latest feature values for the most recent data point
    latest_features = features.iloc[-1:].values

    # Make a prediction (0 = Sell, 1 = Buy)
    prediction = model.predict(latest_features)

    if prediction == 1:
        return "BUY"
    else:
        return "SELL"
