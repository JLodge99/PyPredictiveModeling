import os
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM,Dropout,Dense
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def prepareData(data_file, seq_length):
	data_len = len(data_file)
	X_train = []
	y_train = []
	for i in range(seq_length, data_len - 1):
		X_train.append(data_file[i - seq_length:i])
		y_train.append(data_file[i + 1])
	X_train = np.array(X_train).astype('float32')
	y_train = np.array(y_train).astype('float32')

	return X_train, y_train

data = pd.read_csv("Data\\AAPL_5y.csv")
data = np.array(data['Open'])
data_len = len(data)
scaler=MinMaxScaler(feature_range=(0,1))
data = np.array(data)
data = scaler.fit_transform(data)
testing_data = data[1000:]
training_data = data[:1000]

X_train, y_train = prepareData(training_data, 300)


# define model
model=Sequential()
model.add(LSTM(units=50,return_sequences=True,input_shape=(np.shape(X_train)[1],1)))
model.add(LSTM(units=50))
model.add(Dense(1))
model.compile(loss='mean_squared_error',optimizer='adam')

model.fit(X_train, y_train, epochs=100, batch_size=1, verbose=2)

# model_data=data.values
# model_data = model_data[60:len(final_data)]
# model_data=model_data.reshape(-1,1)

# X_test = []
# for i in range(10, len(model_data) - 1):
#     X_test.append(final_data[i - 10:i])
# X_test = np.array(X_test).astype('float32')
# X_test=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))
# print(model_data.shape[0])
# predicted = model.predict(X_test)
# print(len(predicted))
# plt.plot(final_data[0:62], color="blue")
# plt.plot(range(71, len(final_data)), predicted, color = "red")
# plt.show()
