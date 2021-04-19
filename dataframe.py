import pandas as pd 
df=pd.read_csv('all_matches.csv',low_memory=False)

new=df.loc[df['match_id']==335982]
print(new[['match_id','season','start_date','venue']].head(11))
run=new.groupby(['innings'])['runs_off_bat','extras','wides','noballs','byes','legbyes'].sum()
run['totalscore']=run['runs_off_bat']+run['wides']+run['noballs']+run['byes']+run['legbyes']
print(run)