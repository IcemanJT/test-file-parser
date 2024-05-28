# test-file-parser
### Author: Jeremi Torój
### Date: 26-05-2024
Parser for text files containing data (e.g. CSV, TXT, JSON)

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

## Parser details
### .txt
Parser returns:
- number of lines
- number of words
- number of characters
- email addresses
- phone numbers

Note: Phone numbers are recognized as a sequence of 9 or 10 digits that might be separated by spaces or dashes. The phone number might be preceded by a country code.


### .csv

### .json

