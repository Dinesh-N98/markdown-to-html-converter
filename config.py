"""Application configuration for Markdown to HTML Converter."""

import os
from pathlib import Path

# Base directory (project root)
BASE_DIR = Path(__file__).resolve().parent

# Flask configuration
DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
HOST = os.getenv('FLASK_HOST', 'localhost')
PORT = int(os.getenv('FLASK_PORT', 5000))

# Upload and export directories
UPLOAD_DIR = Path(os.getenv('UPLOAD_DIR', BASE_DIR / 'uploads'))
EXPORT_DIR = Path(os.getenv('EXPORT_DIR', BASE_DIR / 'exports'))

# Ensure directories exist
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

# File configuration
MAX_UPLOAD_SIZE = int(os.getenv('MAX_UPLOAD_SIZE', 10 * 1024 * 1024))  # 10MB default
ALLOWED_EXTENSIONS = {'.md', '.markdown'}

# Frontend paths
FRONTEND_DIR = BASE_DIR / 'frontend'
