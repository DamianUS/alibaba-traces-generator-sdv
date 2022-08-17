# Alibaba batch_task trace file generator

This repo has two main purposes:
1. **preprocess.py**: Pre-process the raw Alibaba cluster trace 2018 batch_task.csv (can be downloaded here http://clusterdata2018pubcn.oss-cn-beijing.aliyuncs.com/batch_task.tar.gz) (more info about the schema and data can be found here https://github.com/alibaba/clusterdata/blob/master/cluster-trace-v2018/trace_2018.md) with the following transformations:
    1. Discard all the tasks with Status != Terminated.
    2. Discard all the tasks from the first day (<=86400s).
    3. Discard all the tasks with end_time 0.
    4. Create a new column makespan such as: end_time - start time.
    5. Remove task name (simplest version without DAG information), status, end time, task type, and job name to reduce the file size and supposedly the memory consumption and training time.
    6. Order by start time.
    7. Transform the start_time from intenger values representing the seconds from the start of the trace to a datetime value such as: 2022-01-01 00:00:00 + start_time seconds. This column is formatted (in Python style): "%Y-%m-%d %H:%M:%S".
2. **train.py**: Train an SDV PAR model (https://sdv.dev/SDV/user_guides/timeseries/par.html).

# Requirements

1. Python 3.8.
2. SDV 0.16.
3. Pandas.

# How to use

1. Download the Alibaba 2018 cluster trace batch_task.csv file (http://clusterdata2018pubcn.oss-cn-beijing.aliyuncs.com/batch_task.tar.gz) and uncompress/paste it in the repository's **data** folder (the name must be **batch_task.csv**).
2. Insert the following line as header of the csv file: task_name,instance_num,job_name,task_type,status,start_time,end_time,plan_cpu,plan_mem
3. Run the **preprocess.py**, which will create a file **processed_batch_task.csv** in the **data** folder.
4. Tune the parameters for the training in **train.py** (if needed) and run it.

# Pre-process Result

The result of the pre-process is this file (8 days): https://uses0-my.sharepoint.com/:u:/g/personal/afdez_us_es/ESv9EOxfeG1Nq-9pdhN53P4BwMBLDWkKToBoMMX-D2nKFw?e=f7hidL
