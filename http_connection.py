# Author: Jeremi Torój
# Date: 27/05/2024

#  server.py

from flask import Flask, request, jsonify
from prometheus_client import generate_latest, Counter, Histogram
from FileParser import FileParser

ALLOWED_EXTENSIONS = {'txt', 'csv', 'json'}

app = Flask(__name__)

upload_exceptions = Counter('upload_exceptions', 'Upload exceptions')
upload_summary = Histogram('upload_file_summary', 'Summary of uploaded file processing time in seconds')
successful_uploads = Counter('successful_uploads', 'Number of successful uploads')


@app.route('/upload', methods=['POST'])
@upload_summary.time()
@upload_exceptions.count_exceptions()
def upload_file():
    parser = FileParser()
    if 'file' not in request.files:
        upload_exceptions.inc()
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        upload_exceptions.inc()
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        try:
            summary = parser.process(file)
            successful_uploads.inc()
            return jsonify(summary), 200
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        upload_exceptions.inc()
        return jsonify({'error': 'Invalid file format'}), 400


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/metrics')
def metrics():
    metrics_exposition = generate_latest()
    return metrics_exposition


if __name__ == '__main__':
    app.run(debug=True)
