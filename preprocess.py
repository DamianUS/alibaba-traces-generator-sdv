import csv
import pandas as pd
import datetime

#To start_time for a datetime due to bug: https://github.com/sdv-dev/SDV/issues/943
start_date = datetime.datetime(2022, 1, 1)

raw_dataset = pd.read_csv("data/batch_task.csv")
filtered_dataset = raw_dataset[(raw_dataset['start_time'] > 86400) & (raw_dataset['end_time'] > 0) & (raw_dataset['status'] == 'Terminated')]
filtered_dataset['makespan'] = filtered_dataset.apply(lambda row: row['end_time'] - row['start_time'], axis=1)
trimmed_dataset = filtered_dataset.drop(columns=['task_name', 'status', 'end_time', 'task_type', 'job_name'])
sorted_dataset = trimmed_dataset.sort_values(by=['start_time'])
sorted_dataset['start_time'] = sorted_dataset.apply(lambda row: start_date+datetime.timedelta(seconds=row['start_time']), axis=1)
sorted_dataset.to_csv('data/processed_batch_task.csv', index=False)
