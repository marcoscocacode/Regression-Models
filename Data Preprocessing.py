# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:05:06 2020

@author: Marcos_Coca_F.
"""

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset

dataset = pd.read_csv('/Users/Alien/Desktop/Machine+Learning+A-Z+(Codes+and+Datasets)/Machine Learning A-Z (Codes and Datasets)/Part 1/Section 2/Python/Data.csv')

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(x)
print(y)

# Taking care of missing data

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values= np.nan, strategy= 'mean')
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

print(x)

# Encoding the independent variable

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('enconder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

print(x)

# Encoding the dependent variable

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y = le.fit_transform(y)

print(y)

# Spltting the dataset into training set and test set

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 0)

print(x_train)
print(x_test)
print(y_train)
print(y_test)

# Feature scaling

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
x_train[:, 3:] + sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] + sc.fit_transform(x_test[:, 3:])

print(x_train)
print(x_test)
