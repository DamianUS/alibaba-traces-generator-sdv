import pandas as pd
import datetime


#start_date = datetime.datetime(2022, 1, 1)


df = pd.read_csv('data/machine_usage/machine_usage_cut_days_3_4_5_6.csv')
df = df.drop(df.columns[[0,4,5]], axis=1) #drop machine_id and empty columns
df = df.groupby(df.columns[0]).mean()
#df = df.drop(df.columns[0], axis=1) # eliminar timestamp
df.to_csv('data/machine_usage/machine_usage_grouped_with_timestamp_days_3_4_5_6.csv')