import matplotlib.pyplot as plt 
from preprocess import strike_rate

a = strike_rate()
a = a.sort_values(by=['strike_rate'])
a = a.groupby(['striker'],as_index=False)[['strike_rate','runs_off_bat']].mean()

#plt.plot(a['strike_rate'],a['runs_off_bat'])
#plt.show()
print(a)