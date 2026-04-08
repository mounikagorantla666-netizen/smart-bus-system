import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Training data
# distance(km), traffic level, speed(kmph)
X = [
    [5,2,40],
    [3,1,50],
    [7,3,35],
    [2,1,45],
    [6,2,38]
]

# Arrival time (minutes)
y = [8,4,12,3,10]

model = LinearRegression()

model.fit(X,y)

joblib.dump(model,"bus_arrival_model.pkl")

print("Model trained successfully")