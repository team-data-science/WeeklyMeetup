import pandas as pd
import datetime as dt


# read dataset
df = pd.read_csv("small.csv", )

# print it and print the types
print(df)
print(df.dtypes)


# turn epoch into a timestamp
df['TimeStamp'] = df['time'].apply(lambda s : dt.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S'))
print(df)


# define the columns we want to keep
#

#filter for these columns and print could also do this as a list: colums_we_want = ['TimeStamp','Dishwasher [kW]','Furnace 1 [kW]','Microwave [kW]']
df_filter = df.filter(items = ['TimeStamp','Dishwasher [kW]','Furnace 1 [kW]','Microwave [kW]'] )
print(df_filter)


# add a column with a predefined value and print
df_filter["House_ID"] = 1
print(df_filter)


# turn the columns and values into variable and value column
df_melted = df_filter.melt(id_vars = ['TimeStamp','House_ID'])
print(df_melted)


