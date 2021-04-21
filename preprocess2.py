import pandas as pd 
import os




df = pd.read_csv(r'{0}/csv/testInput.csv'.format(os.path.dirname(os.path.abspath(__file__))),low_memory=False)

def strike_rate():
    one = [1 for i in range(len(df))]

    df['ball'] = one

    new = df.groupby(['match_id','venue','striker','bowler'],as_index=False)[['runs_off_bat','ball']].sum()

    # new = new.loc[new['striker']==batter]
    # new = new.loc[new['bowler']==bowler]
    new['strike_rate'] = new['runs_off_bat']/new['ball']
    new['strike_rate'] = new['strike_rate']*100
    new['strike_rate'] = new['strike_rate'].round(decimals=2)
    print(new)
   # new.to_csv(r'{0}/csv/new_file.csv'.format(os.path.dirname(os.path.abspath(__file__))))
    
    

    
    return(new)

def function(matchid):

    new = df.loc[df['match_id']==matchid]
    new = new.loc[new['ball']<=5.6]

    new.drop(new[new['innings']>2].index,inplace=True)

    cond = [i for i in new['innings'].unique()]

    if cond!=[1,2]:
        
        return(pd.DataFrame())
    
    else:

        batsman = new.groupby(['venue', 'innings', 'batting_team', 'bowling_team','striker'])[['runs_off_bat','extras']].sum()
        batsman['score'] = batsman['runs_off_bat']+batsman['extras']
        batsman = batsman.drop(columns=['runs_off_bat','extras'])


        return(batsman)



# match_data = pd.DataFrame()




# for i in ids[:5]:
    
#     data = function(i)

    
#     if data.empty != True:

#         match_data = match_data.append(data)
        
        

