"""
Tests for CLI interface.
"""

import json
import os
import pytest
from click.testing import CliRunner
from pathlib import Path

from arch_blueprint_generator.cli import cli


@pytest.fixture
def runner():
    """Fixture for click CLI testing."""
    return CliRunner()


def test_cli_help(runner):
    """Test CLI help command."""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Architectum Blueprint Generator CLI" in result.output
    assert "directory-blueprint" in result.output
    assert "fileset-blueprint" in result.output
    assert "codeelement-blueprint" in result.output


def test_cli_logging_options(runner):
    """Test CLI logging options."""
    with runner.isolated_filesystem():
        log_file = "test_log.log"
        result = runner.invoke(cli, [
            "--log-level", "DEBUG",
            "--log-file", log_file,
            "directory-blueprint",
            "--path", ".",
            "--depth", "0",
            "--level", "minimal"
        ])
        
        assert result.exit_code == 0
        assert os.path.exists(log_file)
        
        with open(log_file, "r") as f:
            log_content = f.read()
            assert "DEBUG" in log_content
            assert "CLI initialized" in log_content


def test_directory_blueprint_basic(runner):
    """Test basic directory blueprint command."""
    with runner.isolated_filesystem():
        # Create a test directory
        os.makedirs("test_dir")
        
        result = runner.invoke(cli, [
            "directory-blueprint",
            "--path", "test_dir",
            "--depth", "1",
            "--level", "minimal"
        ])
        
        assert result.exit_code == 0
        
        # Parse the JSON output
        output = json.loads(result.output)
        
        assert "message" in output
        assert "not yet implemented" in output["message"]
        assert output["configuration"]["path"] == "test_dir"
        assert output["configuration"]["depth"] == 1
        assert output["configuration"]["detail_level"] == "MINIMAL"


def test_directory_blueprint_output_file(runner):
    """Test directory blueprint with output to file."""
    with runner.isolated_filesystem():
        # Create a test directory
        os.makedirs("test_dir")
        output_file = "output.json"
        
        result = runner.invoke(cli, [
            "directory-blueprint",
            "--path", "test_dir",
            "--output", output_file
        ])
        
        assert result.exit_code == 0
        assert os.path.exists(output_file)
        
        with open(output_file, "r") as f:
            output = json.loads(f.read())
            
            assert "message" in output
            assert "not yet implemented" in output["message"]
            assert output["configuration"]["path"] == "test_dir"


def test_directory_blueprint_invalid_path(runner):
    """Test directory blueprint with invalid path."""
    result = runner.invoke(cli, [
        "directory-blueprint",
        "--path", "/path/that/does/not/exist",
        "--depth", "1",
        "--level", "minimal"
    ])
    
    assert result.exit_code != 0


def test_fileset_blueprint_basic(runner):
    """Test basic fileset blueprint command."""
    result = runner.invoke(cli, [
        "fileset-blueprint",
        "--files", "file1.py,file2.py",
        "--level", "standard"
    ])
    
    assert result.exit_code == 0
    
    # Parse the JSON output
    output = json.loads(result.output)
    
    assert "message" in output
    assert "not yet implemented" in output["message"]
    assert output["configuration"]["files"] == ["file1.py", "file2.py"]
    assert output["configuration"]["detail_level"] == "STANDARD"


def test_codeelement_blueprint_basic(runner, tmp_path):
    """Test basic codeelement blueprint command."""
    # Create a test file
    test_file = tmp_path / "test_file.py"
    test_file.write_text("def test_function():\n    pass\n\nclass TestClass:\n    pass\n")
    
    result = runner.invoke(cli, [
        "codeelement-blueprint",
        "--file", str(test_file),
        "--elements", "test_function,TestClass",
        "--level", "detailed"
    ])
    
    assert result.exit_code == 0
    
    # Parse the JSON output
    output = json.loads(result.output)
    
    assert "message" in output
    assert "not yet implemented" in output["message"]
    assert output["configuration"]["file"] == str(test_file)
    assert output["configuration"]["elements"] == ["test_function", "TestClass"]
    assert output["configuration"]["detail_level"] == "DETAILED"


def test_invalid_detail_level(runner, tmp_path):
    """Test invalid detail level."""
    # Create a test file
    test_file = tmp_path / "test_file.py"
    test_file.write_text("# Test file")
    
    result = runner.invoke(cli, [
        "codeelement-blueprint",
        "--file", str(test_file),
        "--elements", "test_function",
        "--level", "invalid"
    ])
    
    assert result.exit_code != 0
    assert "Error: Invalid value for '--level'" in result.output
