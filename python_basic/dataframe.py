import pandas as pd

data = {'name': ['wangdachui', 'Linling', 'Niuyun'], 'pay': [4000, 5000, 6000]}
labels = ['a', 'b', 'c']
df = pd.DataFrame(data, index=labels)
print(df['name'])
