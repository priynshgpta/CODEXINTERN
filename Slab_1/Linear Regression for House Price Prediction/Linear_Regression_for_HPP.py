import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data_path = 'C:\\Users\\priya\\Desktop\\Work Data\\New Data\\CodePlayground\\CODEXINTERN\\Slab_1\\Linear Regression for House Price Prediction\\Housing.csv'

def train_house_price_model(data_path):
    df = pd.read_csv(data_path)

    print(df.head())

    required_columns = {'area', 'bedrooms', 'furnishingstatus', 'mainroad', 'price'}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"Dataset must contain columns: {required_columns}")

    df['furnishingstatus'] = df['furnishingstatus'].astype('category').cat.codes
    df['mainroad'] = df['mainroad'].map({'yes': 1, 'no': 0})

    X = df[['area', 'bedrooms', 'furnishingstatus', 'mainroad']]
    y = df['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print('MSE:', mean_squared_error(y_test, predictions))

# Call the function with the dataset path
train_house_price_model(data_path)
