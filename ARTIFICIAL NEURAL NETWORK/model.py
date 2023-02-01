# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import tensorflow as tf
import keras

dataset = pd.read_csv('HousePrediction.csv')
x = dataset.drop(columns=['price'])
y = dataset[['price']]

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
x['city'] = le.fit_transform(x['city'])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

ann = keras.models.Sequential()

ann.add(keras.layers.Dense(units=6, activation='relu', input_shape=(6,)))

ann.add(keras.layers.Dense(units=6, activation='relu'))

ann.add(keras.layers.Dense(1))

ann.compile(optimizer = 'adam', loss = 'mean_squared_error')

ann.fit(X_train, y_train, batch_size = 32, epochs = 100)

# test_data = np.array([2014, 36, 4.0, 2.50, 2820, 8408])
# print(ann.predict(test_data.reshape(1,6), batch_size=1))

# y_pred = ann.predict(X_test)
# print(np.concatenate((y_pred.reshape(len(y_pred),1), np.array(y_test).reshape(len(np.array(y_test)),1)),1))

# from joblib import dump, load
# dump(ann, 'model.joblib')

# model_in = load('model.joblib')
# test_data = np.array([2014, 36, 4.0, 2.50, 2820, 8408])
# print(model_in.predict(test_data.reshape(1,6), batch_size=1))

# import pickle
# pickle.dump(ann, open('model.pkl','wb'))

ann.save('model.h5')