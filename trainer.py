import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
from preprocess import data,strike_rate,bowling_stats
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets

team_encoder = LabelEncoder()
venue_encoder = LabelEncoder()
name_encoder = LabelEncoder()
bowler_encoder = LabelEncoder()

df = data()
df2 = strike_rate()
df3 = bowling_stats()
df3=df3.fillna(method='ffill')

df['batting_team'] = team_encoder.fit_transform(df.batting_team.values)
df['bowling_team'] = team_encoder.fit_transform(df.bowling_team.values)

df2['venue'] = venue_encoder.fit_transform(df2.venue.values)
df2['striker'] = name_encoder.fit_transform(df2.striker.values)
df2['bowling_team'] = team_encoder.fit_transform(df2.bowling_team.values)

df3['bowler'] = bowler_encoder.fit_transform(df3.bowler.values)
df3['batting_team'] = team_encoder.fit_transform(df3.batting_team.values)


x=df[['batting_team','bowling_team','wickets']]
y=df['total_runs']


X=df2[['venue','striker','bowling_team']]
Y=df2['strike_rate']

X1=df3[['bowler','batting_team','innings']]
Y1=df3['economy']


x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1)
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=1)
X1_train,X1_test,Y1_train,Y1_test = train_test_split(X1,Y1,random_state=1)

linreg = LinearRegression()
linreg.fit(x_train,y_train)

linreg_2 = LinearRegression()
linreg_2.fit(X_train,Y_train)

linreg_3 = LinearRegression()
linreg_3.fit(X1_train,Y1_train)


joblib.dump(linreg,r'{0}/regeression_model.joblib'.format(sys.path[0]))
joblib.dump(linreg_2,r'{0}/new_regeression_model.joblib'.format(sys.path[0]))
joblib.dump(linreg_3,r'{0}/bowler_regeression_model.joblib'.format(sys.path[0]))
joblib.dump(team_encoder,r'{0}/team_encoder.joblib'.format(sys.path[0]))
joblib.dump(venue_encoder,r'{0}/venue_encoder.joblib'.format(sys.path[0]))
joblib.dump(name_encoder,r'{0}/name_encoder.joblib'.format(sys.path[0]))
joblib.dump(bowler_encoder,r'{0}/bowler_encoder.joblib'.format(sys.path[0]))
