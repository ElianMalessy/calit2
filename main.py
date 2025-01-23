from data_preprocessing import preprocessing
from generate_data import generate_data
import argparse
import os

parser = argparse.ArgumentParser(description="processing and generating data")
parser.add_argument("--restart", action="store_true", help="processes data from scratch before generating it")
args = parser.parse_args()

data_dir = os.path.normpath('data/')
cases_dir = os.path.normpath('cases/')
metadata_dir = os.path.normpath('metadata/')

cases_file = os.path.join(cases_dir, 'cases.csv')
metadata_file = os.path.join(metadata_dir, 'cases_metadata.json')

if __name__ == '__main__':
    if args.restart:
        preprocessing(data_dir, cases_file, metadata_file)
    generate_data(cases_dir, metadata_file)
