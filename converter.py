import markdown

def convert_md_to_html(input_file, output_file):
    try:
        # 1. Open and read the contents of the Markdown file
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_text = f.read()
        
        # 2. Use the markdown library to convert the text to HTML strings
        html_content = markdown.markdown(
            markdown_text,
            extensions=["fenced_code", "tables"],
            output_format="html5"
        )
        
        # 3. Wrap the content in a basic HTML5 skeleton so it renders properly in browsers
        full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Converted Document</title>
</head>
<body>
{html_content}
</body>
</html>"""
        
        # 4. Write the complete HTML string into the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
            
        print(f"Success! '{input_file}' has been converted to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' could not be found.")

# Run the function using our files
if __name__ == "__main__":
    convert_md_to_html("sample.md", "output.html")