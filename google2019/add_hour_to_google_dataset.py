from datetime import datetime, timedelta
import pandas as pd


#To start_time for a datetime due to bug: https://github.com/sdv-dev/SDV/issues/943
start_date = datetime(2019, 1, 1)

directory = 'data/week1/'
week_df = pd.read_csv(directory+'instance_usage_5min_sample_week1.csv')
next_date = start_date
sequence_length = week_df.shape[0]
print(sequence_length)
hours = []
for i in range (sequence_length):
    hours.append(next_date.hour)
    next_date = next_date + timedelta(minutes=5)

week_df.insert(0,'hour', hours)
week_df.to_csv(directory+'instance_usage_5min_sample_week1_with_hour.csv', header=True, index=False)

