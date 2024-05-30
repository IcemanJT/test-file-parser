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
OR
2. Run the streamlit app
```bash
streamlit run sl_page.py
```
3. Upload the file to be parsed
4. The summary of the file content will be displayed


## Class: FileParser

Responsible for parsing different file formats and generating summaries of their content.

### Methods:

#### `process(file)`

Determines the file type and processes the file accordingly.

**Parameters:**
- `file`: The file object to be processed.

**Returns:**
- A dictionary containing the summary of the file content.

#### `process_json_file(file)`

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

#### `process_csv_file(file)`

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

#### `process_txt_file(file)`

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

## File: http_connection.py

Responsible for handling HTTP requests, file uploads, and metrics exposition.

### Routes:

#### `/upload` [POST]

Handles file uploads and processes them.

**Request Parameters:**
- `file`: The file to be uploaded.

**Response:**
- If successful, returns a JSON object containing a summary of the file content. The structure of the summary depends on the file type.

#### `/metrics` [GET]

Exposes Prometheus metrics for monitoring purposes.

**Prometheus Metrics:**
- `upload_exceptions`: Counts the number of exceptions during file upload.
- `file_process_time_seconds`: Measures number of uploaded files, time of processing and creates histogram of time taken to process.

### Functions:

#### `upload_file()`

Handles file uploads and processing.

**Returns:**
- If successful, returns a JSON object containing a summary of the file content. Otherwise, returns an error message.

#### `allowed_file(filename)`

Checks if the file extension is allowed for upload.

**Parameters:**
- `filename`: Name of the file to check.

**Returns:**
- `True` if the file extension is allowed, `False` otherwise.

#### `metrics()`

Returns Prometheus metrics for monitoring purposes.

**Returns:**
- Prometheus' metrics in text format.

### Dependencies:
- Flask: Handles HTTP requests and routes.
- prometheus_client: Generates Prometheus metrics.
- FileParser: Handles file parsing and summarization.

## File: sl_page.py

Responsible for providing a Streamlit web interface for file upload and processing.

### Dependencies:
- streamlit: Facilitates the creation of interactive web applications.
- requests: Enables HTTP requests to the Flask API.

### Features:

#### File Upload:
- Users can upload files using the file uploader provided by Streamlit.

#### File Processing:
- Uploaded files are sent via HTTP POST requests to the Flask API (`http://127.0.0.1:5000/upload`) for processing.

#### Display Summary:
- If the processing is successful (HTTP status code 200), the summary of the file content is displayed.
- If an error occurs during processing, an error message is displayed.

### Variables:

#### `FLASK_API_URL`
- URL of the Flask API endpoint for file upload and processing (`http://127.0.0.1:5000/upload`).
