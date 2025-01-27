from sdv.datasets.local import load_csvs
from sdv.sequential import PARSynthesizer
from sdv.metadata import Metadata

# T_min ≤ T_ave ≤ T_max
temperature_constraint = {
    'constraint_class': 'Range',
    'constraint_parameters': {
        'low_column_name': 'T_min (C)',
        'middle_column_name': 'T_ave (C)',
        'high_column_name': 'T_max (C)',
        'strict_boundaries': True
    }
}

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
    synthesizer.add_constraints(constraints=[temperature_constraint])
    synthesizer.fit(data)
    synthetic_data = synthesizer.sample(num_sequences=1)

    print(synthetic_data)

