# Markdown Extended Features Demo

Here is a simple sentence referencing a footnote.[^1] 
You can also use named identifiers for your footnotes.[^technical-note]

## 1. Fenced Code Block
Below is a standard Python code block with syntax highlighting:

```python
def greet_user(name):
    """Print a simple greeting."""
    print(f"Hello, {name}!")

greet_user("Alice")
```

## 2. Definition List
Definition lists pair terms with their corresponding explanations:

Markdown
: A lightweight markup language with plain-text formatting syntax.

HTML
: HyperText Markup Language, the standard language for documents designed to be displayed in a web browser.

CSS
: Cascading Style Sheets, used for describing the presentation of a document written in a markup language.

## 3. Footnote Definitions
These definitions are automatically compiled and displayed at the bottom of the rendered page.

[^1]: This is the text for the first, simple footnote.
[^technical-note]: This is a more complex footnote. It uses an alphanumeric text identifier instead of just a single number.
