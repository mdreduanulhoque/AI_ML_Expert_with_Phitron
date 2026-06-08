import pandas as pd

df = pd.DataFrame({'num': [1,2,3,4]})

df['sq. num'] = df['num'].apply(lambda x: x*x)
print(df)