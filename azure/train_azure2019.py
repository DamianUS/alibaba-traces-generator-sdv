import argparse

import pandas as pd
from sdv.timeseries import PAR
import os
from datetime import datetime
import collections



def save_sample_to_csv(generated_sample, file_name):
    generated_sample.to_csv(file_name, header=False, index=False)


def initialize(trace):
    if (args.trace == 'alibaba2018'):
        dataset_info = {
            "timestamp_frequency_secs": 10,
            "column_config": {
                "cpu": {
                    "column_index": 0,
                    "y_axis_min": 0,
                    "y_axis_max": 100
                },
                "mem": {
                    "column_index": 1,
                    "y_axis_min": 0,
                    "y_axis_max": 100
                },
                "net_in": {
                    "column_index": 2,
                    "y_axis_min": 0,
                    "y_axis_max": 100
                },
                "net_out": {
                    "column_index": 3,
                    "y_axis_min": 0,
                    "y_axis_max": 100
                }
            }
        }
    elif (args.trace == 'google2019'):
        dataset_info = {
            "timestamp_frequency_secs": 300,
            "column_config": {
                "cpu": {
                    "column_index": 0,
                    "y_axis_min": 0,
                    "y_axis_max": 1
                },
                "mem": {
                    "column_index": 1,
                    "y_axis_min": 0,
                    "y_axis_max": 1
                },
                "assigned_mem": {
                    "column_index": 2,
                    "y_axis_min": 0,
                    "y_axis_max": 1
                },
                "cycles_per_instruction": {
                    "column_index": 3
                }
            }
        }
    elif (args.trace == 'azure_v2'):
        dataset_info = {
            "timestamp_frequency_secs": 300,
            "column_config": {
                "cpu_total": {
                    "column_index": 0
                },
                "mem_total": {
                    "column_index": 1
                }
            }
        }
    elif (args.trace == 'reddit'):
        dataset_info = {
            "timestamp_frequency_secs": 3600,
            "column_config": {
                "interactions": {
                    "column_index": 0
                }
            }
        }

    return dataset_info


def main(args):
    dataset_info = initialize(args.trace)
    data = pd.read_csv(args.ori_data_filename, names=dataset_info['column_config'].keys())


    field_types = {
        "cpu_total": {
            "type": "numerical",
            'subtype': 'float'
        },
        "mem_total": {
            "type": "numerical",
            "subtype": 'float'
        }
    }
    Namespace = collections.namedtuple('Parameters', 'iteration sample_size n_samples data_name seq_len ')
    experiment_parameters = Namespace(iteration=args.epochs, sample_size=args.sample_size, n_samples=args.n_samples, data_name=args.trace, seq_len=args.seq_len )

    model = PAR(
        field_types=field_types,
        epochs=experiment_parameters.iteration,
        sample_size=experiment_parameters.sample_size,
        verbose=True,
    )

    model.fit(data)
    experiment_root_directory_name = "experiments/" + experiment_parameters.data_name + '_epochs-' + str(experiment_parameters.iteration) + '-' + datetime.now().strftime("%j-%Y-%H-%M") + "/"
    generated_data_directory_name = experiment_root_directory_name + "generated_data/"
    model_directory_name = experiment_root_directory_name + "model/"
    os.makedirs(generated_data_directory_name, exist_ok=True)
    os.makedirs(model_directory_name, exist_ok=True)
    model.save(model_directory_name+'model.pkl')
    parameters_text_file = open(experiment_root_directory_name + "parameters.txt", "w")
    parameters_text_file.write(repr(experiment_parameters))
    metadata_text_file = open(experiment_root_directory_name + "metadata.txt", "w")
    metadata_text_file.write(repr(model.get_metadata().to_dict()))

    metrics_text_file = open(experiment_root_directory_name + "metrics.txt", "w")
    metrics_text_file.write('no hay métricas')

    for i in range(experiment_parameters.n_samples):
        generated_sample = model.sample(sequence_length=experiment_parameters.seq_len)
        save_sample_to_csv(generated_sample, generated_data_directory_name+"sample_"+ str(i) +".csv")

if __name__ == '__main__':
    # Inputs for the main function
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--ori_data_filename',
        type=str)
    parser.add_argument(
        '--trace',
        choices=['azure_v2', 'google2019', 'alibaba2018', 'reddit'],
        default='azure_v2',
        type=str)
    parser.add_argument(
        '--sample_size',
        default=1,
        type=int)
    parser.add_argument(
        '--n_samples',
        default=10,
        type=int)
    parser.add_argument(
        '--epochs',
        default=1,
        type=int)
    parser.add_argument(
        '--seq_len',
        default=10,
        type=int)

    args = parser.parse_args()
    main(args)