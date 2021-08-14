import csv
import datetime
import requests
from requests.exceptions import HTTPError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM,Dropout,Dense
from sklearn.preprocessing import MinMaxScaler

# Fetch data from URL
# Returns JSON
def fetchData(URL):
    try:
        response = requests.get(URL)
        data = response.json()
        return data[0]['data']

    except HTTPError as http_err:
        print("Error has occured: " + http_err)
        return 0

# Export to csv
def jsonToCsv(json, directory = "./Data", name = "data.csv"):
    np.savetxt(f"{directory}/{name}", json, delimiter=",")

if __name__ == "__main__":
    # execute only if run as a script
    print("Hello world")

# json_data = fetchData("https://www.cargurus.com/Cars/price-trends/priceIndexJson.action?entityIds=lb35&startDate=2%2F10%2F2021")
# jsonToCsv(json_data, directory = "./Data/2_10_2021", name="coupe.csv")