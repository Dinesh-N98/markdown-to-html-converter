from flask import Flask, request, jsonify, send_from_directory
import os
import subprocess
import sys

app = Flask(__name__, static_folder='../frontend', static_url_path='/static')

# Paths
base_dir = os.path.dirname(os.path.abspath(__file__))  # .../server
project_root = os.path.dirname(base_dir)  # workspace root
IMPORT_DIR = os.path.join(project_root, 'backend', 'import-MD')
EXPORT_DIR = os.path.join(project_root, 'backend', 'export-HTML')

# Ensure directories exist
os.makedirs(IMPORT_DIR, exist_ok=True)
os.makedirs(EXPORT_DIR, exist_ok=True)


@app.route('/')
def index():
    frontend_index = os.path.join(project_root, 'frontend', 'index.html')
    with open(frontend_index, 'r', encoding='utf-8') as f:
        return f.read()


@app.route('/convert', methods=['POST'])
def convert_markdown():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        if not file.filename.lower().endswith('.md'):
            return jsonify({'error': 'File must be a .md file'}), 400

        filename = file.filename
        input_path = os.path.join(IMPORT_DIR, filename)
        file.save(input_path)

        output_filename = os.path.splitext(filename)[0] + '.html'
        output_path = os.path.join(EXPORT_DIR, output_filename)

        # Run converter.py from project root so its relative paths work
        converter_path = os.path.join(project_root, 'converter.py')
        result = subprocess.run(
            [sys.executable, converter_path, filename],
            capture_output=True,
            text=True,
            cwd=project_root
        )

        if result.returncode != 0:
            return jsonify({'error': f'Conversion failed: {result.stderr}'}), 500

        if not os.path.exists(output_path):
            return jsonify({'error': 'Conversion finished but output file not found'}), 500

        return jsonify({
            'success': True,
            'output_file': output_filename,
            'message': f'Successfully converted {filename} to {output_filename}'
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/export-HTML/<path:filename>')
def serve_export(filename):
    return send_from_directory(EXPORT_DIR, filename)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200


if __name__ == '__main__':
    print('Starting Markdown to HTML Converter Server...')
    print('Open http://localhost:5000 in your browser')
    app.run(debug=True, host='localhost', port=5000)
    