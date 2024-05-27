# Author: Jeremi Torój
# Date: 27/05/2024


def process_file(file):
    filename = file.filename
    if filename.endswith('.txt'):
        return process_txt_file(file)
    elif filename.endswith('.csv'):
        return process_csv_file(file)
    elif filename.endswith('.json'):
        return process_json_file(file)
    else:
        raise ValueError('Invalid file format')


def process_txt_file(file):
    raise NotImplementedError('Not implemented yet')


def process_csv_file(file):
    raise NotImplementedError('Not implemented yet')


def process_json_file(file):
    raise NotImplementedError('Not implemented yet')