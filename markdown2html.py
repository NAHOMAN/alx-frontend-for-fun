#!/usr/bin/python3
"""
A script that converts a Markdown file to an HTML file.
"""

import sys
import os

def markdown_to_html(md_file, html_file):
    """
    Converts the content of a Markdown file to a simple HTML file.
    For now, this only copies the content directly.
    """
    try:
        with open(md_file, 'r') as md:
            markdown_content = md.read()

        with open(html_file, 'w') as html:
            # Currently, no markdown parsing is implemented, so the content is written directly.
            html.write(markdown_content)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

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

    # Call the function to convert markdown to html
    markdown_to_html(markdown_file, output_html)

    # Successful completion
    sys.exit(0)
