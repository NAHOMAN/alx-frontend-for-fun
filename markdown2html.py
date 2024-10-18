#!/usr/bin/python3
"""
A script that converts a Markdown file to an HTML file.
"""

import sys
import os

def parse_markdown_line(line):
    """Convert a single line of markdown into HTML."""
    line = line.strip()  # Clean up leading/trailing spaces
    if line.startswith("# "):
        return f"<h1>{line[2:].strip()}</h1>"
    elif line.startswith("## "):
        return f"<h2>{line[3:].strip()}</h2>"
    elif line.startswith("### "):
        return f"<h3>{line[4:].strip()}</h3>"
    elif line.startswith("#### "):
        return f"<h4>{line[5:].strip()}</h4>"
    elif line.startswith("##### "):
        return f"<h5>{line[6:].strip()}</h5>"
    elif line.startswith("###### "):
        return f"<h6>{line[7:].strip()}</h6>"
    elif line:
        return f"<p>{line}</p>"  # Treat any non-heading non-empty line as a paragraph
    return ""  # Empty lines are ignored

def convert_markdown_to_html(markdown_content):
    """Convert a markdown text into corresponding HTML."""
    html_content = []
    for line in markdown_content.splitlines():
        html_line = parse_markdown_line(line)
        if html_line:  # Only add non-empty lines
            html_content.append(html_line)
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

        # Convert markdown content to HTML
        html_body = convert_markdown_to_html(markdown_content)

        # Write the HTML content to the output file
        with open(output_html, 'w') a