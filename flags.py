import pandas as pd 
import os

df = pd.read_csv(r'{0}/all_matches.csv'.format(os.path.dirname(os.path.abspath(__file__))),low_memory=False)
flag=pd.DataFrame()
df['count']=1

