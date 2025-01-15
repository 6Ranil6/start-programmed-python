import numpy as np
from datetime import date, timedelta
np.random.seed(33)
dates = list(map(str,[date(2019, 1, 4) + timedelta(days=i) for i in range(360)]))
temperatures = np.random.randint(-10, 35, len(dates))

import pandas as pd
s = pd.Series(temperatures, dates)
month = int(input())
if month < 10:
    month = f'0{month}'
else:
    month = f'{month}'
conditions = []
for index in s.index:
    print(index.startswith('2019-{month}'))
    if index.startswith('2019-{month}'):
        conditions.append(True)
    else:
        conditions.append(False)
print(conditions)
print(s[conditions])