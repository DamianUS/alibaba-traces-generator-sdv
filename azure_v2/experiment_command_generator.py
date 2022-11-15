import itertools
import os
import stat
from datetime import datetime


def generate_experiment_command(ori_data_filename, trace, sample_size, n_samples, seq_len, epochs, ):
    return f'python train_azure2019.py --ori_data_filename {ori_data_filename} --trace {trace} --sample_size {sample_size} --n_samples {n_samples} --seq_len {seq_len} --epochs {epochs}\n'


ori_data_filename = ['data/vm_cpu_readings_month_aggregated_cpu_mem_no_timestamp.csv']
trace = ['azure_v2']
sample_size = [5]
n_samples = [100]
seq_len = [2016]
epochs = [10, 50, 100]

parameterization = [ori_data_filename, trace, sample_size, n_samples, seq_len, epochs]

commands = [generate_experiment_command(ori_data_filename, trace, sample_size, n_samples, seq_len, epochs) for
            ori_data_filename, trace, sample_size, n_samples, seq_len, epochs in
            list(itertools.product(*parameterization))]

sh_filename = "experiments" + '-' + datetime.now().strftime("%j-%Y-%H-%M") + ".sh"
sh_file = open(sh_filename, "w")
sh_file.writelines(commands)
st = os.stat(sh_filename)
os.chmod(sh_filename, st.st_mode | stat.S_IEXEC)
