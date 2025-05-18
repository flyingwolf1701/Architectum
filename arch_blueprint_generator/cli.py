"""
Command Line Interface for the blueprint generator.
"""

import click
import json
import logging
import sys
from enum import Enum
from pathlib import Path
from typing import Optional

from arch_blueprint_generator.logging_config import setup_logging, logger
from arch_blueprint_generator.models.base import DetailLevel


@click.group()
@click.option(
    "--log-level",
    type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], case_sensitive=False),
    default="INFO",
    help="Set the logging level."
)
@click.option(
    "--log-file",
    type=click.Path(),
    help="Path to log file. If not specified, logs will be sent to console only."
)
def cli(log_level: str, log_file: Optional[str]) -> None:
    """Architectum Blueprint Generator CLI.
    
    Generate structured JSON blueprints of codebases for consumption by AI agents and visualization tools.
    """
    # Setup logging based on CLI options
    level = getattr(logging, log_level.upper())
    setup_logging(level=level, log_file=log_file)
    
    logger.debug("CLI initialized")


@cli.command(name="directory-blueprint")
@click.option(
    "--path",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True),
    required=True,
    help="Path to the target directory."
)
@click.option(
    "--depth",
    type=click.INT,
    default=0,
    help="Depth of directory traversal. 0 for all descendants, 1 for immediate children only, etc."
)
@click.option(
    "--level",
    type=click.Choice(["minimal", "standard", "detailed"], case_sensitive=False),
    default="minimal",
    help="Level of detail to include in the blueprint."
)
@click.option(
    "--output",
    type=click.Path(file_okay=True, dir_okay=False, writable=True),
    help="Path to output file. If not specified, output will be printed to console."
)
@click.option(
    "--pretty/--compact",
    default=True,
    help="Whether to pretty-print the JSON output."
)
def directory_blueprint(
    path: str,
    depth: int,
    level: str,
    output: Optional[str],
    pretty: bool
) -> None:
    """Generate a directory blueprint.
    
    This command is not yet implemented. It will generate a structured JSON representation
    of the specified directory, including files and subdirectories down to the specified depth.
    """
    try:
        detail_level = DetailLevel.from_string(level)
        logger.info(f"Generating directory blueprint for path={path}, depth={depth}, level={detail_level.name}")
        
        # Placeholder for actual implementation
        result = {
            "message": "Directory blueprint generation is not yet implemented.",
            "configuration": {
                "path": path,
                "depth": depth,
                "detail_level": detail_level.name
            }
        }
        
        # Format and output the result
        indent = 2 if pretty else None
        json_output = json.dumps(result, indent=indent)
        
        if output:
            output_path = Path(output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w") as f:
                f.write(json_output)
            logger.info(f"Output written to {output_path}")
        else:
            print(json_output)
    
    except Exception as e:
        logger.error(f"Error generating directory blueprint: {str(e)}", exc_info=True)
        sys.exit(1)


@cli.command(name="fileset-blueprint")
@click.option(
    "--files",
    type=str,
    required=True,
    help="Comma-separated list of file paths."
)
@click.option(
    "--level",
    type=click.Choice(["minimal", "standard", "detailed"], case_sensitive=False),
    default="minimal",
    help="Level of detail to include in the blueprint."
)
@click.option(
    "--output",
    type=click.Path(file_okay=True, dir_okay=False, writable=True),
    help="Path to output file. If not specified, output will be printed to console."
)
@click.option(
    "--pretty/--compact",
    default=True,
    help="Whether to pretty-print the JSON output."
)
def fileset_blueprint(
    files: str,
    level: str,
    output: Optional[str],
    pretty: bool
) -> None:
    """Generate a file set blueprint.
    
    This command is not yet implemented. It will generate a structured JSON representation
    of the specified set of files.
    """
    try:
        detail_level = DetailLevel.from_string(level)
        file_list = [f.strip() for f in files.split(",")]
        logger.info(f"Generating fileset blueprint for {len(file_list)} files, level={detail_level.name}")
        
        # Placeholder for actual implementation
        result = {
            "message": "FileSet blueprint generation is not yet implemented.",
            "configuration": {
                "files": file_list,
                "detail_level": detail_level.name
            }
        }
        
        # Format and output the result
        indent = 2 if pretty else None
        json_output = json.dumps(result, indent=indent)
        
        if output:
            output_path = Path(output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w") as f:
                f.write(json_output)
            logger.info(f"Output written to {output_path}")
        else:
            print(json_output)
    
    except Exception as e:
        logger.error(f"Error generating fileset blueprint: {str(e)}", exc_info=True)
        sys.exit(1)


@cli.command(name="codeelement-blueprint")
@click.option(
    "--file",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True),
    required=True,
    help="Path to the target file."
)
@click.option(
    "--elements",
    type=str,
    required=True,
    help="Comma-separated list of element names (functions, classes, methods)."
)
@click.option(
    "--level",
    type=click.Choice(["minimal", "standard", "detailed"], case_sensitive=False),
    default="minimal",
    help="Level of detail to include in the blueprint."
)
@click.option(
    "--output",
    type=click.Path(file_okay=True, dir_okay=False, writable=True),
    help="Path to output file. If not specified, output will be printed to console."
)
@click.option(
    "--pretty/--compact",
    default=True,
    help="Whether to pretty-print the JSON output."
)
def codeelement_blueprint(
    file: str,
    elements: str,
    level: str,
    output: Optional[str],
    pretty: bool
) -> None:
    """Generate a code element blueprint.
    
    This command is not yet implemented. It will generate a structured JSON representation
    of the specified code elements within the target file.
    """
    try:
        detail_level = DetailLevel.from_string(level)
        element_list = [e.strip() for e in elements.split(",")]
        logger.info(f"Generating code element blueprint for file={file}, elements={element_list}, level={detail_level.name}")
        
        # Placeholder for actual implementation
        result = {
            "message": "CodeElement blueprint generation is not yet implemented.",
            "configuration": {
                "file": file,
                "elements": element_list,
                "detail_level": detail_level.name
            }
        }
        
        # Format and output the result
        indent = 2 if pretty else None
        json_output = json.dumps(result, indent=indent)
        
        if output:
            output_path = Path(output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w") as f:
                f.write(json_output)
            logger.info(f"Output written to {output_path}")
        else:
            print(json_output)
    
    except Exception as e:
        logger.error(f"Error generating code element blueprint: {str(e)}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    cli()
