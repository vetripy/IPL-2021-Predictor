import pandas as pd 
import os

df=pd.read_csv(r'{0}/all_matches.csv'.format(os.path.dirname(os.path.abspath(__file__))),low_memory=False)
beta_df=pd.DataFrame()
run=pd.DataFrame()
new=pd.DataFrame()
for id in df[['match_id']]:
    new=df.loc[df['match_id']==id]
    new = new.loc[new['ball']<=5.6]
    run=new.groupby(['innings'])[['runs_off_bat','extras','wides','noballs','byes','legbyes']].sum()
    run['totalscore']=run['runs_off_bat']+run['wides']+run['noballs']+run['byes']+run['legbyes']
    if id==335982:
        beta_df=run
    else:
        beta_df=pd.concat([beta_df,run])
print(beta_df)
