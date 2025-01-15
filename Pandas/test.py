import pandas as pd
import numpy as np

df = pd.DataFrame([[1, 2]], columns= ['A', 'B'])
s = df['A'].unique()
print(s)