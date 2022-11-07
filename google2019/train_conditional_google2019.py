import pandas as pd
from sdv.timeseries import PAR
import os
from datetime import datetime
import collections



def save_sample_to_csv(generated_sample, file_name):
    generated_sample.to_csv(file_name, header=False, index=False)

data = pd.read_csv("data/week1/instance_usage_5min_sample_week1_with_hour.csv")

field_types = {
    "hour": {
        "type": "numerical",
        'subtype': 'integer'
    },
    "avg_cpu": {
        "type": "numerical",
        'subtype': 'float'
    },
    "avg_mem": {
        "type": "numerical",
        "subtype": 'float'
    },
    "avg_assigned_mem": {
        "type": "numerical",
        'subtype': 'float'
    },
    "avg_cycles_per_instruction": {
        "type": "numerical",
        'subtype': 'float'
    }
}
Parameters = collections.namedtuple('Parameters','iteration sample_size segment_size, data_name seq_len')
experiment_parameters = Parameters(iteration=10, sample_size=1, segment_size=12, data_name='google2019', seq_len=288)

model = PAR(
    field_types=field_types,
    epochs=experiment_parameters.iteration,
    sample_size=experiment_parameters.sample_size,
    verbose=True,
    entity_columns=['hour'],
    segment_size=experiment_parameters.segment_size
)


model.fit(data)
experiment_root_directory_name = "experiments/" + 'google2019' + '_epochs-' + str(experiment_parameters.iteration) + '-' + datetime.now().strftime("%j-%Y-%H-%M") + "/"
generated_data_directory_name = experiment_root_directory_name + "generated_data/"
os.makedirs(generated_data_directory_name, exist_ok=True)
parameters_text_file = open(experiment_root_directory_name + "parameters.txt", "w")
parameters_text_file.write(repr(experiment_parameters))
parameters_text_file.write(repr(model.get_metadata().to_dict()))

metrics_text_file = open(experiment_root_directory_name + "metrics.txt", "w")
metrics_text_file.write('no hay métricas')



context = pd.DataFrame([{'hour': 13}])
for i in range(10):
    generated_sample = model.sample(sequence_length=experiment_parameters.segment_size, context=context)
    save_sample_to_csv(generated_sample, generated_data_directory_name+"conditioned_sample_" + str(i) +".csv")


# print(TSFClassifierEfficacy.compute(data, new_data, field_types, target='avg_cpu'))

