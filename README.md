# Markdown to HTML Converter

A small Python utility that converts a Markdown file into a styled HTML document.

## Features

- Converts headings, paragraphs, blockquotes, lists, and tables
- Supports fenced code blocks with syntax highlighting
- Converts inline code and code blocks
- Adds clean HTML skeleton and simple default styling
- Custom support for strikethrough using `~~text~~`
- Includes normalization to help lists render correctly when they follow a paragraph

## What it covers

The converter handles many common Markdown features with optimizations for performance and rendering:

- headings (`#`, `##`, etc.)
- paragraphs
- blockquotes
- lists (both ordered and unordered, with proper normalization)
- task lists (`- [ ]`, `- [x]`) with HTML disabled checkboxes
- fenced code blocks
- tables
- inline code and code blocks
- syntax highlighting via `codehilite` (Monokai theme)
- strikethrough via custom `~~text~~` replacement
- pre-compiled regex patterns for improved performance
- responsive HTML5 template with modern styling
- automatic list normalization to prevent rendering issues

## What it may miss

This converter does not cover every Markdown flavor or extension. It may not support:

- footnotes
- definition lists
- math blocks / inline math
- YAML front matter
- emoji shortcuts
- admonitions / callouts
- automatic table of contents
- some GitHub Flavored Markdown edge cases
- custom HTML attributes or raw HTML in Markdown
- other `markdown` package extensions that are not enabled

## Usage

Run the converter from the command line using Python:

```bash
python converter.py <file-name.md>
python converter.py <file-name.md> -o <output-name.html>
```

**File Locations:**
- Input files should be placed in the `import-MD/` directory
- Output HTML files are automatically saved to the `export-HTML/` directory

**Arguments:**
- `<file-name.md>`: Required. The Markdown file to convert (referenced from `import-MD/`)
- `-o, --output`: Optional. Specify a custom output filename. If omitted, the output filename is derived from the input filename (e.g., `sample.md` → `sample.html`)

## Requirements

- Python 3
- `markdown` package

Install the package with:

```bash
pip install markdown
```

## Styling

The converter includes comprehensive built-in styling with:

- Clean, modern design using system fonts
- Dark code blocks with Monokai syntax highlighting
- Responsive typography and spacing
- Styled tables, blockquotes, and lists
- Proper handling of code elements with syntax highlighting
- Optimized for readability across different screen sizes

## Notes

This is a solid utility for converting common Markdown files to well-styled HTML. The converter prioritizes performance through pre-compiled regex patterns and provides sensible defaults for styling and layout.

For advanced use cases or broader Markdown flavor support, consider:
- Adding more `markdown` package extensions
- Using a more full-featured tool like `pandoc` or `commonmark`
- Customizing the CSS template in `converter.py` for your specific design needs
