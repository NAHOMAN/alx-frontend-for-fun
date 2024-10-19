#!/usr/bin/python3
"""
A script that converts a Markdown file to an HTML file.
"""

import sys
import os

def parse_heading(line):
    """
    Convert markdown heading syntax to HTML heading.
    Example: 
    # Heading 1 => <h1>Heading 1</h1>
    """
    heading_level = 0
    for char in line:
        if char == '#':
            heading_level += 1
        else:
            break
    
    # Ensure the line starts with heading markdown syntax
    if heading_level > 0 and heading_level <= 6 and line[heading_level] == ' ':
        heading_content = line[heading_level+1:].strip()  # Get the content after the #
        return f"<h{heading_level}>{heading_content}</h{heading_level}>"
    else:
        return line

def markdown_to_html(md_file, html_file):
    """
    Converts the content of a Markdown file to a simple HTML file.
    """
    try:
        with open(md_file, 'r') as md:
            markdown_content = md.readlines()

        with open(html_file, 'w') as html:
            for line in markdown_content:
                line = line.strip()
                
                # Check if the line is a heading and convert it
                if line.startswith('#'):
                    html.write(parse_heading(line) + '\n')
                else:
                    html.write(line + '\n')

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
