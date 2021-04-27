import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
from preprocess import data
import joblib


team_encoder = LabelEncoder()
venue_encoder = LabelEncoder()

df = data()

temp=pd.DataFrame()

temp['venue'] = df['venue'].values
temp['batting_team'] = df['batting_team'].values
temp['bowling_team'] = df['bowling_team'].values

df['batting_team'] = team_encoder.fit_transform(df.batting_team.values)
df['bowling_team'] = team_encoder.fit_transform(df.bowling_team.values)
df['venue'] = venue_encoder.fit_transform(df.venue.values)


batting_team_dict = dict(zip(temp['batting_team'],df['batting_team']))
bowling_team_dict = dict(zip(temp['bowling_team'],df['bowling_team']))
venue_dict = dict(zip(temp['venue'],df['venue']))


X=df[['venue','batting_team','bowling_team']]
y=df['total_runs']


x_train,x_test,y_train,y_test = train_test_split(X,y,random_state=1)

linreg = LinearRegression()
linreg.fit(x_train,y_train)

venue = "Sardar Patel Stadium, Motera"
ball = "Kings XI Punjab"
bat = "Kolkata Knight Riders"

data = [[venue_dict[venue],batting_team_dict[bat],bowling_team_dict[ball]]]

print(linreg.predict(data))
