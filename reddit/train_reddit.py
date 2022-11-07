import pandas as pd
from sdv.timeseries import PAR
import os
from datetime import datetime
import collections



def save_sample_to_csv(generated_sample, file_name):
    generated_sample.to_csv(file_name, header=False, index=False)

data = pd.read_csv("data/LoadReddit-60minutes-2015-01.csv")
print(data.head())
for col in data.columns:
    print(col)

field_types = {
    "timestamp": {
        "type": "datetime",
        "format": "%Y-%m-%d %H:%M:%S"
    },
    "interactions": {
        "type": "numerical",
        'subtype': 'integer'
    }
}
Parameters = collections.namedtuple('Parameters','iteration sample_size data_name n_samples seq_len')
iteration=10000
sample_size=1
data_name='reddit2015'
seq_len=24*7
n_samples=10
experiment_parameters = Parameters(iteration=iteration, sample_size=sample_size, data_name=data_name, n_samples=n_samples, seq_len=seq_len)

model = PAR(
    field_types=field_types,
    epochs=experiment_parameters.iteration,
    sample_size=experiment_parameters.sample_size,
    verbose=True,
    sequence_index='timestamp'
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

for i in range(n_samples):
    generated_sample = model.sample(sequence_length=experiment_parameters.seq_len)
    save_sample_to_csv(generated_sample.drop(['timestamp'], axis=1), generated_data_directory_name+"sample_"+ str(i) +".csv")


# print(TSFClassifierEfficacy.compute(data, new_data, field_types, target='avg_cpu'))

