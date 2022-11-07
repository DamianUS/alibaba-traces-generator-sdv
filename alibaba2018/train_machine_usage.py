import pandas as pd
from sdv.timeseries import PAR
import os
from datetime import datetime
import collections

def save_sample_to_csv(generated_sample, file_name):
    generated_sample.to_csv(file_name, header=False, index=False)

data = pd.read_csv("data/machine_usage/machine_usage_grouped_days_3-4-5-6.csv")
field_types = {
    "cpu": {
        "type": "numerical",
        'subtype': 'float'
    },
    "mem": {
        "type": "numerical",
        'subtype': 'float'
    },
    "net_in": {
        "type": "numerical",
        'subtype': 'float'
    },
    "net_out": {
        "type": "numerical",
        'subtype': 'float'
    }
}

Parameters = collections.namedtuple('Parameters','iteration sample_size data_name seq_len ')
experiment_parameters = Parameters(iteration=500, sample_size=1, data_name='alibaba2018', seq_len=8640)

model = PAR(
    field_types=field_types,
    epochs=experiment_parameters.iteration,
    sample_size=experiment_parameters.sample_size,
    verbose=True,
)


model.fit(data)
experiment_root_directory_name = "experiments/" + experiment_parameters.data_name + '_epochs-' + str(experiment_parameters.iteration) + '-' + datetime.now().strftime("%j-%Y-%H-%M") + "/"
generated_data_directory_name = experiment_root_directory_name + "generated_data/"
os.makedirs(generated_data_directory_name, exist_ok=True)
parameters_text_file = open(experiment_root_directory_name + "parameters.txt", "w")
parameters_text_file.write(repr(experiment_parameters))
parameters_text_file.write(repr(model.get_metadata().to_dict()))

metrics_text_file = open(experiment_root_directory_name + "metrics.txt", "w")
metrics_text_file.write('no hay métricas')


for i in range(150):
    generated_sample = model.sample(sequence_length=experiment_parameters.seq_len)
    save_sample_to_csv(generated_sample, generated_data_directory_name+"sample_"+ str(i) +".csv")
