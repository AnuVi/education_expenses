import pandas as pd

df1 = pd.read_csv('bank1.csv')
df2 = pd.read_csv('bank2.csv')
  
# combining two files together
df_combined = pd.concat([df1, df2], ignore_index=True)

# adding new column - Category
df_combined['Category'] = ''

# lets save the file
df_combined.to_csv('costs.csv', index=False)


