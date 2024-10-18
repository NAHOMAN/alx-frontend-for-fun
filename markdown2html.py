#!/usr/bin/python3
"""
A script that converts a Markdown file to an HTML file.
"""

import sys
import os

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

        with open(output_html, 'w') as html_file:
            # Basic HTML structure wrapping the content of the Markdown file
            html_file.write(markdown_content)

<<<<<<< HEAD
if __name__ == "__main__":
    main()
=======
        # If everything succeeds, exit with 0
        sys.exit(0)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
>>>>>>> 8fa0df5c4ab6d325b159198a8323a1bf531e3cf2
