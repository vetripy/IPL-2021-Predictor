import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
temp=pd.DataFrame()
df = pd.read_csv(r"{0}/testInput.csv".format(sys.path[0]),low_memory=False)
new=pd.DataFrame()
new=new.append(df)
#df=df.loc[df['venue']=='Wankhede Stadium']
#df=df.loc[df['bowler']=='AD Russell']
df=df.drop(columns=['other_wicket_type', 'other_player_dismissed','season'
,'start_date','batting_team','bowling_team','byes','legbyes','noballs'
,'penalty','wides','striker','non_striker'])
df=df.groupby(['match_id','venue','bowler'],as_index=False)[['runs_off_bat','extras']].sum()
df['score']=df['runs_off_bat']+df['extras']
df=df.drop(columns=['runs_off_bat','extras'])
df=df.groupby(['venue','bowler'],as_index=False)[['score']].mean()
df['score']=df['score'].round(decimals=2)
temp['venue']=df['venue'].values
temp['bowler']=df['bowler'].values
df['venue'] = le.fit_transform(df.venue.values)
df['bowler']=le.fit_transform(df.bowler.values)

venue_dict = dict(zip(temp.venue, df.venue))
bowler_dict= dict(zip(temp.bowler,df.bowler))

X=df[['venue','bowler']]
y=df['score']
x_train,x_test,y_train,y_test=train_test_split(X,y,random_state=1)
linreg=LinearRegression()
linreg.fit(x_train,y_train)
data=[[venue_dict['Rajiv Gandhi International Stadium, Uppal'],bowler_dict['S Kaul']]]
score=linreg.predict(data)
print(score)

new=new.loc[new['match_id']==1082609]
new=new.groupby('bowler')[['runs_off_bat','extras']].sum()
new['score']=new['runs_off_bat']+new['extras']

print(new)