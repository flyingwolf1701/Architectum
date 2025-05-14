import os
import xml.etree.ElementTree as ET
import yaml
from pathlib import Path

PLAN_PATH = Path("architectum/instructions/plan.yaml")
STRUCTURE_DIR = Path("architectum/structure")
OUTPUT_DIR = STRUCTURE_DIR


def load_plan():
    with open(PLAN_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def collect_files(folders):
    xml_files = []
    for folder in folders:
        path = STRUCTURE_DIR / folder
        if path.exists():
            for root, _, files in os.walk(path):
                for file in files:
                    if file.endswith(".xml"):
                        xml_files.append(Path(root) / file)
    return xml_files


def merge_index(group_name, xml_files):
    root = ET.Element("Application", name=f"index_{group_name}", domain="composite")
    for file in xml_files:
        tree = ET.parse(file)
        for component in tree.getroot().findall("Component"):
            root.append(component)
    ET.ElementTree(root).write(OUTPUT_DIR / f"{group_name}_index.xml", encoding="utf-8", xml_declaration=True)
    print(f"Wrote: {group_name}_index.xml")


def main():
    plan = load_plan()
    for group, folders in plan.get("xml_groups", {}).items():
        files = collect_files(folders)
        merge_index(group, files)


if __name__ == "__main__":
    main()
