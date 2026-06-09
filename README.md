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

## Contributing

Contributions are welcome. If you want to help improve the converter:

- Open an issue for bugs or feature requests.
- Send a pull request with a clear description of your change.
- Keep changes small and focused, especially for parser or template updates.


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
- `POST /convert` — upload a `.md` file (form field `file`); returns the converted HTML directly as a downloadable attachment.

Converted files are not stored on the server for the web app flow.


## File structure

```
markdown-to-html-converter/
├─ converter.py
├─ README.md
├─ frontend/
│  ├─ index.html
│  ├─ script.js
│  └─ style.css
├─ server/
│  └─ server.py
```

## Backend

### Convert a file locally (CLI):

```bash
python converter.py sample.md
```

- `sample.md` can be any Markdown file accessible from your current directory.
- The output file is written as `sample.html` in the current directory by default.
- To choose a specific output location, provide `-o`.

```bash
python converter.py <input.md>
python converter.py <input.md> -o <output.html>
```

- If you specify `-o`, the converter will write to the provided output path.

## Troubleshooting

- Port in use: change the port in `server/server.py`.
- Missing packages: run the `pip install` command above.
- Output file not found after conversion: verify the input file exists and check `converter.py` output path.

## Notes

This project favors a simple, practical conversion pipeline. For broader Markdown compatibility or advanced output control, consider `pandoc` or adding more extensions to the `markdown` converter.
