import pandas as pd
from sdv.timeseries import PAR
from sdv.metrics.timeseries import TSFClassifierEfficacy

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
    epochs=1,
    verbose=True
)
model.fit(data)
print(model.get_metadata().to_dict())
new_data = model.sample(1)
print(new_data)
print(TSFClassifierEfficacy.compute(data, new_data, field_types, target='makespan'))
