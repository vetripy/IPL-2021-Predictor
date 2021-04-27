import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
from preprocess import data,strike_rate
import joblib


team_encoder = LabelEncoder()
venue_encoder = LabelEncoder()








X_train,X_test,Y_train,Y_test = train_test_split(x,Y,random_state=1)


