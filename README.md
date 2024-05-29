# text-file-parser
### Author: Jeremi Torój
### Date: 26-05-2024
Parser for text files containing data.

## Supported file formats
- .txt
- .csv
- .json

## Requirements
- Python 3.11
- OS: Linux, MacOS

## Installation
1. Clone the repository 
2. Creat a virtual environment
```bash
python3 -m venv venv
```
3. Activate the virtual environment
```bash
source venv/bin/activate
```
4. Install the requirements
```bash
pip install -r requirements.txt
```

## Usage
1. Run the script
```bash
python3 http_connection.py
```
2. Send a POST request with the file to be parsed replacing `<path_to_file>` with the path to the file
```bash
curl -X POST -F 'file=@<path_to_file>' http://127.0.0.1:5000/upload
```

## API Endpoints

### `/upload` [POST]

Uploads a file and processes it.

**Request Parameters:**
- `file`: The file to be uploaded.

**Response:**
- If successful, returns a JSON object containing a summary of the file content. The structure of the summary depends on the file type:

### `/metrics` [GET]

Returns Prometheus metrics for monitoring purposes.

**Prometheus Metrics:**
- `http_requests_exceptions`: Counts the number of exceptions during HTTP requests.
- `HTTP_requests`: Records the number and duration of HTTP requests.

## Functions

### `process_file(file)`

Determines the file type and processes the file accordingly.

**Parameters:**
- `file`: The file object to be processed.

**Returns:**
- A dictionary containing the summary of the file content.

### `process_txt_file(file)`

Processes a `.txt` file and generates a summary of its content.

**Parameters:**
- `file`: The text file object to be processed.

**Returns:**
- A dictionary with the following keys:
  - `num_rows`: Number of rows in the file.
  - `num_words`: Number of words in the file.
  - `num_chars`: Number of characters in the file.
  - `emails`: List of email addresses found in the file.
  - `phone_numbers`: List of phone numbers found in the file.

### `process_csv_file(file)`

Processes a `.csv` file and generates a summary of its content.

**Parameters:**
- `file`: The CSV file object to be processed.

**Returns:**
- A dictionary with the following keys:
  - `num_rows`: Number of rows in the CSV file.
  - `num_columns`: Number of columns in the CSV file.
  - `unique_values`: Dictionary of unique values count for each column.
  - `categorical_column_stats`: Basic statistics for categorical columns.
  - `numerical_column_stats`: Basic statistics for numerical columns.

### `process_json_file(file)`

Processes a `.json` file and generates a summary of its content by flattening nested structures.

**Parameters:**
- `file`: The JSON file object to be processed.

**Returns:**
- A dictionary with the following keys:
  - `flat_data`: Flattened JSON data.
  - `keys`: List of keys in the flattened JSON data.
  - `values`: List of values in the flattened JSON data.
  - `num_keys`: Number of keys in the flattened JSON data.
  - `num_values`: Number of values in the flattened JSON data.
  - `unique_values`: Number of unique values in the flattened JSON data.

