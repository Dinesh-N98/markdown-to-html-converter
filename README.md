# Markdown to HTML Converter

A compact utility and small web app that converts Markdown files into HTML.

### Quick features

- Converts headings, paragraphs, blockquotes, ordered and unordered lists
- Converts tables and task lists
- Converts fenced code blocks, inline code, and syntax highlighting via `codehilite`
- Strikethrough (`~~text~~`) and checkbox normalization
- Opinionated, responsive HTML template included

### What it may miss

- Footnotes, definition lists, and some extended Markdown flavors
- Math blocks / inline LaTeX rendering
- YAML front matter handling
- GitHub-specific markdown edge cases and raw HTML passthrough
- Advanced extensions (admonitions, automatic TOC, emoji shortcuts)

### Requirements

- Python 3.7+
- Python packages: `markdown`, `flask`, `pygments`

## Install from GitHub

1. Clone the repo:

```bash
git clone https://github.com/Dinesh-N98/markdown-to-html-converter.git
cd markdown-to-html-converter
```

Or download the ZIP from GitHub, extract it, then `cd` into the extracted folder.

Optional: create and activate a virtual environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install markdown flask pygments
```

3. Run the server:

```bash
python server/server.py
# then open http://localhost:5000
```


## Web app

- Frontend: `frontend/` (served at `/`)
- Static assets: `/static` (points to `frontend/` files)

API endpoints:
- `POST /convert` — upload a `.md` file (form field `file`); returns JSON `{ output_file, message }`.
- `GET /export-HTML/<filename>` — serve converted HTML.

Converted files are written to `backend/export-HTML/`; uploaded files are saved to `backend/import-MD/`.


## File structure

```
markdown-to-html-converter/
├─ converter.py
├─ README.md
├─ frontend/
│  ├─ index.html
│  ├─ script.js
│  └─ style.css
├─ backend/
│  ├─ import-MD/
│  └─ export-HTML/
├─ server/
│  └─ server.py
```

## Backend

### Convert a file locally (CLI):

```bash
python converter.py sample.md
```

- This `sample.md` is in `backend/import-MD/`.
- If you want to convert a custom Markdown file, copy it into `backend/import-MD/` first.
- Run the code with your file name in CLI

```bash
python converter.py <your-file-name.md>
```

- After conversion, the generated HTML file will be written to `backend/export-HTML/`.


### CLI usage

```bash
python converter.py <input.md>
python converter.py <input.md> -o <output.html>
```

- If you specify `-o`, the converter will use the provided output path instead.

## Troubleshooting

- Port in use: change the port in `server/server.py`.
- Missing packages: run the `pip install` command above.
- Output file not found after conversion: verify the input file was saved to `backend/import-MD/` and check `converter.py` output path.

## Notes

This project favors a simple, practical conversion pipeline. For broader Markdown compatibility or advanced output control, consider `pandoc` or adding more extensions to the `markdown` converter.

If you want, I can also generate a minimal `requirements.txt` and add a short CONTRIBUTING section.
