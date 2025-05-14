import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
import re

def extract_kotlin_api(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    component = ET.Element("Component", name=str(Path(file_path).stem), description="Extracted from Kotlin module")
    class_pattern = re.compile(r"class (\\w+)")
    fun_pattern = re.compile(r"fun (\\w+)\\s*\\((.*?)\\):?\\s*(\\w+)?")

    for line in lines:
        class_match = class_pattern.search(line)
        if class_match:
            ET.SubElement(component, "Type", name=class_match.group(1), kind="object")
            continue

        fun_match = fun_pattern.search(line)
        if fun_match:
            fn_el = ET.SubElement(component, "Function", name=fun_match.group(1), method="N/A", path="N/A")
            desc = ET.SubElement(fn_el, "Description")
            desc.text = f"Function {fun_match.group(1)} extracted from {file_path}"
            ET.SubElement(fn_el, "Returns", type=fun_match.group(3) or "unknown", reference="")
            ET.SubElement(fn_el, "Calls")
            ET.SubElement(fn_el, "CalledBy")

    return component

def write_xml(output_path, component):
    app = ET.Element("Application", name="auto_extracted", domain="kotlin")
    app.append(component)
    tree = ET.ElementTree(app)
    tree.write(output_path, encoding="utf-8", xml_declaration=True)

def main():
    input_path = sys.argv[1]
    input_path = Path(input_path)
    kt_files = []

    if input_path.is_dir():
        for root, _, files in os.walk(input_path):
            for file in files:
                if file.endswith(".kt"):
                    kt_files.append(Path(root) / file)
    else:
        kt_files = [input_path]

    for kt_file in kt_files:
        component = extract_kotlin_api(kt_file)
        out_file = kt_file.with_suffix(".xml").name
        write_xml(out_file, component)
        print(f"Extracted XML: {out_file}")

if __name__ == "__main__":
    main()
