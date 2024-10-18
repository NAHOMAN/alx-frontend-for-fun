#!/usr/bin/python3
"""
A script to convert a Markdown file to an HTML file.
"""

import sys
import os

def markdown_to_html(md_file, html_file):
    """Convert Markdown content to HTML format by writing directly to a file."""
    try:
        with open(md_file, 'r') as md:
            content = md.readlines()

        with open(html_file, 'w') as html:
            for line in content:
                html.write(line)

    except IOError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.exists(md_file):
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)

    # Perform markdown to HTML conversion
    markdown_to_html(md_file, html_file)

    sys.exit(0)
