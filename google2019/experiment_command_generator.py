import itertools
import os
import stat
from datetime import datetime

def generate_bash_file(commands, sh_name, trace_name):
    sh_filename = f'experiments_{trace_name}_{sh_name}_{datetime.now().strftime("%j-%Y-%H-%M")}.sh'
    sh_file = open(sh_filename, "w")
    sh_file.writelines(commands)
    st = os.stat(sh_filename)
    os.chmod(sh_filename, st.st_mode | stat.S_IEXEC)

def generate_experiment_command(trace, sample_size, n_samples, seq_len, epochs, experiment_save_dir):
   return f'python train_sdv.py --trace {trace} --sample_size {sample_size} --n_samples {n_samples} --seq_len {seq_len} --epochs {epochs} --experiment_save_dir {experiment_save_dir}\n'

sample_size = [1]
n_samples = [10]
seq_len = [288]
epochs = [10, 100, 500, 1000, 1500, 2000]
parameterization = [sample_size, n_samples, seq_len, epochs]

experiment_save_dir = '~/experiments/sdv/google2019/'
trace = 'google2019'

commands = [generate_experiment_command(trace, sample_size, n_samples, seq_len, epochs, experiment_save_dir) for
            sample_size, n_samples, seq_len, epochs in
            list(itertools.product(*parameterization))]

generate_bash_file(commands,'', trace)