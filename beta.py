import pandas as pd 
import os
df = pd.read_csv(r'{0}/all_matches.csv'.format(os.path.dirname(os.path.abspath(__file__))),low_memory=False)

def function(matchid,innings):
    
    
    
    
    new = df.loc[df['match_id']==matchid]
    new = new.loc[new['ball']<=5.6]
    
    run = new.groupby(['innings'])[['runs_off_bat','extras','wides','noballs','byes','legbyes']].sum()
    run['match_id']=matchid
    run['totalscore'] = run['runs_off_bat']+run['wides']+run['noballs']+run['byes']+run['legbyes']
    

    run['innings'] = [1,2]

    run['wickets'] = new.groupby(['innings'])[['player_dismissed']].count()


    return(run.loc[run['innings']==innings])


id=392180
beta_df=pd.DataFrame()
beta_df= function(id,1)
id+=1
while(id<=392189):
    beta_df=beta_df.append(function(id,1))
    beta_df=beta_df[['match_id','innings','totalscore','wickets']]  
    id+=1
        
#innings,score,wickets = [i for i in a['innings']],[i for i in a['totalscore']],[i for i in a['wickets']]

print(beta_df)





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
