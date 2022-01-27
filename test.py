import pandas as pd
print(f'pandas version: {pd.__version__}')

df = pd.read_excel(r'Book.xlsx')
df.to_excel('test.xlsx')
print(pd)