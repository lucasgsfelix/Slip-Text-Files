"""
    Split and join huge files

"""
import os

import sys

import math


def split_list(data_list, max_size):


    splits = []

    amount_splits = math.ceil(max_size/sys.getsizeof(data_list))

    split_index = math.ceil(len(data_list)/amount_splits)


    for split in range(0, amount_splits):

        splits.append(data_list[(split*split_index): split_index*(split+1)])


    return splits


def write_splitted_files(data_splits, file_name, path_file):

    file_prefix = file_name.split('.')[0] # assuming that is a .txt, .csv

    for index, split in enumerate(data_splits):

        with open(os.path.join(path_file,file_prefix + '_part_' + str(index) + '.txt'), 'w') as output_file:

            output_file.write('\n'.join(split) + '\n')


def define_path(path_file):

    if not path_file:

        return os.getcwd()

    return path_file


def split_files(path_file=None, file_size=1e+8, file_name=None):

    path_file = define_path(path_file)

    files_path = os.listdir(path_file)

    measure_size = os.path.getsize

    selected_files = []

    if file_name:

        if measure_size(os.path.join(path_file, file_name)) >= file_size:

            selected_files.append(file_name)

    else:

        selected_files = list(filter(lambda x: measure_size(os.path.join(path_file, x)) >= file_size, files_path))


    for file in selected_files:

        with open(os.path.join(path_file, file), 'r') as split_file:

            data_list = split_file.read().split('\n')

            data_splits = split_list(data_list, file_size)

            write_splitted_files(data_splits, file, path_file)


def join_files(string_seek, path_file=None):

    path_file = define_path(path_file)

    files_path= os.listdir(path_file)

    join_files = list(filter(lambda x: string_seek in x, files_path))

    join_files = sorted(join_files)


    with open(os.path.join(path_file, string_seek + '_join.txt'), 'w') as output_file:

        for file in join_files:

            with open(file, 'r') as join_file:

                output_file.write(join_file.read() + '\n')

