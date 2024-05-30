# Author: Jeremi Torój
# Date: 27/05/2024

from flask import Flask, request, jsonify
from parser import process_file


ALLOWED_EXTENSIONS = {'txt', 'csv', 'json'}

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
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
