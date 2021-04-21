import pandas as pd 
import os




def score(matchid):

    #--------Opening the input dataframe and store it as df-------------------
    df = pd.read_csv(r'{0}/csv/testInput.csv'.format(os.path.dirname(os.path.abspath(__file__))),low_memory=False)


    #--------Cleaning the data with respect to the matchid and till 6th over---
    score = df.loc[df['match_id']==matchid]
    score = score.loc[score['ball']<=5.6]


    #--------Removing the superover innings------------------------------------
    score.drop(score[score['innings']>2].index,inplace=True)

    #--------Returning empty dataframe if a mathch as only 1 innings-----------
    cond = [i for i in score['innings'].unique()]
    if cond!=[1,2]:
       
        return(pd.DataFrame())
    
    else:
    
        #------Grouping the data with reasaonable coolumns to get the score of each innings-------------
        score = score.groupby(['venue', 'innings', 'batting_team', 'bowling_team','striker'])[['runs_off_bat','extras']].sum()
        score['score'] = score['runs_off_bat'] + score['extras']
        score = score.drop(columns = ['runs_off_bat','extras'])

        #------Grouping the data with reasaonable coolumns to get the dotballs of each innings-------------
        balls = score.groupby(['runs_off_bat','innings','bowler']).size().reset_index()
        balls=balls[(balls.runs_off_bat==0)]
        dot_balls = score.groupby(['venue', 'innings', 'batting_team','bowler'])[['player_dismissed','wides','noballs']].count()
        dot_balls['dot_balls'] = balls['index'].values
        dot_balls['extra']=dot_balls['wides']+dot_balls['noballs']
        dot_balls = dot_balls.drop(columns=['wides','noballs'])
        
        return(score,dot_balls)



def strike_rate():

    #--------Opening the input dataframe and store it as df-----------------
    df = pd.read_csv(r'{0}/csv/testInput.csv'.format(os.path.dirname(os.path.abspath(__file__))),low_memory=False)


    #--------Changing the all the balls to 1 to count it easier--------------  
    one = [1 for i in range(len(df))]
    df['ball'] = one

    #--------Grouping the batsmen with their strike rate all the bowlers-----
    strike = df.groupby(['match_id','venue','striker','bowler'],as_index=False)[['runs_off_bat','ball']].sum()

    #--------Calculating the strike rate and adding them to the dataframe----
    strike['strike_rate'] = strike['runs_off_bat']/strike['ball']
    strike['strike_rate'] = strike['strike_rate']*100
    strike['strike_rate'] = strike['strike_rate'].round(decimals=2)

    
    return(strike)


def bowling_stats():

    #--------Opening the input dataframe and store it as df-----------------
    df = pd.read_csv(r'{0}/csv/testInput.csv'.format(os.path.dirname(os.path.abspath(__file__))),low_memory=False)

    bowler_stats=pd.DataFrame()
    bowler_stats = bowler_stats.append(df)

    #-----------Wicket Stats--------------------------------------------------
    bowler_stats=bowler_stats.groupby(['match_id','bowler','batting_team'],as_index=False)[['player_dismissed']].count()
    bowler_stats=bowler_stats.groupby(['bowler','batting_team'],as_index=False)[['player_dismissed']].mean()
    bowler_stats['player_dismissed']=bowler_stats['player_dismissed'].astype(int)


    #-----------No of overs----------------------------------------------------
    over=df.groupby(['match_id','bowler','batting_team'],as_index=False)[['ball']].size().reset_index()
    over=over.groupby(['bowler','batting_team'],as_index=False)[['index']].sum()
    over['overs']=over['index'].div(6)
    over=over.drop(columns=['index'])

    #-----------Economy Stats---------------------------------------------------
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
    

    
    return (bowler_stats)

print(bowling_stats())