from sdv.datasets.local import load_csvs
from sdv.sequential import PARSynthesizer
from sdv.metadata import Metadata
import os

def generate_data(cases_dir, metadata_file):
    datasets = load_csvs(
        folder_name=cases_dir,
        read_csv_parameters={
            'skipinitialspace': True,
            'encoding': 'utf_8'
        })

    data = datasets['cases']
    metadata = Metadata.load_from_json(metadata_file)

    synthesizer = PARSynthesizer(metadata)
    synthesizer.fit(data)
    synthetic_data = synthesizer.sample(num_sequences=10)
    print(synthetic_data)
    # synthetic_data.sort_values(by='Time (s)', ascending=True, inplace=True)

