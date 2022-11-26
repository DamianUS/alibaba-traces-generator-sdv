import argparse
import os
import shutil
import traceback
from datetime import datetime
from distutils.dir_util import copy_tree

from sdv.timeseries import PAR


def save_sample_to_csv(generated_sample, file_name):
    generated_sample.to_csv(file_name, header=False, index=False)


def clone_experiment(experiment_dir, new_experiment_dir):
    copy_tree(experiment_dir, new_experiment_dir)
    try:
        remove_directory_files(new_experiment_dir + '/generated_data')
    except:
        print('Failed to remove directory'+ new_experiment_dir + '/generated_data')

    try:
        remove_directory_files(new_experiment_dir + '/evaluation_metrics')
    except:
        print('Failed to remove directory'+ new_experiment_dir + '/evaluation_metrics')


def remove_directory_files(directory_name):
    for filename in os.listdir(directory_name):
        file_path = os.path.join(directory_name, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def main(args_params):
    root_dir = args_params.experiment_dir
    if args_params.recursive == 'true':
        first_level_dirs = []
        for subdir, dirs, files in os.walk(root_dir):
            first_level_dirs = dirs
            break
        for dir_name in first_level_dirs:
            print("dir_name", dir_name)
            experiment_dir = root_dir + dir_name
            print('experiment_dir', experiment_dir)
            generate_new_experiment_samples_from_experiment_dir(args_params.seq_len, args_params.n_samples, experiment_dir, dir_name)
        print("\nAll models where loaded and data samples generated:\n")
    else:
        generate_new_experiment_samples_from_experiment_dir(args_params.seq_len, args_params.n_samples, root_dir)

def generate_new_experiment_samples_from_experiment_dir(seq_len, n_samples, experiment_dir, dir_name):
    try:
        experiment_dir_parent = os.path.dirname(experiment_dir)
        print("Processing directory ", experiment_dir)
        cloned_experiment_dir = experiment_dir_parent + '/seq_len-' + str(seq_len) + '/'+dir_name
        print("Cloned experiment dir", cloned_experiment_dir)
        clone_experiment(experiment_dir, cloned_experiment_dir)
        loaded_model = PAR.load(cloned_experiment_dir + '/model/model.pkl')
        generate_samples_from_model(seq_len, n_samples, cloned_experiment_dir, loaded_model)
        print("Finished generation of samples in ", cloned_experiment_dir)
    except Exception as e:
        print('Error computing experiment dir:', experiment_dir)
        print(e)
        traceback.print_exc()


def generate_samples_from_model(seq_len,n_samples, experiment_root_directory_name, model):
    generated_data_directory_name = experiment_root_directory_name + "/generated_data/"
    os.makedirs(generated_data_directory_name, exist_ok=True)
    for i in range(n_samples):
        generated_sample = model.sample(sequence_length=seq_len)
        save_sample_to_csv(generated_sample, generated_data_directory_name + "sample_" + str(i) + ".csv")

    print("Samples saved in", generated_data_directory_name)

if __name__ == '__main__':
    # Inputs for the main function
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--experiment_dir',
        required=True,
        type=str)
    parser.add_argument(
        '--recursive',
        default='false',
        type=str)
    parser.add_argument(
        '--seq_len',
        default=288,
        type=int)
    parser.add_argument(
        '--n_samples',
        default=10,
        type=int)

    args = parser.parse_args()
    main(args)
