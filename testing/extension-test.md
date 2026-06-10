---
title: Extension Test
author: Test Suite
---

[TOC]

# Markdown Extension Test

This test file includes examples for the newly added Markdown extensions and conversion behavior.

## Metadata

The document metadata above should be parsed by the `meta` extension.

## Admonition Example

!!! note "Important Note"
    This is an admonition block. It should render as a highlighted note section.

## Attribute Lists

A paragraph with a custom ID and classes.

This paragraph should get custom attributes.
{: #custom-paragraph .text-large data-role="example" }

## Tables

| Feature | Supported |
|--------:|:---------:|
| Extra syntax | ✅ |
| Meta block | ✅ |
| TOC generation | ✅ |
| Attribute lists | ✅ |
| Admonition | ✅ |

## Fenced Code Block

```python
def greet(name):
    return f"Hello, {name}!"
```

## Strikethrough and Checkbox

- [x] Completed task
- [ ] Remaining task

This text contains ~~deleted content~~ that should become a strikethrough.

## Nested List after Paragraph

A paragraph followed by a list should still render correctly.

- First item
- Second item
    - Nested item

## Headings and TOC

### Subheading A

Some content under subheading A.

### Subheading B

Some content under subheading B.
