import pandas as pd
from sdv.timeseries import PAR

data = pd.read_csv("data/processed_batch_task.csv")
sequence_index = 'start_time'
field_types = {
    "instance_num": {
        "type": "numerical",
        'subtype': 'integer'
    },
    "start_time": {
        "type": "datetime",
        "format": "%Y-%m-%d %H:%M:%S"
    },
    "plan_cpu": {
        "type": "numerical",
        'subtype': 'float'
    },
    "plan_mem": {
        "type": "numerical",
        'subtype': 'float'
    },
    "makespan": {
        "type": "numerical",
        'subtype': 'integer'
    },
}
model = PAR(
    sequence_index=sequence_index,
    field_types=field_types,
    segment_size=20,
    epochs=10,
    verbose=True,
    cuda=False
)
print ("Before fit")
model.fit(data)
print("After fit")
print(model.get_metadata().to_dict())
print(new_data)
#print(TSFClassifierEfficacy.compute(data, new_data, field_types, target='makespan'))



experiment_root_directory_name = "experiments/" + 'alibaba2018'
generated_data_directory_name = experiment_root_directory_name + "generated_data/"
os.makedirs(generated_data_directory_name, exist_ok=True)


for i in range(150):
    generated_sample = model.sample(1)
    save_sample_to_csv(generated_sample, generated_data_directory_name+"sample_"+ str(i) +".csv")

