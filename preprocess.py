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

    return(data_file)


def strike_rate():

    #--------Opening the input dataframe and store it as df-----------------
    df = pd.read_csv(r'{0}/testInput.csv'.format(sys.path[0]),low_memory=False)

    #--------Changing the all the balls to 1 to count it easier--------------   
    one = [1 for i in range(len(df))]
    df['ball'] = one

    #--------Grouping the batsmen with their strike rate all the bowlers-----
    strike = df.groupby(['match_id','striker','bowler'],as_index=False)[['runs_off_bat','ball']].sum()
    

    #--------Calculating the strike rate and adding them to the dataframe----
    strike['strike_rate'] = strike['runs_off_bat']/strike['ball']
    strike['strike_rate'] = strike['strike_rate']*100
    strike['strike_rate'] = strike['strike_rate'].round(decimals=2)

    #--------Removing used columns and reseting the index--------------------
    strike = strike.drop(columns=['ball','runs_off_bat'])
    
    #--------Average strike rate of batsmen-----------------------------------
    #strike = strike.groupby(['striker','bowler'],as_index=False)[['strike_rate']].mean().round(decimals=2)
    
    
    return(strike)


def bowling_stats():

    #--------Opening the input dataframe and store it as df-----------------
    df = pd.read_csv(r'{0}/testInput.csv'.format(sys.path[0]),low_memory=False)
    df=df.loc[df['ball']<=5.6]
    df=df.loc[df['innings']<=2]
    economy=pd.DataFrame()
    

   


    #-----------No of overs----------------------------------------------------
    over=df.groupby(['match_id','bowler','batting_team','innings'],as_index=False)[['ball']].size()
    #over=over.groupby(['match_id','bowler','batting_team'],as_index=False)[['index']].sum()
    over['overs']=over['size']//6
    over=over.drop(columns=['size'])

    #-----------Economy Stats---------------------------------------------------
    economy=df.groupby(['match_id','bowler','batting_team','innings'],as_index=False)[['runs_off_bat','extras']].sum()
    economy['economy']=economy['runs_off_bat']+economy['extras']
    economy = economy.drop(columns=['runs_off_bat','extras'])
    #economy=economy.groupby(['match_id','bowler','batting_team'],as_index=False)[['economy']].sum()
    economy['economy']=economy['economy'].div(over['overs'].values)
    
    economy['overs']=over['overs'].values

    economy['economy']=economy['economy'].round(decimals=0)
    economy['overs']=economy['overs'].round(decimals=0)
    economy = economy.drop(columns=['overs'])
    economy=economy.loc[economy['economy']!=float('inf')]
    
    return(economy)


