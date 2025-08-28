#.ipynb file

import pandas as pd
#!!!!attention if delimeter is ',' or ';'
df = pd.read_csv('bank2.csv', sep=';', quotechar='"', engine='python')

#import csv

#print(df.head())
print(len(df))
# 195 rows

#lets delete columns and some rows
df_1 = df.drop(df.columns[[0, 1]], axis=1)
df_2 = df_1.iloc[:,:-4]
df_3 = df_2.iloc[:,:-2]
df_4 = df_3.drop(['ColName1'], axis=1)
df_d = df_4
#print(df_d.columns)

#lets drop rows
print(df_d['ColName2'].unique())
df_d1 = df_d.iloc[4:]

#what type is date
print(df_d1['Date'].dtype)

#lets filter needed dates - at the moment they are objects
#dates = ["", "2025-11-01", "2025-12-31"]
#df_filtered = df_d1[df_d1['Date'].isin(dates)]

#lets delete some places which costs we don't need
mask_place1 = df_d1['ColName2'].str.contains('name town|name|area', case=False, na=False)
df_clean = df_d1[~mask_place1]
mask_place2= df_clean['ColName2'].str.contains('name town|name', case=False, na=False)
df_clean2 = df_clean[~mask_place2]
df_f2= df_clean2.iloc[:-1]
print(len(df_f))
display(df_f)


#new order of columns
new_order = ['Date','Beneficiary','Sum','Currency','Explanation']
df_f['Explanation'] = ''

#lets write new file:
df_f = df_f[new_order]
df_f.to_csv('bank2_cleaned.csv', index=False)
