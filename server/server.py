from flask import Flask, request, jsonify, make_response
from pathlib import Path
import os
import sys
import tempfile

app = Flask(__name__, static_folder='../frontend', static_url_path='/static')

# Paths
base_dir = Path(__file__).resolve().parent  # .../server
project_root = base_dir.parent  # workspace root
sys.path.insert(0, str(project_root))

from converter import convert_md_to_html


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

        output_filename = os.path.splitext(file.filename)[0] + '.html'

        # Save uploaded markdown to a temporary file, convert, then return HTML
        with tempfile.NamedTemporaryFile(delete=False, suffix='.md') as tmp_in:
            tmp_in.write(file.read())
            tmp_in_path = tmp_in.name

        tmp_out = tempfile.NamedTemporaryFile(delete=False, suffix='.html')
        tmp_out_path = tmp_out.name
        tmp_out.close()

        try:
            convert_md_to_html(tmp_in_path, tmp_out_path)
            with open(tmp_out_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
        finally:
            try:
                os.remove(tmp_in_path)
            except Exception:
                pass
            try:
                os.remove(tmp_out_path)
            except Exception:
                pass

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
    