#!/usr/bin/env python3
"""
A simple script to convert a TELOS Markdown file into a JSON structure. This
script looks for second-level headings (lines starting with "##") and
collects bullet list items under each section. It adds a version and updated
field for metadata. The output can be written to a file or printed.
"""
import sys
import json
import re
import os
import datetime


def parse_markdown(md: str) -> dict:
    """Parse a TELOS markdown document into a dict keyed by section names.

    Sections are identified by lines starting with '## '. Bullet list items
    starting with '- ' or '* ' are collected under the current section.
    """
    data: dict[str, list] = {}
    current_section: str | None = None
    lines = md.splitlines()
    for line in lines:
        stripped = line.strip()
        # Identify new section by second-level heading
        if stripped.startswith("## "):
            section_name = stripped[3:].strip().lower().replace(" ", "_")
            current_section = section_name
            data[current_section] = []
        # Collect bullet list items
        elif stripped.startswith("- ") or stripped.startswith("* "):
            item = stripped[2:].strip()
            if current_section is not None:
                data[current_section].append(item)
    return data


#!/usr/bin/env python3
"""
A simple script to convert a TELOS Markdown file into a JSON structure. This
script looks for second-level headings (lines starting with "##") and
collects bullet list items under each section. It adds a version and updated
field for metadata. The output can be written to a file or printed.
"""
import sys
import json
import re
import os
import datetime


def parse_markdown(md: str) -> dict:
    """Parse a TELOS markdown document into a dict keyed by section names.

    Sections are identified by lines starting with '## '. Bullet list items
    starting with '- ' or '* ' are collected under the current section.
    """
    data: dict[str, list] = {}
    current_section: str | None = None
    lines = md.splitlines()
    for line in lines:
        stripped = line.strip()
        # Identify new section by second-level heading
        if stripped.startswith("## "):
            section_name = stripped[3:].strip().lower().replace(" ", "_")
            current_section = section_name
            data[current_section] = []
        # Collect bullet list items
        elif stripped.startswith("- ") or stripped.startswith("* "):
            item = stripped[2:].strip()
            if current_section is not None:
                data[current_section].append(item)
    return data


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Convert TELOS Markdown to JSON")
    parser.add_argument("input_md", help="Path to the input TELOS markdown file")
    parser.add_argument(
        "-o", "--output", help="Output JSON file path. If omitted, prints to stdout", default=None
    )
    args = parser.parse_args()

    with open(args.input_md, encoding="utf-8") as f:
        md = f.read()
    data = parse_markdown(md)

    # Add metadata fields
    data["version"] = "1.0.0"
    data["updated"] = datetime.datetime.utcnow().isoformat() + "Z"

    json_text = json.dumps(data, indent=2)
    if args.output:
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as out:
            out.write(json_text)
    else:
        print(json_text)


if __name__ == "__main__":
    main()
def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Convert TELOS Markdown to JSON")
    parser.add_argument("input_md", help="Path to the input TELOS markdown file")
    parser.add_argument(
        "-o", "--output", help="Output JSON file path. If omitted, prints to stdout", default=None
    )
    args = parser.parse_args()

    with open(args.input_md, encoding="utf-8") as f:
        md = f.read()
    data = parse_markdown(md)

    # Add metadata fields
    data["version"] = "1.0.0"
    data["updated"] = datetime.datetime.utcnow().isoformat() + "Z"

    json_text = json.dumps(data, indent=2)
    if args.output:
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as out:
            out.write(json_text)
    else:
        print(json_text)


if __name__ == "__main__":
    main()
