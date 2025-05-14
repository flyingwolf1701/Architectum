import ast
import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

def extract_api(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()
    tree = ast.parse(source, filename=file_path)

    component = ET.Element("Component", name=str(Path(file_path).stem), description="Extracted from Python module")

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            func = ET.SubElement(component, "Function", name=node.name, method="N/A", path="N/A")
            desc = ET.SubElement(func, "Description")
            desc.text = f"Function {node.name} extracted from {file_path}"
            ET.SubElement(func, "Returns", type="unknown", reference="")
            ET.SubElement(func, "Calls")
            ET.SubElement(func, "CalledBy")

        elif isinstance(node, ast.ClassDef):
            shape = ET.SubElement(component, "Type", name=node.name, kind="object")
            for stmt in node.body:
                if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
                    field_name = stmt.target.id
                    field_type = getattr(stmt.annotation, "id", "unknown")
                    ET.SubElement(shape, "Property", name=field_name, type=field_type, required="true")

    return component

def write_xml(output_path, component):
    app = ET.Element("Application", name="auto_extracted", domain="python")
    app.append(component)
    tree = ET.ElementTree(app)
    tree.write(output_path, encoding="utf-8", xml_declaration=True)

def main():
    input_path = sys.argv[1]
    input_path = Path(input_path)
    py_files = []

    if input_path.is_dir():
        for root, _, files in os.walk(input_path):
            for file in files:
                if file.endswith(".py"):
                    py_files.append(Path(root) / file)
    else:
        py_files = [input_path]

    for py_file in py_files:
        component = extract_api(py_file)
        out_file = py_file.with_suffix(".xml").name
        write_xml(out_file, component)
        print(f"Extracted XML: {out_file}")

if __name__ == "__main__":
    main()
