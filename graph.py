import matplotlib.pyplot as plt 
from preprocess import data

a = data()
a = a.sort_values(by=['wickets'])
a = a.groupby(['wickets'],as_index=False)[['total_runs']].mean()

plt.scatter(a['wickets'],a['total_runs'])
plt.show()
