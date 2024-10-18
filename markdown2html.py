#!/usr/bin/python3
import sys
import os

def markdown2html(md_file, html_file):
    try:
        with open(md_file, 'r') as md:
            markdown_content = md.read()

        # Convert Markdown to HTML (using simple text replacement as an example)
        html_content = markdown_content.replace("# ", "<h1>").replace("\n", "</h1>\n")

        with open(html_file, 'w') as html:
            html.write(html_content)

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.isfile(md_file):
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)

    markdown2html(md_file, html_file)
    sys.exit(0)

if __name__ == "__main__":
    main()
