from flask import Flask, request, jsonify, make_response
from pathlib import Path
import sys

from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.utils import secure_filename

# Add project root to path for imports
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Import configuration
from config import DEBUG, HOST, PORT, MAX_UPLOAD_SIZE, ALLOWED_EXTENSIONS, FRONTEND_DIR
from converter import convert_markdown_text_to_html

app = Flask(__name__, static_folder=str(FRONTEND_DIR), static_url_path='/static')
app.config['MAX_CONTENT_LENGTH'] = MAX_UPLOAD_SIZE


@app.route('/')
def index():
    frontend_index = FRONTEND_DIR / 'index.html'
    return frontend_index.read_text(encoding='utf-8')


@app.route('/preview')
@app.route('/preview.html')
def preview():
    frontend_preview = FRONTEND_DIR / 'preview.html'
    return frontend_preview.read_text(encoding='utf-8')


@app.errorhandler(RequestEntityTooLarge)
def handle_request_entity_too_large(error):
    return jsonify({'error': f'File size exceeds maximum allowed ({MAX_UPLOAD_SIZE / 1024 / 1024:.1f}MB)'}), 413


def allowed_file(filename: str) -> bool:
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS


@app.route('/convert', methods=['POST'])
def convert_markdown():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if not file or file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    filename = secure_filename(Path(file.filename).name)
    if filename == '':
        return jsonify({'error': 'Invalid file name provided'}), 400

    if not allowed_file(filename):
        return jsonify({'error': f'File must be a markdown file ({", ".join(sorted(ALLOWED_EXTENSIONS))})'}), 400

    content = file.read()
    if not content:
        return jsonify({'error': 'Empty file provided'}), 400

    try:
        markdown_text = content.decode('utf-8')
    except UnicodeDecodeError:
        markdown_text = content.decode('utf-8', errors='replace')

    html_content = convert_markdown_text_to_html(markdown_text)
    output_filename = Path(filename).with_suffix('.html').name

    response = make_response(html_content)
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    response.headers['Content-Disposition'] = f'attachment; filename="{output_filename}"'
    return response


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200


if __name__ == '__main__':
    print('Starting Markdown to HTML Converter Server...')
    print(f'Open http://{HOST}:{PORT} in your browser')
    app.run(debug=DEBUG, host=HOST, port=PORT)
    