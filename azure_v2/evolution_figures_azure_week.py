import matplotlib.pyplot as plt
import numpy as np

directory_name = 'experiments/'
ori_data = np.loadtxt(directory_name+'vm_cpu_readings_week1_aggregated_cpu_mem.csv', delimiter=",", skiprows=0)
print(ori_data)
#ori_data = ori_data.drop(ori_data.columns[[0]], axis=1)
seq_len = len(ori_data[:, 0])

column_names = ['cpu_usage', 'assigned_mem']
for column_name in column_names:
    index = column_names.index(column_name)
    column_data = ori_data[:, index+1]
    axis = [0, seq_len, np.amin(column_data), np.amax(column_data)]
    plt.rcParams["figure.figsize"] = (18, 3)
    f, ax = plt.subplots(1)
    plt.plot(column_data, c="blue", label="Original data", linewidth=1)
    plt.axis(axis)
    plt.title(column_name)
    plt.xlabel('time')
    plt.ylabel(column_name)
    ax.legend()
    plt.savefig(directory_name+column_name+'_week1.png')
    plt.close()