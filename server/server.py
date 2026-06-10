from flask import Flask, request, jsonify, make_response
from pathlib import Path
import os
import sys
import tempfile

# Add project root to path for imports
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Import configuration
from config import (
    DEBUG, HOST, PORT, 
    UPLOAD_DIR, EXPORT_DIR, 
    MAX_UPLOAD_SIZE, ALLOWED_EXTENSIONS,
    FRONTEND_DIR
)

from converter import convert_md_to_html

app = Flask(__name__, static_folder=str(FRONTEND_DIR), static_url_path='/static')


@app.route('/')
def index():
    frontend_index = FRONTEND_DIR / 'index.html'
    with open(frontend_index, 'r', encoding='utf-8') as f:
        return f.read()


@app.route('/preview')
@app.route('/preview.html')
def preview():
    frontend_preview = FRONTEND_DIR / 'preview.html'
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
        
        # Validate file extension
        file_ext = os.path.splitext(file.filename)[1].lower()
        if file_ext not in ALLOWED_EXTENSIONS:
            return jsonify({'error': f'File must be a markdown file ({", ".join(ALLOWED_EXTENSIONS)})'}), 400
        
        # Validate file size
        file.seek(0, 2)
        file_size = file.tell()
        file.seek(0)
        if file_size > MAX_UPLOAD_SIZE:
            return jsonify({'error': f'File size exceeds maximum allowed ({MAX_UPLOAD_SIZE / 1024 / 1024:.1f}MB)'}), 400

        output_filename = os.path.splitext(file.filename)[0] + '.html'

        # Save uploaded markdown to a temporary file, convert, then return HTML
        with tempfile.NamedTemporaryFile(delete=False, suffix='.md', dir=str(UPLOAD_DIR)) as tmp_in:
            tmp_in.write(file.read())
            tmp_in_path = tmp_in.name

        tmp_out = tempfile.NamedTemporaryFile(delete=False, suffix='.html', dir=str(EXPORT_DIR))
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
    print(f'Open http://{HOST}:{PORT} in your browser')
    print(f'Upload directory: {UPLOAD_DIR}')
    print(f'Export directory: {EXPORT_DIR}')
    app.run(debug=DEBUG, host=HOST, port=PORT)
    