from flask import Flask, request, jsonify, make_response
import os
import sys

app = Flask(__name__, static_folder='../frontend', static_url_path='/static')

# Paths
base_dir = os.path.dirname(os.path.abspath(__file__))  # .../server
project_root = os.path.dirname(base_dir)  # workspace root
sys.path.insert(0, project_root)

import converter


@app.route('/')
def index():
    frontend_index = os.path.join(project_root, 'frontend', 'index.html')
    with open(frontend_index, 'r', encoding='utf-8') as f:
        return f.read()


@app.route('/preview')
@app.route('/preview.html')
def preview():
    frontend_preview = os.path.join(project_root, 'frontend', 'preview.html')
    with open(frontend_preview, 'r', encoding='utf-8') as f:
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

        markdown_bytes = file.read()
        markdown_text = markdown_bytes.decode('utf-8', errors='replace')
        output_filename = os.path.splitext(file.filename)[0] + '.html'

        html_content = converter.convert_markdown_text_to_html(markdown_text)
        response = make_response(html_content)
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        response.headers['Content-Disposition'] = f'attachment; filename="{output_filename}"'
        return response

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200


if __name__ == '__main__':
    print('Starting Markdown to HTML Converter Server...')
    print('Open http://localhost:5000 in your browser')
    app.run(debug=True, host='localhost', port=5000)
    