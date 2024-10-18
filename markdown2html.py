#!/usr/bin/python3
"""
A script that converts a Markdown file to an HTML file.
"""

import sys
import os
import re

class MarkdownConverter:
    """A class to convert Markdown to HTML."""

    def __init__(self, markdown_file, output_file):
        self.markdown_file = markdown_file
        self.output_file = output_file

    def check_file_exists(self):
        """Check if the markdown file exists."""
        if not os.path.isfile(self.markdown_file):
            print(f"Missing {self.markdown_file}", file=sys.stderr)
            sys.exit(1)

    @staticmethod
    def parse_markdown(markdown_content):
        """Convert Markdown content to HTML."""
        html_lines = []
        for line in markdown_content.splitlines():
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            # Check for headings using regular expressions
            heading_match = re.match(r'^(#{1,6}) (.+)', line)
            if heading_match:
                level = len(heading_match.group(1))  # Count the number of '#' symbols
                title = heading_match.group(2).strip()
                html_lines.append(f"<h{level}>{title}</h{level}>")
            else:
                # Convert regular text to paragraph
                html_lines.append(f"<p>{line}</p>")
        return "\n".join(html_lines)

    def convert(self):
        """Read the Markdown file and write the HTML output."""
        with open(self.markdown_file, 'r') as md_file:
            markdown_content = md_file.read()
        html_body = self.parse_markdown(markdown_content)
        
        # Write the HTML content to the output file
        with open(self.output_file, 'w') as html_file:
            html_file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Markdown to HTML</title>\n</head>\n<body>\n")
            html_file.write(html_body)
            html_file.write("\n</body>\n</html>")

if __name__ == "__main__":
    # Validate the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Create a converter instance and process the file
    converter = MarkdownConverter(markdown_file, output_file)
    converter.check_file_exists()

    try:
        converter.convert()
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
