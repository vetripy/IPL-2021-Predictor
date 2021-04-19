import pandas as pd 
import os


def function(matchid,innings):
    
    df = pd.read_csv(r'{0}/all_matches.csv'.format(os.path.dirname(os.path.abspath(__file__))),low_memory=False)
    

    new = df.loc[df['match_id']==matchid]
    new = new.loc[new['ball']<=5.6]

    run = new.groupby(['innings'])[['runs_off_bat','extras','wides','noballs','byes','legbyes']].sum()

    run['totalscore'] = run['runs_off_bat']+run['wides']+run['noballs']+run['byes']+run['legbyes']


    run['innings'] = [1,2]

    run['wickets'] = new.groupby(['innings'])[['player_dismissed']].count()


    return(run.loc[run['innings']==innings])


id = 335982

a = function(id,1)

innings,score,wickets = [i for i in a['innings']],[i for i in a['totalscore']],[i for i in a['wickets']]

print(innings,score,wickets)





#run = pd.DataFrame()
#new = pd.DataFrame()







# for id in range(10):
#     new=df.loc[df[['match_id']]]]
#     new = new.loc[new['ball']<=5.6]
#     run=new.groupby(['innings'])[['runs_off_bat','extras','wides','noballs','byes','legbyes']].sum()
#     run['totalscore']=run['runs_off_bat']+run['wides']+run['noballs']+run['byes']+run['legbyes']
#     if id==0:
#         beta_df=run
#     else:
#         beta_df=pd.concat([beta_df,run])
# print(beta_df)
