import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from difflib import unified_diff

def normalize_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8').splitlines(keepends=True)

def diff_xml_files(current_path, previous_path):
    current_lines = normalize_xml(current_path)
    previous_lines = normalize_xml(previous_path)
    diff = unified_diff(previous_lines, current_lines, fromfile=str(previous_path), tofile=str(current_path))
    return list(diff)

def main():
    if len(sys.argv) != 3:
        print("Usage: arch_extract.py diff-index <current.xml> <previous.xml>")
        sys.exit(1)

    current_xml = Path(sys.argv[1])
    previous_xml = Path(sys.argv[2])

    if not current_xml.exists() or not previous_xml.exists():
        print("Both XML files must exist.")
        sys.exit(1)

    diff = diff_xml_files(current_xml, previous_xml)
    if not diff:
        print("No differences found.")
    else:
        print("".join(diff))

if __name__ == "__main__":
    main()
