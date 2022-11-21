import argparse

import pandas as pd
from sdv.timeseries import PAR
import os
from datetime import datetime
import collections

from datacentertracesdatasets import loadtraces

from dataset_schema_loader import get_dataset_info


def main(args_params):
    dataset_info = get_dataset_info(args_params.trace)
    if (args_params.ori_data_filename):
        data = pd.read_csv(args_params.ori_data_filename, names=dataset_info['column_config'].keys())
    else:
        data = loadtraces.get_alibaba_2018_trace(stride_seconds = dataset_info['timestamp_frequency_secs'])

    field_types = dataset_info['metadata']['fields']

    Namespace = collections.namedtuple('Parameters', 'iteration sample_size n_samples data_name seq_len ')
    experiment_parameters = Namespace(iteration=args_params.epochs, sample_size=args_params.sample_size,
                                      n_samples=args_params.n_samples, data_name=args_params.trace,
                                      seq_len=args_params.seq_len)

    model = PAR(
        field_types=field_types,
        epochs=experiment_parameters.iteration,
        sample_size=experiment_parameters.sample_size,
        verbose=True,
    )

    model.fit(data)
    experiment_root_directory_name = save_experiment_files(experiment_parameters, model, args.experiment_save_dir)
    print ("Experiment data saved in", args.experiment_save_dir)

    generate_samples_from_model(experiment_parameters.seq_len, experiment_parameters.n_samples, experiment_root_directory_name, model)


def generate_samples_from_model(seq_len, n_samples, experiment_root_directory_name, model):
    generated_data_directory_name = experiment_root_directory_name + "generated_data/"
    os.makedirs(generated_data_directory_name, exist_ok=True)
    for i in range(n_samples):
        generated_sample = model.sample(sequence_length=seq_len)
        generated_sample.to_csv(f'{generated_data_directory_name}/sample_{i}.csv', header=False, index=False)

    print ("Samples saved in", generated_data_directory_name)


def save_experiment_files(experiment_parameters, model, experiment_save_dir):
    experiment_root_directory_name = f'{args.experiment_save_dir}/{experiment_parameters.data_name}_epochs-{experiment_parameters.iteration}-{datetime.now().strftime("%j-%Y-%H-%M")}/'
    model_directory_name = experiment_root_directory_name + "model/"

    os.makedirs(model_directory_name, exist_ok=True)

    model.save(model_directory_name + 'model.pkl')
    parameters_text_file = open(experiment_root_directory_name + "parameters.txt", "w")
    parameters_text_file.write(repr(experiment_parameters))
    metadata_text_file = open(experiment_root_directory_name + "metadata.txt", "w")
    metadata_text_file.write(repr(model.get_metadata().to_dict()))
    metrics_text_file = open(experiment_root_directory_name + "metrics.txt", "w")
    metrics_text_file.write('no hay métricas')
    return experiment_root_directory_name


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
    parser.add_argument(
        '--experiment_save_dir',
        default='experiments/',
        type=str)

    args = parser.parse_args()
    main(args)
