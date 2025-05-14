#!/usr/bin/env python3

import argparse
import subprocess
import sys
from pathlib import Path

# Usage:
#   python scripts/arch_extract.py extract --lang <language> <path>
#   python scripts/arch_extract.py diff-index <new.xml> <old.xml>
#
# Supported languages: python, typescript, kotlin, flutter
# Output: One XML per file, suitable for index generation and visualization

def extract_python(target_path: str):
    script_path = Path(__file__).parent / "extract_python.py"
    subprocess.run(["python3", str(script_path), target_path], check=True)

def extract_typescript(target_path: str):
    script_path = Path(__file__).parent / "extract_typescript.js"
    subprocess.run(["node", str(script_path), target_path], check=True)

def extract_kotlin(target_path: str):
    script_path = Path(__file__).parent / "extract_kotlin.py"
    subprocess.run(["python3", str(script_path), target_path], check=True)

def extract_flutter(target_path: str):
    script_path = Path(__file__).parent / "extract_flutter.py"
    subprocess.run(["python3", str(script_path), target_path], check=True)

def diff_index(current_path: str, previous_path: str):
    script_path = Path(__file__).parent / "arch_diff_index.py"
    subprocess.run(["python3", str(script_path), current_path, previous_path], check=True)

def main():
    parser = argparse.ArgumentParser(description="Arch: AI-first code structure extractor")
    subparsers = parser.add_subparsers(dest="command", required=True)

    extract_parser = subparsers.add_parser("extract", help="Extract code structure")
    extract_parser.add_argument("--lang", required=True, choices=["python", "typescript", "kotlin", "flutter"], help="Language to extract")
    extract_parser.add_argument("path", help="Path to source file or directory")

    diff_parser = subparsers.add_parser("diff-index", help="Diff two XML index files")
    diff_parser.add_argument("current", help="Path to current XML index")
    diff_parser.add_argument("previous", help="Path to previous XML index")

    args = parser.parse_args()

    if args.command == "extract":
        if args.lang == "python":
            extract_python(args.path)
        elif args.lang == "typescript":
            extract_typescript(args.path)
        elif args.lang == "kotlin":
            extract_kotlin(args.path)
        elif args.lang == "flutter":
            extract_flutter(args.path)
        else:
            print("Unsupported language")
            sys.exit(1)
    elif args.command == "diff-index":
        diff_index(args.current, args.previous)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
