#!/usr/bin/python3
"""
A script to convert a Markdown file to an HTML file.
"""

import sys
import os

def convert_markdown_to_html(markdown_file, output_html):
    """Reads a Markdown file and writes it to an HTML file."""
    with open(markdown_file, 'r') as md_file:
        lines = md_file.readlines()

    with open(output_html, 'w') as html_file:
        for line in lines:
            html_file.write(line)

if __name__ == "__main__":
    # Check if the number of arguments is less than 3
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
    convert_markdown_to_html(markdown_file, output_html)
    sys.exit(0)