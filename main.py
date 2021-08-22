import csv
import os
import datetime
import requests
from requests.exceptions import HTTPError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plotShit(foo:str):

    data = pd.read_csv(foo, index_col='Time(ms)')
    print(data)
    plt.plot(data)
    plt.xlabel("Time(ms)")
    plt.ylabel("Price($)")
    plt.show()

# Fetch data from URL API
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
    # plotShit("C:\\Users\\Jrld1\\Documents\\CodingProjects\\PyPredictiveModeling\\Data\\2_10_2021\\sedan.csv")

# json_data = fetchData("https://www.cargurus.com/Cars/price-trends/priceIndexJson.action?entityIds=lb35&startDate=2%2F10%2F2021")
# jsonToCsv(json_data, directory = "./Data/2_10_2021", name="coupe.csv")

data = pd.read_csv('DATA\\AAPL_5y.csv')
print(data['Open'])