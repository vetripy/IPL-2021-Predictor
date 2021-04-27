import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
from preprocess import strike_rate
import joblib

name_encoder = LabelEncoder()

df = strike_rate()


temp = pd.DataFrame()
temp['striker'] = df['striker'].values
temp['bowling_team'] = df['bowling_team'].values

#df['venue'] = le.fit_transform(df.venue.values)
df['striker'] = name_encoder.fit_transform(df.striker.values)
df['bowling_team'] = name_encoder.fit_transform(df.bowling_team.values)


#venue_dict = dict(zip(temp.venue, df.venue))
striker_dict= dict(zip(temp.striker,df.striker))
bowling_team_dict = dict(zip(temp.bowling_team,df.bowling_team))

#print(striker_dict)
X=df[['striker','bowling_team']]
y=df['strike_rate']

x_train,x_test,y_train,y_test=train_test_split(X,y,random_state=1)

linreg=LinearRegression()
linreg.fit(x_train,y_train)

# strike_list = []

# try:

#     for i,j in temp['striker'].values,temp['bowling_team']:
#         strike_list.append(linreg.predict([[striker_dict[i],bowling_team_dict[j]]]))
# except Exception:
#     pass

#data=[[batting_team_dict["Kolkata Knight Riders"],bowling_team_dict["Chennai Super Kings"],5]]
# dtree=DecisionTreeRegressor()
# dtree.fit(x_train,y_train)
# y_pred = dtree.predict(data)
# print(y_pred)

joblib.dump(linreg,r'{0}/strike_regeression_model.joblib'.format(sys.path[0]))
joblib.dump(name_encoder,r'{0}/name_encoder.joblib'.format(sys.path[0]))


