#!/usr/bin/env python3

from os.path import join
PATH = '/Users/krishnakalyan3/Educational/SGS_TextMining/data/sample/001'
SAVE_PATH = PATH + 'wc_data.csv'

import os
import csv


def unique_word_count(in_file):
    wc_dict = {}
    with open(in_file, "r", encoding='UTF-8') as f:
        split_word = f.read().split(" ")
        for i in split_word:
            if i not in wc_dict:
                wc_dict[i] = 1
            else:
                wc_dict[i] += 1
    return wc_dict


def get_files(PATH):
    my_files = []
    for r, d, f in os.walk(PATH, topdown=False):
        for file in f:
            path_name = '/'.join([r, file])
            try:
                my_files += [path_name]
            except:
                pass
    return my_files


def write_file(data, PATH):
    print(data)
    with open(PATH, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == '__main__':
    all_data = []
    file = get_files(PATH)
    for i in file:
        wc = unique_word_count(i)
        dist_count = len(wc)
        total_count = 0

        for k, v in enumerate(wc):
            total_count += int(k)

        my_data = ' '.join([i.split('/')[-1], str(dist_count), str(total_count)])
        all_data.append(my_data)

    myfile = open('001.csv', 'w')
    wr = csv.writer(myfile, delimiter=';')
    wr.writerows([''.join(c[0:])] for c in all_data)
    myfile.close()
