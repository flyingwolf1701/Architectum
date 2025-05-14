import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
import re

def extract_flutter_api(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    component = ET.Element("Component", name=str(Path(file_path).stem), description="Extracted from Flutter (Dart) module")
    class_pattern = re.compile(r"class (\w+)")
    method_pattern = re.compile(r"(\w+)\s+(\w+)\s*\((.*?)\)")

    for line in lines:
        class_match = class_pattern.search(line)
        if class_match:
            type_el = ET.SubElement(component, "Type", name=class_match.group(1), kind="object")
            continue

        method_match = method_pattern.search(line)
        if method_match and not line.strip().startswith("//"):
            fn_el = ET.SubElement(component, "Function", name=method_match.group(2), method="N/A", path="N/A")
            desc = ET.SubElement(fn_el, "Description")
            desc.text = f"Method {method_match.group(2)} extracted from {file_path}"
            ET.SubElement(fn_el, "Returns", type=method_match.group(1), reference="")
            ET.SubElement(fn_el, "Calls")
            ET.SubElement(fn_el, "CalledBy")

    return component

def write_xml(output_path, component):
    app = ET.Element("Application", name="auto_extracted", domain="flutter")
    app.append(component)
    tree = ET.ElementTree(app)
    tree.write(output_path, encoding="utf-8", xml_declaration=True)

def main():
    input_path = sys.argv[1]
    input_path = Path(input_path)
    dart_files = []

    if input_path.is_dir():
        for root, _, files in os.walk(input_path):
            for file in files:
                if file.endswith(".dart"):
                    dart_files.append(Path(root) / file)
    else:
        dart_files = [input_path]

    for dart_file in dart_files:
        component = extract_flutter_api(dart_file)
        out_file = dart_file.with_suffix(".xml").name
        write_xml(out_file, component)
        print(f"Extracted XML: {out_file}")

if __name__ == "__main__":
    main()
