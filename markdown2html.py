#!/usr/bin/python3
"""
A script that converts a Markdown file to an HTML file.
"""

import sys
import os

def convert_markdown_to_html(markdown_content):
    """Convert simple markdown headings to HTML."""
    html_content = []
    for line in markdown_content.splitlines():
        # Check for Markdown headings and convert them to HTML
        if line.startswith("# "):
            html_content.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            html_content.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("### "):
            html_content.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("#### "):
            html_content.append(f"<h4>{line[5:]}</h4>")
        elif line.startswith("##### "):
            html_content.append(f"<h5>{line[6:]}</h5>")
        elif line.startswith("###### "):
            html_content.append(f"<h6>{line[7:]}</h6>")
        else:
            html_content.append(line)  # For now, leave non-heading text unchanged
    
    return "\n".join(html_content)

if __name__ == "__main__":
    # Check if the number of arguments is less than 2
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_html = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Convert the Markdown file to HTML
    try:
        with open(markdown_file, 'r') as md_file:
            markdown_content = md_file.read()

        # Convert the markdown content to HTML format
        html_body = convert_markdown_to_html(markdown_content)

        # Write the output to the HTML file with basic HTML structure
        with open(output_html, 'w') as html_file:
            html_file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Markdown to HTML</title>\n</head>\n<body>\n")
            html_file.write(html_body)
            html_file.write("\n</body>\n</html>")

        # Successful execution
        sys.exit(0)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)