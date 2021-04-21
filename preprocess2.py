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

        balls = new.groupby(['runs_off_bat','innings','bowler']).size().reset_index(name='counts')
        balls=balls[(balls.runs_off_bat==0)]
        bowler = new.groupby(['venue', 'innings', 'batting_team','bowler'])[['player_dismissed','wides','noballs']].count()
        bowler['dot_balls'] = balls['counts'].values
        bowler['extra']=bowler['wides']+bowler['noballs']
        bowler = bowler.drop(columns=['wides','noballs'])
        
        return(batsman,bowler)


def bowling_stats():
    bowler_stats=pd.DataFrame()
    bowler_stats = bowler_stats.append(df)
    #-----------------------------------------------------------------------------------
    #WICKET STATS
    bowler_stats=bowler_stats.groupby(['match_id','bowler','batting_team'],as_index=False)[['player_dismissed']].count()
    bowler_stats=bowler_stats.groupby(['bowler','batting_team'],as_index=False)[['player_dismissed']].mean()
    bowler_stats['player_dismissed']=bowler_stats['player_dismissed'].astype(int)
    #-----------------------------------------------------------------------------------
    #NO. OF OVERS
    over=df.groupby(['match_id','bowler','batting_team'],as_index=False)[['ball']].size().reset_index(name='ball_count')
    over=over.groupby(['bowler','batting_team'],as_index=False)[['ball_count']].sum()
    over['overs']=over['ball_count'].div(6)
    over=over.drop(columns=['ball_count'])
    #------------------------------------------------------------------------------------------
    #ECONOMY STATS
    economy=df.groupby(['match_id','bowler','batting_team'],as_index=False)[['runs_off_bat','extras']].sum()
    economy['economy']=economy['runs_off_bat']+economy['extras']
    economy = economy.drop(columns=['runs_off_bat','extras'])
    economy=economy.groupby(['bowler','batting_team'],as_index=False)[['economy']].sum()
    economy['economy']=economy['economy'].div(over['overs'].values)
    bowler_stats['avg_wkts']=bowler_stats['player_dismissed'].values
    bowler_stats=bowler_stats.drop(columns=['player_dismissed'])
    bowler_stats['economy']=economy['economy'].values
    bowler_stats['overs']=over['overs'].values
    bowler_stats['economy']=bowler_stats['economy'].round(decimals=2)
    bowler_stats['overs']=bowler_stats['overs'].round(decimals=2)
    
    #----------------------------------------------------------------------------------------
    
    return bowler_stats



<<<<<<< HEAD

# match_data = pd.DataFrame()

=======
bowler_stats=pd.DataFrame()
bat_data = pd.DataFrame()
ball_data = pd.DataFrame()
bowler_stats=bowling_stats()
>>>>>>> 1fd4e69ec6a9cdd39d11d0e10205a3570db552fe



# for i in ids[:5]:
    
<<<<<<< HEAD
#     data = function(i)

    
#     if data.empty != True:

#         match_data = match_data.append(data)
        
        

=======
    databat,databall = function(i)
    
    
    #if databat.empty != True and databall != True:

    bat_data = bat_data.append(databat)
    ball_data = ball_data.append(databall)
        

print(bowler_stats)
>>>>>>> 1fd4e69ec6a9cdd39d11d0e10205a3570db552fe
