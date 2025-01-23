# -*- coding: utf-8 -*-
"""Data preprocessing

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11rmg6LwJ9B5qjITarKVRsVixGp7GgWgM
"""

import pandas as pd
from sdv.metadata import Metadata
import os

def process_data(df, output_file):
    df['Time (s)'] = df['Time (s)'].astype(float)
    df.drop(columns=['Case_No.', 'TimeN (s)', 'Time_aveN (C)'], inplace=True)
    df.to_csv(output_file, index=False, encoding='utf-8')

    return df

def generate_metadata(df, metadata_file):
    metadata = Metadata.detect_from_dataframe(data=df)

    metadata.update_column(column_name='Sequence_ID', sdtype='id')
    metadata.set_sequence_key('Sequence_ID')
    metadata.set_sequence_index(column_name='Time (s)')

    metadata.save_to_json(filepath=metadata_file)


def preprocessing(input_dir, output_file, metadata_file):
    df = pd.DataFrame()

    for f in sorted(os.listdir(input_dir)):
        input_file = os.path.join(input_dir, f)

        if not os.path.isfile(input_file):
            continue
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"File {input_file} not found")
        if os.path.exists(output_file):
            os.remove(output_file)
        if os.path.exists(metadata_file):
            os.remove(metadata_file)

        df = pd.concat([df, pd.read_csv(input_file)], ignore_index=True)

    df = process_data(df, output_file)
    generate_metadata(df, metadata_file)


