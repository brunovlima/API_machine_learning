import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pickle


filename = r'C:\Users\TEL\OneDrive - Fatec Centro Paula Souza\5º SEMESTRE\LP3\API_IRIS\IRIS.csv'
df = pd.read_csv(filename, sep=',')
le = LabelEncoder()
df['species'] = le.fit_transform(df['species'])


X = df.drop(columns=['species'])
Y = df['species']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=5)
model = LogisticRegression()
dfmodel = model.fit(x_train, y_train)

file = open('irishtopickle.pkl', 'wb')
pickle.dump(dfmodel, file)
