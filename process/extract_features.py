from __future__ import print_function
import os, sys
import argparse
import json
import numpy as np

def convert_to_dict(data, is_test=False):
    ret_dict = {}
    if not is_test:
        ret_dict["Y"] = data[:, 0].tolist()
        ret_dict["X"] = data[:, 1:].tolist()
    else:
        ret_dict["X"] = data.tolist()
    return ret_dict


def extract_features(args):
    train_file = os.path.join(args.data_dir, args.training_file)
    test_file = os.path.join(args.data_dir, args.test_file)
    output_dir = args.output_dir
    train_output_file = os.path.join(output_dir, "train.json")
    test_output_file = os.path.join(output_dir, "test.json")

    if not os.path.exists(train_file):
        print("Training file does not exist")
        sys.exit(-1)
    if not os.path.exists(test_file):
        print("Test file does not exist")
        sys.exit(-1)

    training_data = np.genfromtxt(train_file, delimiter=',', skip_header=1)
    test_data = np.genfromtxt(test_file, delimiter=',', skip_header=1)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(train_output_file, 'w') as fh:
        json.dump(convert_to_dict(training_data), fh)

    with open(test_output_file, 'w') as fh:
        json.dump(convert_to_dict(test_data), fh)

    if os.path.exists(train_output_file) and os.path.exists(test_output_file):
        sys.exit(0)
    else:
        print("Extract Features Fail")
        sys.exit(-1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--training_file", default="train.csv")
    parser.add_argument("--test_file", default="test.csv")
    parser.add_argument("--output_dir", default="output/features")
    parser.add_argument('data_dir')

    args = parser.parse_args()
    extract_features(args)
