import pandas as pd
import numpy as np

# s = pd.Series([10,12,8,14], index=['a', 'b', 'c', 'd'])
# print(s)
# data ={'Kraj':['Belgia', 'Indie', 'Brazylia'],
#        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#        'Populacja': [11190846, 1303171035, 207847528]}
# df = pd.DataFrame(data)
# print(df)
# print()
# print(s['c'])
# print(s.c)
# print()
#
#
# print(df[0:1])
# print()
#
# print(df['Populacja'])
# print(df.iloc[0,0])
# print(df.loc[0, 'Kraj'])
# print()
# print(df.at[0, "Kraj"])
# print()
# print(df.loc[0])
#
# print()
# print()
# print("kraj: " + df.Kraj)
# print()
#
# print(df.sample())
#
# print(df.sample(2))
# print(df.sample(frac=0.5))
# print(df.sample(n=10, replace=True))
# print()
# print(df.head())
# print()
# print(df.head(2))
# print(df.tail(1))
# print(df.describe())
# print(df.T)

# print(s[(s>9)])
# print(s.where(s > 10))
#
# print(s.where(s > 10, 'za duże'))
#
#
# seria = s.copy()
# seria.where(s > 10, 'za duże', inplace=True)
# print('###############')
# print(seria)
#
# print()
# print(s[~(s > 10)])
#
# print()
# print(s[(s < 13) & (s > 8)])
#
# print(df[df['Populacja']>120000000])
# print(df[(df.Populacja>1000000) & (df.index.isin([0,2]))])
#
# print()
# print("#############")
# szukaj = ['Belgia', 'Brazylia']
# print(df.isin(szukaj))

# s['e'] = 15
# print(s.e)
# s['f'] = 16
# print(s)
#
# df.loc[3] = 'dodane'
# print(df)
#
# df.loc[4] = ['Polska', "Warszawa", 38675467]
# print(df)
#
# print()
# new_df = df.drop([3])
# print(new_df)
#
# df.drop([3],inplace=True)
# print(df)
#
#
# # df.drop('Kraj', axis=1, inplace=True)
# print(df)
#
#
# print()
# df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
# print(df)
#
# print()
# print(df.sort_values('Kraj'))
# grouped = df.groupby(['Kontynent'])
# print(grouped.get_group(('Europa')))
#
# print(df.groupby(['Kontynent']).agg({'Populacja': ['sum']}))

ramka_danych = pd.read_csv('iris.data', sep=',', header=None, decimal='.')
print(ramka_danych.to_string())
ramka_danych[0:5].to_csv('nowe_dane.csv', index=False, header=False)



dane_z_excela = pd.read_excel('Financial Sample.xlsx', sheet_name=0)
print(dane_z_excela)
dane_z_excela[0:5].to_excel('przykladowyExcel.xlsx', index=False, header=False)



