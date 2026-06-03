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

The converter handles many common Markdown features, including:

- headings (`#`, `##`, etc.)
- paragraphs
- blockquotes
- lists
- fenced code blocks
- tables
- inline code and code blocks
- syntax highlighting via `codehilite`
- strikethrough via custom `~~text~~` replacement

## What it may miss

This converter does not cover every Markdown flavor or extension. It may not support:

- footnotes
- task lists (`- [ ]`, `- [x]`)
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
python converter.py
```

By default, it converts `sample.md` into `output.html`.

## Requirements

- Python 3
- `markdown` package

Install the package with:

```bash
pip install markdown
```

## Notes

This is a good starting point for basic/common Markdown conversion, but it is not a complete Markdown-to-HTML engine for every Markdown flavor. For broader support, consider adding more `markdown` extensions or using a more full-featured tool like `pandoc`.
