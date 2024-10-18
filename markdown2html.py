#!/usr/bin/python3
"""
markdown2html.py module
This script converts Markdown files into HTML format.
"""

import sys
import os


def markdown_to_html(md_file, html_file):
    """
    Convert a Markdown file to HTML.
    Args:
        md_file (str): The input markdown file path.
        html_file (str): The output HTML file path.
    """
    try:
        with open(md_file, 'r') as f:
            md_content = f.readlines()

        html_content = []
        for line in md_content:
            # Simple markdown to HTML conversion
            if line.startswith("# "):
                html_content.append(f"<h1>{line[2:].strip()}</h1>\n")
            elif line.startswith("## "):
                html_content.append(f"<h2>{line[3:].strip()}</h2>\n")
            elif line.startswith("### "):
                html_content.append(f"<h3>{line[4:].strip()}</h3>\n")
            else:
                html_content.append(f"<p>{line.strip()}</p>\n")

        with open(html_file, 'w') as f:
            f.writelines(html_content)

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """
    Main function to handle the command-line interface and file conversion.
    """
    # Check if the number of arguments is less than 2
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(md_file):
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)

    # Convert markdown to HTML
    markdown_to_html(md_file, html_file)

    sys.exit(0)  # Exit with status 0 on success


if __name__ == "__main__":
    main()