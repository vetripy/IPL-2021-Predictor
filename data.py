import pandas as pd 
import os




df = pd.read_csv(r'{0}/all_matches.csv'.format(os.path.dirname(os.path.abspath(__file__))),low_memory=False)


def function(matchid,innings):

    new = df.loc[df['match_id']==i]
    new = new.loc[new['ball']<=5.6]

    new.drop(new[new['innings']>2].index,inplace=True)

    cond = [i for i in new['innings'].unique()]

    if cond!=[1,2]:
        
        return(pd.DataFrame())
    
    else:

        run = new.groupby(['innings'])[['runs_off_bat','extras','wides','noballs','byes','legbyes']].sum()

        run['totalscore'] = run['runs_off_bat']+run['wides']+run['noballs']+run['byes']+run['legbyes']

        balls = new.groupby(['runs_off_bat','innings']).size().reset_index(name='counts')
        

        count_balls = balls['counts']
        #DOT-BALL COUNT
        if innings==1:
            run['dot_balls'] = [i for i in balls['counts']][0]
        elif innings==2:
            run['dot_balls'] = [i for i in balls['counts']][1]
        #BOUNDARY COUNT
        boundary=balls[(balls.runs_off_bat>=4)]
        boundary=boundary.groupby(['innings']).sum()
        run.index=boundary.index
        run['boundary']=boundary['counts'].values
        #------------------------------------------
        try:
            run['innings'] = [1,2]
        except Exception:
            run['innings'] = [1]
        
        run['wickets'] = new.groupby(['innings'])[['player_dismissed']].count()
        
        
                
        

        return(run[['innings','totalscore','wickets','dot_balls','boundary']].loc[run['innings']==innings])


ids = [i for i in df['match_id'].unique()]


first_innings = pd.DataFrame()
second_innings=pd.DataFrame()



for i in ids[:10]:
    
    first = function(i,1)
    second = function(i,2)
    if first.empty != True and second.empty != True:
        first_innings = first_innings.append(function(i,1))
        
        second_innings = second_innings.append(function(i,2))
        second_innings.index=first_innings.index
        second_innings['target_score']=first_innings['totalscore'].values

        
print(first_innings)
print(second_innings)
#second_innings.to_csv('second_innings.csv')
