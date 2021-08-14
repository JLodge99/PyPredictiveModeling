import csv
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM,Dropout,Dense
from sklearn.preprocessing import MinMaxScaler

if __name__ == "__main__":
    # execute only if run as a script
    print("Hello world")