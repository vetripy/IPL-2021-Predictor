import pandas as pd 
import os

df=pd.read_csv(r'{0}/all_matches.csv'.format(os.path.dirname(os.path.abspath(__file__))),low_memory=False)

new=df.loc[df['match_id']==335982]
new = new.loc[new['ball']<=5.6]
run=new.groupby(['innings'])[['runs_off_bat','extras','wides','noballs','byes','legbyes']].sum()
run['totalscore']=run['runs_off_bat']+run['wides']+run['noballs']+run['byes']+run['legbyes']


run['wickets']=new.groupby(['innings'])[['player_dismissed']].count()
print(run)
