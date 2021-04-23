import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
from preprocess import data
import joblib

team_encoder = LabelEncoder()

df = data()
df.to_csv('testdata.csv')
temp=pd.DataFrame()
temp['batting_team'] = df['batting_team'].values
temp['bowling_team'] = df['bowling_team'].values

#df['venue'] = le.fit_transform(df.venue.values)
df['batting_team'] = team_encoder.fit_transform(df.batting_team.values)
df['bowling_team'] = team_encoder.fit_transform(df.bowling_team.values)


#venue_dict = dict(zip(temp.venue, df.venue))
bowling_team_dict= dict(zip(temp.bowling_team,df.bowling_team))
batting_team_dict = dict(zip(temp.batting_team,df.batting_team))

X=df[['batting_team','bowling_team','wickets']]
y=df['total_runs']

x_train,x_test,y_train,y_test=train_test_split(X,y,random_state=1)

# linreg=LinearRegression()
# linreg.fit(x_train,y_train)

data=[[batting_team_dict["Kolkata Knight Riders"],bowling_team_dict["Chennai Super Kings"],5]]
dtree=DecisionTreeRegressor()
dtree.fit(x_train,y_train)
y_pred = dtree.predict(data)
print(y_pred)

# joblib.dump(linreg,r'{0}/regeression_model.joblib'.format(sys.path[0]))
# joblib.dump(team_encoder,r'{0}/team_encoder.joblib'.format(sys.path[0]))


