# Author: Jeremi Torój
# Date: 27/05/2024

from flask import Flask, request, jsonify
from parser import process_file
from prometheus_client import Counter, Summary, generate_latest

ALLOWED_EXTENSIONS = {'txt', 'csv', 'json'}

app = Flask(__name__)

REQUESTS_EXCEPTIONS = Counter('http_requests_exceptions', 'Number of exceptions during HTTP requests')
REQUEST_DURATION = Summary('HTTP_requests', 'HTTP requests summary')


@app.route('/metrics')
def metrics():
    return generate_latest()


@app.route('/upload', methods=['POST'])
@REQUEST_DURATION.time()
@REQUESTS_EXCEPTIONS.count_exceptions()
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        summary = process_file(file)
        return jsonify(summary), 200
    else:
        return jsonify({'error': 'Invalid file format'}), 400


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run(debug=True)
