import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
from preprocess import bowling_stats
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
team_encoder = LabelEncoder()

df = bowling_stats()
df = df.fillna(method='ffill')

df.to_csv('bowlingdata.csv')
test_case=pd.read_csv('D:\PSR FOLDER\python\IPL-2021-Predictor\input_test_data.csv')#to the predictor
temp=pd.DataFrame()
temp['bowler'] = df['bowler'].values
temp['batting_team'] = df['batting_team'].values

df['bowler'] = team_encoder.fit_transform(df.bowler.values)
df['batting_team'] = team_encoder.fit_transform(df.batting_team.values)

bowler_dict= dict(zip(temp.bowler,df.bowler))
batting_team_dict = dict(zip(temp.batting_team,df.batting_team))

X=df[['bowler','batting_team','innings']]
y=df['economy']

x_train,x_test,y_train,y_test=train_test_split(X,y,random_state=1)

y_pred=0
linreg=LinearRegression()
linreg.fit(x_train,y_train)
n=len(test_case['bowlers'].values[0].split(','))#to the predictor
overs=6/n#to the predictor

for i in test_case['bowlers'].values[0].split(','):#full loop to the predictor
    data=[[bowler_dict[i],batting_team_dict[test_case['batting_team'].values[0]],test_case['innings'].values[0]]]
    y_pred+=(int(linreg.predict(data))*overs)

print(y_pred)