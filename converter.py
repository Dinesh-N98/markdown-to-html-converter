import argparse
import os
import re
import shutil
import sys
import markdown

# Pre-compile regex patterns for better performance
_LIST_PATTERN = re.compile(r'^(?:[ \t]{0,3}(?:\* |\+ |-|\d+\.\s))', re.MULTILINE)
_PREV_LINE_PATTERN = re.compile(r'^(?:[ \t]{0,3}(?:\* |\+ |-|\d+\.\s)|> |#{1,6} |---|\*\*\*|___)', re.MULTILINE)
_STRIKETHROUGH_PATTERN = re.compile(r'~~(.*?)~~', re.S)
_CHECKBOX_PATTERN = re.compile(r'^(\s*(?:[-+*]|\d+\.))\s*\[([ xX])\]\s+', re.M)

def normalize_markdown(markdown_text):
    """Normalize markdown text for better HTML conversion.
    
    - Adds blank lines before lists following paragraphs
    - Converts strikethrough (~~text~~) to HTML <del> tags
    - Converts markdown checkboxes to HTML input elements
    """
    lines = markdown_text.splitlines()
    normalized_lines = []
    
    # Add empty line before lists if needed
    for index, line in enumerate(lines):
        if _LIST_PATTERN.match(line):
            previous = lines[index - 1] if index > 0 else ''
            if previous.strip() and not _PREV_LINE_PATTERN.match(previous):
                normalized_lines.append('')
        normalized_lines.append(line)

    normalized_text = '\n'.join(normalized_lines)
    
    # Apply transformations
    normalized_text = _STRIKETHROUGH_PATTERN.sub(r'<del>\1</del>', normalized_text)
    normalized_text = _CHECKBOX_PATTERN.sub(
        lambda m: f"{m.group(1)} <input type=\"checkbox\" disabled{' checked' if m.group(2).lower() == 'x' else ''}> ",
        normalized_text
    )
    return normalized_text

def convert_md_to_html(input_file, output_file):
    """Convert a Markdown file to a styled HTML file.
    
    Args:
        input_file: Path to the input Markdown file
        output_file: Path to the output HTML file
    """
    try:
        # Read the markdown file
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_text = f.read()
        
        # Normalize markdown and convert to HTML
        markdown_text = normalize_markdown(markdown_text)
        html_content = markdown.markdown(
            markdown_text,
            extensions=["fenced_code", "tables", "codehilite", "sane_lists"],
            extension_configs={
                'codehilite': {
                    'guess_lang': False,
                    'noclasses': True,
                    'pygments_style': 'monokai'
                }
            },
            output_format="html5"
        )
        
        # Create HTML5 template with styling
        full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Converted Document</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.7;
            color: #333;
            margin: 0;
            padding: 2rem;
            background: #f6f7fb;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #1a202c;
            margin-top: 1.6rem;
            margin-bottom: 0.75rem;
        }}
        h1 {{ font-size: 2.4rem; }}
        h2 {{ font-size: 2rem; }}
        h3 {{ font-size: 1.6rem; }}
        p {{
            margin: 0 0 1rem 0;
        }}
        hr {{
            border: none;
            border-top: 1px solid #d2d6dc;
            margin: 2rem 0;
        }}
        a {{
            color: #1d4ed8;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        blockquote {{
            border-left: 4px solid #6b7280;
            padding: 1rem 1.25rem;
            margin: 1.5rem 0;
            background: #ffffff;
            color: #4b5563;
        }}
        ul, ol {{
            margin: 0 0 1rem 1.5rem;
            padding: 0;
        }}
        ul ul, ol ol, ul ol, ol ul {{
            margin-top: 0.5rem;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
            background: #ffffff;
        }}
        table th,
        table td {{
            border: 1px solid #d1d5db;
            padding: 0.75rem 0.9rem;
        }}
        table th {{
            background: #e5e7eb;
        }}
        code {{
            background-color: rgba(110, 118, 129, 0.4);
            padding: 0.15rem 0.3rem;
            border-radius: 0.3rem;
            font-family: Consolas, 'Courier New', monospace;
            font-size: 0.95rem;
            
        }}
        del {{
            text-decoration: line-through;
            color: #6b7280;
        }}
        ul li {{
            margin-bottom: 0.35rem;
        }}
        pre {{
            margin: 1rem 0;
            padding: 1rem;
            background: #0d1117;
            color: #d6deeb;
            overflow-x: auto;
            border-radius: 0.65rem;
            box-shadow: 0 1px 3px rgba(15, 23, 42, 0.12);
        }}
        pre code {{
            background: transparent;
            padding: 0;
            color: inherit;
            font-size: 0.95rem;
            white-space: pre-wrap;
        }}
        .codehilite {{
            background: #0d1117;
            color: #d6deeb;
        }}
        .codehilite .hll {{ background-color: #21262d }}
        .codehilite .c, .codehilite .cm, .codehilite .c1, .codehilite .cs {{ color: #6a737d; font-style: italic }}
        .codehilite .err {{ color: #f97583; background-color: #fff0f1 }}
        .codehilite .k, .codehilite .kc, .codehilite .kd, .codehilite .kn, .codehilite .kp, .codehilite .kr, .codehilite .gd, .codehilite .ne, .codehilite .se, .codehilite .si {{ color: #ff7b72 }}
        .codehilite .o, .codehilite .nb, .codehilite .nl, .codehilite .nf, .codehilite .nt, .codehilite .nv, .codehilite .ow, .codehilite .bp, .codehilite .vc, .codehilite .vg, .codehilite .vi, .codehilite .sr {{ color: #79c0ff }}
        .codehilite .ch, .codehilite .cp, .codehilite .go, .codehilite .gp, .codehilite .gu, .codehilite .ni {{ color: #8b949e }}
        .codehilite .ge {{ font-style: italic }}
        .codehilite .gi {{ color: #56d364 }}
        .codehilite .gs {{ font-weight: bold }}
        .codehilite .kt, .codehilite .m, .codehilite .no, .codehilite .mf, .codehilite .mh, .codehilite .mi, .codehilite .mo, .codehilite .il {{ color: #f2cc8f }}
        .codehilite .s, .codehilite .sb, .codehilite .sc, .codehilite .sd, .codehilite .s2, .codehilite .sh, .codehilite .sx, .codehilite .s1, .codehilite .ss {{ color: #a5d6ff }}
        .codehilite .nc, .codehilite .nd, .codehilite .nn {{ color: #7ee787 }}
        .codehilite .na {{ color: #ffab70 }}
        .codehilite .w {{ color: #c9d1d9 }}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""
        
        # Write the HTML to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
            
        print(f"Success! '{input_file}' has been converted to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' could not be found.")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a Markdown file to HTML.")
    parser.add_argument("input", nargs="?", help="Input Markdown file (e.g. sample.md)")
    parser.add_argument("-o", "--output", help="Output HTML file (optional). If omitted, uses the same basename with .html")
    args = parser.parse_args()

    if not args.input:
        print("Usage: python converter.py <input.md> [-o output.html]")
        sys.exit(1)

    input_file = os.path.join("import-MD", args.input)
    if args.output:
        output_file = os.path.join("export-HTML", args.output)
    else:
        output_file = os.path.join("export-HTML", os.path.splitext(args.input)[0] + ".html")

    convert_md_to_html(input_file, output_file)