import pandas as pd
import numpy as np
import plotly.express as px

data = pd.read_excel("D:/PROGRAMMING/DWM/Food Delivery Time Prediction Case Study.xlsx")
#print(data.head())
#data.info()


# Set the earth's radius (in kilometers)
R = 6371

# Convert degrees to radians
def deg_to_rad(degrees):
    return degrees * (np.pi/180)

# Function to calculate the distance between two points using the haversine formula
def distcalculate(lat1, lon1, lat2, lon2):
    d_lat = deg_to_rad(lat2-lat1)
    d_lon = deg_to_rad(lon2-lon1)
    a = np.sin(d_lat/2)**2 + np.cos(deg_to_rad(lat1)) * np.cos(deg_to_rad(lat2)) * np.sin(d_lon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return R * c
  
# Calculate the distance between each pair of points
data['distance'] = np.nan

for i in range(len(data)):
    data.loc[i, 'distance'] = distcalculate(data.loc[i, 'Restaurant_latitude'], 
                                        data.loc[i, 'Restaurant_longitude'], 
                                        data.loc[i, 'Delivery_location_latitude'], 
                                        data.loc[i, 'Delivery_location_longitude'])
    
print(data.head())


from sklearn.model_selection import train_test_split
x = np.array(data[["Delivery_person_Age", 
                   "Delivery_person_Ratings", 
                   "distance"]])
y = np.array(data[["Time_taken(min)"]])
xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                test_size=0.10, 
                                                random_state=42)

# creating the LSTM neural network model
from keras.models import Sequential
from keras.layers import Dense, LSTM
model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape= (xtrain.shape[1], 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
model.summary()

def predict_delivery_time(age, rating, distance):
    # Simple prediction formula for demonstration
    time = (distance * 2) + (30 - age) * 0.5 + (5 - rating) * 3
    return max(time, 0)  # Ensures that time is not negative

# Define the input features
age = 23
rating = 4.9
distance = 12

# Now you can create the feature array
features = np.array([[age, rating, distance]])

print("Food Delivery Time Prediction")

# Call the prediction function
predicted_time = predict_delivery_time(age, rating, distance)
print(f"Predicted Delivery Time: {predicted_time:.2f} minutes")

# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, LSTM

# print("TensorFlow version:", tf.__version__)
