import argparse
import os
import shutil
import traceback
from tqdm import tqdm
from distutils.dir_util import copy_tree
from functools import partialmethod

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
        for dir_name in tqdm(first_level_dirs):
            experiment_dir = root_dir + dir_name
            generate_new_experiment_samples_from_experiment_dir(args_params.seq_len, args_params.n_samples, experiment_dir, dir_name)
        print(f'All models where loaded and data samples generated in {args_params.experiment_dir}-seq_len-{args_params.seq_len}')
    else:
        generate_new_experiment_samples_from_experiment_dir(args_params.seq_len, args_params.n_samples, root_dir)

def generate_new_experiment_samples_from_experiment_dir(seq_len, n_samples, experiment_dir, dir_name=''):
    try:
        experiment_dir_parent = os.path.dirname(experiment_dir)
        cloned_experiment_dir = f'{experiment_dir_parent}-seq_len-{seq_len}/{dir_name}'
        clone_experiment(experiment_dir, cloned_experiment_dir)
        loaded_model = PAR.load(cloned_experiment_dir + '/model/model.pkl')
        generate_samples_from_model(seq_len, n_samples, cloned_experiment_dir, loaded_model)
    except Exception as e:
        print('Error computing experiment dir:', experiment_dir)
        print(e)
        traceback.print_exc()


def generate_samples_from_model(seq_len,n_samples, experiment_root_directory_name, model):
    generated_data_directory_name = experiment_root_directory_name + "/generated_data/"
    os.makedirs(generated_data_directory_name, exist_ok=True)
    for i in tqdm(n_samples, leave=False):
        tqdm.__init__ = partialmethod(tqdm.__init__, disable=True)
        generated_sample = model.sample(sequence_length=seq_len)
        save_sample_to_csv(generated_sample, generated_data_directory_name + "sample_" + str(i) + ".csv")

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
