import pandas as pd 
import os




df = pd.read_csv(r'{0}/csv/all_matches.csv'.format(os.path.dirname(os.path.abspath(__file__))),low_memory=False)


def function(matchid,innings):

    new = df.loc[df['match_id']==i]

    total_run = new

    new = new.loc[new['ball']<=5.6]

    new.drop(new[new['innings']>2].index,inplace=True)

    cond = [i for i in new['innings'].unique()]

    if cond!=[1,2]:
        
        return(pd.DataFrame())
    
    else:

        run = new.groupby(['innings'])[['runs_off_bat','extras','wides','noballs','byes','legbyes']].sum()
        total_run = total_run.groupby(['innings'])[['runs_off_bat','extras','wides','noballs','byes','legbyes']].sum()

        total_run = total_run['runs_off_bat']+total_run['wides']+total_run['noballs']+total_run['byes']+total_run['legbyes']

        run['totalscore'] = run['runs_off_bat']+run['wides']+run['noballs']+run['byes']+run['legbyes']

        balls = new.groupby(['runs_off_bat','innings']).size().reset_index(name='counts')

        run['match_id'] = matchid
        
        run['target_score'] = total_run
        
        #DOT-BALL COUNT
        if innings==1:
            run['dot_balls'] = [i for i in balls['counts']][0]
        elif innings==2:
            run['dot_balls'] = [i for i in balls['counts']][1]
            


        #BOUNDARY COUNT
        boundary=balls[(balls.runs_off_bat>=4)]
        boundary=boundary.groupby(['innings']).sum()


        #run.index=boundary.index
        try:
            run['boundary']=boundary['counts'].values
        except Exception:
            run['boundary']=[0,0]


        #------------------------------------------

        try:
            run['innings'] = [1,2]
        except Exception:
            run['innings'] = [1]

        #------------------------------------------
        
        run['wickets'] = new.groupby(['innings'])[['player_dismissed']].count()
        

        return(run[['match_id','innings','target_score','totalscore','wickets','dot_balls','boundary']].loc[run['innings']==innings])
        

ids = [i for i in df['match_id'].unique()]


first_innings = pd.DataFrame()
second_innings=pd.DataFrame()



for i in ids[:1]:
    
    first = function(i,1)
    second = function(i,2)
    
    if first.empty != True and second.empty != True:

        first_innings = first_innings.append(function(i,1))
        
        target_score = first_innings['target_score']
        first_innings.drop('target_score',axis='columns',inplace=True)
        
        second_innings = second_innings.append(function(i,2))
        second_innings.drop('target_score',axis='columns',inplace=True)
        
        second_innings.index = first_innings.index
        second_innings = second_innings.assign(target_score)
        
        #second_innings = second_innings.append(target)
        
        


print(second_innings)
# first_innings = first_innings.reset_index(drop=True)
# second_innings = second_innings.reset_index(drop=True)

# first_innings.to_csv('csv/first_innings.csv')
# second_innings.to_csv('csv/second_innings.csv')
