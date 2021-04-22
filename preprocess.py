import pandas as pd 
import sys


def data():
    
    #--------Opening the input dataframe and store it as data_file----------
    df = pd.read_csv(r"{0}/testInput.csv".format(sys.path[0]),low_memory=False)
    
    #--------Removing irrelevant columns-------------------------------------
    data_file = df.drop(columns=['season','start_date','wicket_type','other_wicket_type','other_player_dismissed'])


    #--------Calculating the total runs-------------------------------------
    data_file['total_runs'] = data_file['runs_off_bat'] + data_file['extras']
    data_file = data_file.drop(columns=['runs_off_bat','extras'])


    #--------Cleaning the data, to get data within 6 overs without super overs----
    data_file = data_file.loc[data_file['ball']<=5.6]
    data_file = data_file.loc[data_file['innings']<=2]

    #--------Grouping the data with relevant columns------------------------
    data_file = data_file.groupby(['match_id','venue','innings','batting_team','bowling_team'],as_index=False)[['total_runs']].sum()
    
    #--------Calculating the  wickets in each innings
    data_file_copy = df.copy()
    data_file_copy = data_file_copy.loc[data_file_copy['ball']<=5.6]
    data_file_copy = data_file_copy.loc[data_file_copy['innings']<=2]
    data_file_copy = data_file_copy.groupby(['match_id','venue','innings','batting_team','bowling_team'],as_index=False)[['player_dismissed']].count()
    data_file['wickets'] = data_file_copy['player_dismissed']
    del data_file_copy

    #--------Calculating the no of bowlers-------------------------------------
    data_file_copy = df.copy()
    data_file_copy = data_file_copy.loc[data_file_copy['ball']<=5.6]
    data_file_copy = data_file_copy.loc[data_file_copy['innings']<=2]
    data_file_copy = data_file_copy.groupby(['match_id','venue','innings','batting_team','bowling_team','bowler'],as_index=False)[['ball']].count()
    data_file_copy = data_file_copy.drop(columns=['ball'])
    data_file_copy = data_file_copy.groupby(['match_id','venue','innings','batting_team','bowling_team'],as_index=False)[['bowler']].count()
    data_file['no of bowlers'] = data_file_copy['bowler']
    del data_file_copy

    data_file.to_csv('test.csv')
    return(data_file)


def strike_rate():

    #--------Opening the input dataframe and store it as df-----------------
    df = pd.read_csv(r'{0}/testInput.csv'.format(sys.path[0]),low_memory=False)

    #--------Changing the all the balls to 1 to count it easier--------------  

    #strike = df.loc[df['innings']<=2]
    a = df.copy()
    a = a.loc[a['ball']<=5.6]
    a = a.loc[a['innings']<=2]
    a = a.groupby(['match_id','venue','bowling_team'],as_index=False)[['runs_off_bat','extras']].sum()
    a['totalscore'] = a['runs_off_bat']+a['extras']
    a = a.drop(columns=['runs_off_bat','extras'])
    
 
    one = [1 for i in range(len(df))]
    df['ball'] = one

    #--------Grouping the batsmen with their strike rate all the bowlers-----
    strike = df.groupby(['match_id','striker','venue','bowling_team'],as_index=False)[['runs_off_bat','ball']].sum()
    
    

    #--------Calculating the strike rate and adding them to the dataframe----
    strike['strike_rate'] = strike['runs_off_bat']/strike['ball']
    strike['strike_rate'] = strike['strike_rate']*100
    strike['strike_rate'] = strike['strike_rate'].round(decimals=2)

    #--------Removing used columns and reseting the index--------------------
    strike = strike.drop(columns=['ball'])
    
    #--------Average strike rate of batsmen-----------------------------------
    strike = strike.groupby(['match_id','venue','striker','runs_off_bat'],as_index=False)[['strike_rate']].mean().round(decimals=2)
    strike['score'] = a['totalscore']
    del a
    strike.to_csv('test.csv')
    #return(strike.loc[strike['striker']==batsman_name].values[0][1])
    return(strike)


def bowling_stats(bowler_name):

    #--------Opening the input dataframe and store it as df-----------------
    df = pd.read_csv(r'{0}/testInput.csv'.format(sys.path[0]),low_memory=False)

    bowler_stats=pd.DataFrame()
    bowler_stats = bowler_stats.append(df)

    #-----------Wicket Stats--------------------------------------------------
    bowler_stats=bowler_stats.groupby(['match_id','bowler','batting_team'],as_index=False)[['player_dismissed']].count()
    bowler_stats=bowler_stats.groupby(['bowler','batting_team'],as_index=False)[['player_dismissed']].mean()
    bowler_stats['player_dismissed']=bowler_stats['player_dismissed'].astype(int)


    #-----------No of overs----------------------------------------------------
    over=df.groupby(['match_id','bowler','batting_team'],as_index=False)[['ball']].size().reset_index(name='index')
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
    
    bowler_stats = bowler_stats.groupby(['bowler'],as_index=False)[['economy']].mean().round(decimals=2)
    
    return (bowler_stats.loc[bowler_stats['bowler']==bowler_name].values[0][1])
strike_rate()
