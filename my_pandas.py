#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

s = pd.Series()
print(s)    #prints an empty series

data = np.array(['a','b','c','d'])
t = pd.Series(data)
print(t)    #prints a series with the data

data1 = {'a' : 0., 'b' : 1., 'c' : 2.}
u = pd.Series(data1)
print(u)    #prints a series with the data