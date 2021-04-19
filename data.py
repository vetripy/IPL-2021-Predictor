import pandas as pd 
import os

df = pd.read_csv(r'{0}/all_matches.csv'.format(os.path.dirname(os.path.abspath(__file__))),low_memory=False)

def function(matchid,innings):
    

    new = df.loc[df['match_id']==matchid]
    new = new.loc[new['ball']<=5.6]
    new.drop(new[new['innings']>2].index,inplace=True)
    run = new.groupby(['innings'])[['runs_off_bat','extras','wides','noballs','byes','legbyes']].sum()

    run['totalscore'] = run['runs_off_bat']+run['wides']+run['noballs']+run['byes']+run['legbyes']
    
    try:
        run['innings'] = [1,2]
    except Exception:
        run['innings'] = [1]
    
    run['wickets'] = new.groupby(['innings'])[['player_dismissed']].count()
    

    return(run[['innings','totalscore','wickets']].loc[run['innings']==innings])


ids = [i for i in df['match_id'].unique()]


first_innings = pd.DataFrame()
second_innings=pd.DataFrame()

for i in ids:
    first_innings = first_innings.append(function(i,1))
    second_innings=second_innings.append(function(i,2))
    second_innings['target_score']=first_innings['totalscore'].values

#first_innings.to_csv("First_Innings.csv")
print(second_innings)
