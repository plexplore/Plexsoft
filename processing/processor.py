import pandas as pd
import numpy as np

# Beispiel DataFrame
data = pd.read_csv("data-41.csv", header=None, names=["id", "time", "value"], sep=";", index_col=None)

# Sensor-ID Mapping
data_mapping = {
    "Altitude": 16,
    "Latitude": 14,
    "Longitude": 15,
    "Air Pressure": 1,
    "Temperature": 0,
    "Humidity": 2,
    "Oxygen": 32,
    "Dust": 31,
    "Nitrogen": 33,
}
