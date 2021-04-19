import pandas as pd 
import os

df=pd.read_csv(r'{0}/all_matches.csv'.format(os.path.dirname(os.path.abspath(__file__))),low_memory=False)

new=df.loc[df['match_id']==335982]
run=new.groupby(['innings'])[['runs_off_bat','extras','wides','noballs','byes','legbyes']].sum()
run['totalscore']=run['runs_off_bat']+run['wides']+run['noballs']+run['byes']+run['legbyes']

first_innings_wickets = 0
second_innings_wickets = 0

for i in new['player_dismissed']:
    if type(i)==str:
        a = new[new['player_dismissed']==i]['innings']
        for i in a:
            if i == 1:
                first_innings_wickets+=1
            if i == 2:
                second_innings_wickets+=1

print(first_innings_wickets,second_innings_wickets)
