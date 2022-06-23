import pandas as pd
import numpy as np

# dict1 = {
#     "name":['abhay','rohan','skillf','shubh'],
#     "marks":[56,44,45,34],
#     "city":['a','b','c','d']
# }
# df = pd.DataFrame(dict1)
# df.to_csv('file1.csv')
# df.to_csv('file2.csv',index=False)
# print(df.head(2))
# print(df.tail(2))
# print(df.describe())
df = pd.read_csv('file3.csv')
print(df)
print()
a = df.station
# a[0] = 90
# print(df)
# df.to_csv("updated_file3.cs")
# df.index = ["first","second","third","fourth"]
# print(df)

#PANDAS HAS TWO TYPES OF DATASTRUCTURE

# SERIES - It's a one dimenional array with indexes, it stores a single column or row of data in a dataframe
# DATAFRAME - it's a tabular spreadsheet like structure  representing rows each of which containes one or multiple 
# columns

# a one dimesional array capable of holding  any type of data -series
# a two dimesional data (labeled) strucuture with colummns o potentially different types of data - dataframe

# ser = pd.Series(np.random.rand(34))
# print(type(ser))

# newdf = pd.DataFrame(np.random.rand(334,5), index=np.arange(334))
# print(newdf.head(5))
# print(type(newdf))
# print(newdf.dtypes)
# newdf[0][0] = "abhay"
# print(newdf.dtypes)
# print(newdf.head())
# print(newdf.index)
# print(newdf.columns)
# b = newdf.to_numpy()
# print(b)
# newdf[0][0] = 0.3
# print(newdf.head())
# print(newdf.T)
# print(newdf.sort_index(axis=0,ascending=False))
# print(newdf.sort_index(axis=1,ascending=False))

# newdf2 = newdf
# newdf2[0][0] =458
# print(newdf)

# newdf.loc[0,0] = 245
# print(newdf.head(2))
# newdf.columns = list("ABCDE")
# print(newdf)
# newdf.loc[0,'A'] = 66
# print(newdf.loc[[1,2],['C','D']])
# print(newdf.loc[:,['C','D']])
# print(newdf.loc[[1,2],:])
# print(newdf)

# c = newdf.loc[(newdf['A']<0.3) & (newdf['c']>0.1)]
# print(c)

# d = newdf.iloc[0,4]
# print(d)

# e = newdf.iloc[[0,5],[1,2]]
# print(e)

# f= newdf.drop([0])
# f= newdf.drop(['A','C'],axis = 1, inplace=True)
# print(f)
# g = newdf.reset_index(drop=True)
# print(g)
# h = newdf['B'].isnull()
# print(h)
# i = newdf['B'] = None
# print(newdf['B'].isnull())
# print(newdf)

# df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Alfred'],
#                    "toy": [np.nan, np.nan, np.nan],
#                    "born": [pd.NaT, pd.Timestamp("1940-04-25"),
#                             pd.NaT]})

# print(df.dropna(how='all',axis = 1))
# print(df.drop_duplicates(subset=['name'],keep='first'))
# print(df.drop_duplicates(subset=['name'],keep='last'))
# print(df.drop_duplicates(subset=['name'],keep=False))
# print(df.shape)
# print(df.info())
# print(df['name'].value_counts(dropna=False))
# print(df.notnull())