import argparse
import os
import re
import sys
import markdown

# Pre-compile regex patterns for better performance
_LIST_PATTERN = re.compile(r'^(?:\* |\+ |-|\d+\.\s)', re.MULTILINE)
_PREV_LINE_PATTERN = re.compile(r'^(?:\* |\+ |-|\d+\.\s|> |#{1,6} |---|\*\*\*|___)', re.MULTILINE)
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
        * {{
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.8;
            color: #333;
            margin: 0;
            padding: 2rem 1rem;
            background: linear-gradient(135deg, #f6f7fb 0%, #f0f2f9 100%);
            max-width: 900px;
            margin: 0 auto;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #1a202c;
            margin-top: 2rem;
            margin-bottom: 1rem;
            font-weight: 600;
            line-height: 1.3;
        }}
        h1 {{ 
            font-size: 2.5rem;
            border-bottom: 3px solid #1d4ed8;
            padding-bottom: 0.5rem;
        }}
        h2 {{ 
            font-size: 2rem;
            color: #1d4ed8;
        }}
        h3 {{ font-size: 1.6rem; }}
        h4 {{ font-size: 1.3rem; }}
        p {{
            margin: 1rem 0;
            text-align: justify;
        }}
        hr {{
            border: none;
            border-top: 2px solid #d2d6dc;
            margin: 2.5rem 0;
            opacity: 0.6;
        }}
        a {{
            color: #1d4ed8;
            text-decoration: none;
            transition: all 0.3s ease;
            border-bottom: 1px solid transparent;
        }}
        a:hover {{
            text-decoration: underline;
            border-bottom-color: #1d4ed8;
        }}
        a:focus {{
            outline: 2px solid #1d4ed8;
            outline-offset: 2px;
        }}
        blockquote {{
            border-left: 5px solid #1d4ed8;
            padding: 1.25rem 1.5rem;
            margin: 1.5rem 0;
            background: linear-gradient(90deg, rgba(29, 78, 216, 0.05) 0%, transparent 100%);
            color: #4b5563;
            font-style: italic;
            border-radius: 0.5rem;
        }}
        ul, ol {{
            margin: 1.5rem 0;
            padding-left: 2rem;
        }}
        ul ul, ol ol, ul ol, ol ul {{
            margin-top: 0.75rem;
            margin-bottom: 0.75rem;
        }}
        ul li, ol li {{
            margin-bottom: 0.75rem;
            line-height: 1.8;
        }}
        ul li::marker {{
            color: #1d4ed8;
            font-weight: 600;
        }}
        ol li::marker {{
            color: #1d4ed8;
            font-weight: 600;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 2rem 0;
            background: #ffffff;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
            border-radius: 0.5rem;
            overflow: hidden;
        }}
        table th {{
            background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
            color: white;
            font-weight: 600;
            padding: 1rem 0.9rem;
            text-align: left;
        }}
        table td {{
            border-bottom: 1px solid #e5e7eb;
            padding: 0.9rem;
        }}
        table tr:last-child td {{
            border-bottom: none;
        }}
        table tr:hover {{
            background: #f9fafb;
        }}
        code {{
            background: #f3f4f6;
            padding: 0.2rem 0.4rem;
            border-radius: 0.35rem;
            font-family: 'Courier New', Consolas, monospace;
            font-size: 0.9rem;
            color: #c41e3a;
        }}
        del {{
            text-decoration: line-through;
            color: #9ca3af;
            opacity: 0.7;
        }}
        pre {{
            margin: 1.5rem 0;
            padding: 1.25rem;
            background: #0d1117;
            color: #d6deeb;
            overflow-x: auto;
            border-radius: 0.65rem;
            box-shadow: 0 4px 12px rgba(13, 17, 23, 0.3);
            line-height: 1.6;
            font-size: 0.95rem;
        }}
        pre code {{
            background: transparent;
            padding: 0;
            color: inherit;
            font-size: inherit;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}
        pre::-webkit-scrollbar {{
            height: 8px;
        }}
        pre::-webkit-scrollbar-track {{
            background: #0d1117;
        }}
        pre::-webkit-scrollbar-thumb {{
            background: #30363d;
            border-radius: 4px;
        }}
        pre::-webkit-scrollbar-thumb:hover {{
            background: #484f58;
        }}
        .codehilite {{
            background: #0d1117;
            color: #d6deeb;
            border-radius: 0.65rem;
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
        input[type="checkbox"] {{
            margin-right: 0.5rem;
            cursor: pointer;
            accent-color: #1d4ed8;
        }}
        @media (max-width: 768px) {{
            body {{
                padding: 1.5rem 1rem;
            }}
            h1 {{ font-size: 2rem; }}
            h2 {{ font-size: 1.5rem; }}
            h3 {{ font-size: 1.25rem; }}
            table {{
                font-size: 0.9rem;
            }}
            table th, table td {{
                padding: 0.75rem 0.6rem;
            }}
            pre {{
                padding: 1rem;
                font-size: 0.85rem;
            }}
        }}
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
    parser.add_argument("input", nargs="?", help="Input Markdown file (e.g. README.md)")
    parser.add_argument("-o", "--output", help="Output HTML file (optional). If omitted, uses the same basename with .html")
    args = parser.parse_args()

    if not args.input:
        print("Usage: python converter.py <input.md> [-o output.html]")
        sys.exit(1)

    input_file = args.input
    output_file = args.output or os.path.splitext(input_file)[0] + ".html"

    convert_md_to_html(input_file, output_file)