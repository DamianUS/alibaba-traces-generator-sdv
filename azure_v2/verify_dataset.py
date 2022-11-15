import pandas as pd

month_df = pd.read_csv('data/vm_cpu_readings_month_aggregated_cpu_mem.csv', header=None)

print (month_df[month_df.columns[0]].diff()[month_df[month_df.columns[0]].diff()==300])