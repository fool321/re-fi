# -*- coding: utf-8 -*- 
# @Time : 2021/6/8 
# @Author : thefool
# @File : test.py.py

import pickle as pickle
import numpy as np

# python 2 working
def LoadDataNoDefCW_py2():
    print("Loading non-defended dataset for closed-world scenario")
    # Point to the directory storing data
    dataset_dir = '../dataset/ClosedWorld/NoDef/'

    # X represents a sequence of traffic directions
    # y represents a sequence of corresponding label (website's label)

    # Load training data
    with open(dataset_dir + 'X_test_NoDef.pkl', 'rb') as handle:
        X_train = np.array(pickle.load(handle))

    print("Data dimensions:")
    print("X: Training data's shape : ", X_train.shape)

    return X_train

# python3 work
def LoadDataNoDefCW():
    print("Loading non-defended dataset for closed-world scenario")
    # Point to the directory storing data
    dataset_dir = '../dataset/ClosedWorld/NoDef/'

    # X represents a sequence of traffic directions
    # y represents a sequence of corresponding label (website's label)

    # Load training data
    with open(dataset_dir + 'X_test_NoDef.pkl', 'rb') as handle:
        X_train = np.array(pickle.load(handle,encoding='bytes')) # add encoding='bytes'

    print("Data dimensions:")
    print("X: Training data's shape : ", X_train.shape)

    return X_train

def main():
    LoadDataNoDefCW()
    pass


if __name__ == '__main__':
    main()
