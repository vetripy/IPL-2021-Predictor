import pandas as pd 
import os




df = pd.read_csv(r'{0}/csv/testInput.csv'.format(os.path.dirname(os.path.abspath(__file__))),low_memory=False)


def function(matchid):

    new = df.loc[df['match_id']==i]

    
    new = new.loc[new['ball']<=5.6]

    new.drop(new[new['innings']>2].index,inplace=True)

    cond = [i for i in new['innings'].unique()]

    if cond!=[1,2]:
        
        return(pd.DataFrame())
    
    else:

        batsman = new.groupby(['venue', 'innings', 'batting_team', 'bowling_team','striker'])[['runs_off_bat','extras','wides','noballs','byes','legbyes']].sum()
        batsman['score'] = batsman['runs_off_bat']+batsman['extras']
        batsman = batsman.drop(columns=['runs_off_bat','extras','wides','noballs','byes','legbyes'])


        return(batsman)

ids = [i for i in df['match_id'].unique()]


match_data = pd.DataFrame()


print(ids[-1])

for i in ids[-2:]:
    
    data = function(i)

    
    if data.empty != True:

        match_data = match_data.append(function(i))
        
        

print(match_data)
