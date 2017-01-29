import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
print(s)
print('\n')

dates = pd.date_range('20170101',periods=100)
print(dates)
print('\n')

col_name = ['A', 'B', 'C', 'D']
df = pd.DataFrame(np.random.randn(100,4),index=dates,columns=col_name)
print(df)
print(df.head())
print(df.tail(3))
print(df.describe())
print('\n')

df = pd.DataFrame(np.random.randn(100,4),index=dates,columns=col_name)
df = df.cumsum()
plt.figure()
df.plot()
plt.legend(loc='best')
print('\n')

df.to_csv('foo.csv')

print(pd.read_csv('foo.csv'))

