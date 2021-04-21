import matplotlib.pyplot as plt 
import pandas as pd
import os


df = pd.read_csv(r'{0}/csv/second_innings.csv'.format(os.path.dirname(os.path.abspath(__file__))))

df = df.groupby(['dot_balls'])[['dot_balls','srcoe']].mean()

a = df.groupby(['dot_balls'])['srcoe'].mean()



plt.scatter(a.index,a)


plt.show()
