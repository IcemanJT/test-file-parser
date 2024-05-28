# Author: Jeremi Torój
# Date: 27/05/2024

import pandas as pd
import re


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
    content = file.read().decode('utf-8')

    num_rows = content.count('\n')
    num_words = len(re.findall(r'\w+', content))
    num_chars = len(content)
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content)
    #  I assume that phone number has 9/10 digits and can be separated by space or dash and may have country code
    phone_pattern = r'(\+\d{1,3}\s?)?(\d{3}[\s-]?\d{3}[\s-]?\d{3,4})'
    matched_numbers = re.findall(phone_pattern, content)
    phone_numbers = [''.join(match) for match in matched_numbers]

    summary = {
        'num_rows': num_rows,
        'num_words': num_words,
        'num_chars': num_chars,
        'emails': emails,
        'phone_numbers': phone_numbers,
    }

    return summary


def process_csv_file(file):
    df = pd.read_csv(file)

    #  I assume that csv file has header row
    columns = df.columns.tolist()

    num_of_rows = df.shape[0]

    summary = {
        'columns': columns,
        'num_of_rows': num_of_rows,
    }

    return summary


def process_json_file(file):
    raise NotImplementedError('Not implemented yet')
