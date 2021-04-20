import matplotlib.pyplot as plt 
import pandas as pd
import os


df = pd.read_csv(r'{0}/csv/second_innings.csv'.format(os.path.dirname(os.path.abspath(__file__))))

df = df.sort_values(by=['target'])

plt.scatter(df['target'],df['srcoe'])

plt.xlabel('Traget in asc order')
plt.ylabel('score in 6 overs')

a = [60 for i in range(817)]
b = pd.DataFrame({
    'col1' : a
})


plt.plot(df['target'],b['col1'])
plt.show()
