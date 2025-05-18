"""
Tests for base models.
"""

import json
import pytest
from hypothesis import given, strategies as st
from pathlib import Path
from typing import Dict, List, Optional

from arch_blueprint_generator.models.base import (
    BlueprintError,
    BlueprintBase,
    CodeElement,
    DetailLevel,
    ElementKind,
    FileInfo,
    RelationshipInfo
)


class TestDetailLevel:
    """Tests for DetailLevel enum."""
    
    def test_from_string_valid(self):
        """Test conversion from valid strings to DetailLevel."""
        assert DetailLevel.from_string("minimal") == DetailLevel.MINIMAL
        assert DetailLevel.from_string("MINIMAL") == DetailLevel.MINIMAL
        assert DetailLevel.from_string("standard") == DetailLevel.STANDARD
        assert DetailLevel.from_string("STANDARD") == DetailLevel.STANDARD
        assert DetailLevel.from_string("detailed") == DetailLevel.DETAILED
        assert DetailLevel.from_string("DETAILED") == DetailLevel.DETAILED
    
    def test_from_string_invalid(self):
        """Test conversion from invalid strings raises ValueError."""
        with pytest.raises(ValueError):
            DetailLevel.from_string("invalid")
        
        with pytest.raises(ValueError):
            DetailLevel.from_string("")


class TestBlueprintError:
    """Tests for BlueprintError class."""
    
    def test_init(self):
        """Test initialization."""
        error = BlueprintError(
            message="Test error",
            path="/path/to/file",
            element_name="TestElement",
            exception=ValueError("Test exception")
        )
        
        assert error.message == "Test error"
        assert error.path == "/path/to/file"
        assert error.element_name == "TestElement"
        assert isinstance(error.exception, ValueError)
    
    def test_to_dict(self):
        """Test conversion to dictionary."""
        error = BlueprintError(
            message="Test error",
            path="/path/to/file",
            element_name="TestElement",
            exception=ValueError("Test exception")
        )
        
        error_dict = error.to_dict()
        
        assert error_dict["message"] == "Test error"
        assert error_dict["path"] == "/path/to/file"
        assert error_dict["element_name"] == "TestElement"
        assert error_dict["exception_type"] == "ValueError"


class TestFileInfo:
    """Tests for FileInfo class."""
    
    def test_init(self):
        """Test initialization."""
        file_info = FileInfo(
            path=Path("/path/to/file.py"),
            name="file.py",
            extension="py",
            is_directory=False,
            exists=True,
            size=1024
        )
        
        assert file_info.path == Path("/path/to/file.py")
        assert file_info.name == "file.py"
        assert file_info.extension == "py"
        assert file_info.is_directory is False
        assert file_info.exists is True
        assert file_info.size == 1024
        assert file_info.errors == []
    
    @given(
        path_str=st.text(min_size=1).map(lambda x: x.replace('\\', '/').replace(':', '')),
        name=st.text(min_size=1),
        extension=st.text(min_size=0, max_size=10),
        is_directory=st.booleans(),
        exists=st.booleans(),
        size=st.integers(min_value=0, max_value=10**6) | st.none()
    )
    def test_to_dict_property_based(
        self,
        path_str: str,
        name: str,
        extension: str,
        is_directory: bool,
        exists: bool,
        size: Optional[int]
    ):
        """Test conversion to dictionary using property-based testing."""
        # Create a valid path by prepending a slash
        valid_path = f"/{path_str}"
        
        file_info = FileInfo(
            path=Path(valid_path),
            name=name,
            extension=extension,
            is_directory=is_directory,
            exists=exists,
            size=size
        )
        
        file_dict = file_info.to_dict()
        
        assert file_dict["path"] == str(Path(valid_path))
        assert file_dict["name"] == name
        assert file_dict["extension"] == extension
        assert file_dict["is_directory"] == is_directory
        assert file_dict["exists"] == exists
        assert file_dict["size"] == size
        assert file_dict["errors"] is None
    
    def test_from_path_existing_file(self, tmp_path):
        """Test creating FileInfo from an existing file path."""
        # Create a temporary file
        test_file = tmp_path / "test_file.txt"
        test_file.write_text("Test content")
        
        file_info = FileInfo.from_path(test_file)
        
        assert file_info.path == test_file
        assert file_info.name == "test_file.txt"
        assert file_info.extension == "txt"
        assert file_info.is_directory is False
        assert file_info.exists is True
        assert file_info.size > 0
        assert file_info.errors == []
    
    def test_from_path_existing_directory(self, tmp_path):
        """Test creating FileInfo from an existing directory path."""
        file_info = FileInfo.from_path(tmp_path)
        
        assert file_info.path == tmp_path
        assert file_info.name == tmp_path.name
        assert file_info.extension == ""
        assert file_info.is_directory is True
        assert file_info.exists is True
        assert file_info.size is None
        assert file_info.errors == []
    
    def test_from_path_non_existing(self):
        """Test creating FileInfo from a non-existing path."""
        non_existing_path = Path("/path/that/does/not/exist")
        
        file_info = FileInfo.from_path(non_existing_path)
        
        assert file_info.path == non_existing_path
        assert file_info.name == "exist"
        assert file_info.exists is False
        assert len(file_info.errors) == 1
        assert "Error accessing file" in file_info.errors[0].message


class TestRelationshipInfo:
    """Tests for RelationshipInfo class."""
    
    def test_init(self):
        """Test initialization."""
        relationship = RelationshipInfo(
            source="ClassA",
            target="ClassB",
            relationship_type="inherits",
            source_location="/path/to/file_a.py",
            target_location="/path/to/file_b.py"
        )
        
        assert relationship.source == "ClassA"
        assert relationship.target == "ClassB"
        assert relationship.relationship_type == "inherits"
        assert relationship.source_location == "/path/to/file_a.py"
        assert relationship.target_location == "/path/to/file_b.py"
    
    def test_to_dict(self):
        """Test conversion to dictionary."""
        relationship = RelationshipInfo(
            source="ClassA",
            target="ClassB",
            relationship_type="inherits",
            source_location="/path/to/file_a.py",
            target_location="/path/to/file_b.py"
        )
        
        relationship_dict = relationship.to_dict()
        
        assert relationship_dict["source"] == "ClassA"
        assert relationship_dict["target"] == "ClassB"
        assert relationship_dict["relationship_type"] == "inherits"
        assert relationship_dict["source_location"] == "/path/to/file_a.py"
        assert relationship_dict["target_location"] == "/path/to/file_b.py"


class TestCodeElement:
    """Tests for CodeElement class."""
    
    def test_init(self):
        """Test initialization."""
        element = CodeElement(
            name="TestFunction",
            kind=ElementKind.FUNCTION,
            file_path=Path("/path/to/file.py")
        )
        
        assert element.name == "TestFunction"
        assert element.kind == ElementKind.FUNCTION
        assert element.file_path == Path("/path/to/file.py")
        assert element.relationships == []
    
    def test_to_dict(self):
        """Test conversion to dictionary."""
        relationship = RelationshipInfo(
            source="TestFunction",
            target="OtherFunction",
            relationship_type="calls"
        )
        
        element = CodeElement(
            name="TestFunction",
            kind=ElementKind.FUNCTION,
            file_path=Path("/path/to/file.py"),
            relationships=[relationship]
        )
        
        element_dict = element.to_dict()
        
        assert element_dict["name"] == "TestFunction"
        assert element_dict["kind"] == "FUNCTION"
        assert element_dict["file_path"] == str(Path("/path/to/file.py"))
        assert len(element_dict["relationships"]) == 1
        assert element_dict["relationships"][0]["source"] == "TestFunction"
        assert element_dict["relationships"][0]["target"] == "OtherFunction"
        assert element_dict["relationships"][0]["relationship_type"] == "calls"


class TestImplementationBlueprintBase:
    """Test implementation of BlueprintBase class."""
    
    class TestBlueprint(BlueprintBase):
        """Test implementation of BlueprintBase for testing."""
        
        def generate(self) -> Dict:
            """Generate test blueprint."""
            return {
                "detail_level": self.detail_level.name,
                "errors": [error.to_dict() for error in self.errors]
            }
    
    def test_init(self):
        """Test initialization."""
        blueprint = self.TestBlueprint(detail_level=DetailLevel.MINIMAL)
        
        assert blueprint.detail_level == DetailLevel.MINIMAL
        assert blueprint.errors == []
    
    def test_add_error(self):
        """Test adding an error."""
        blueprint = self.TestBlueprint()
        error = BlueprintError(message="Test error")
        
        blueprint.add_error(error)
        
        assert len(blueprint.errors) == 1
        assert blueprint.errors[0] == error
    
    def test_generate(self):
        """Test generate method."""
        blueprint = self.TestBlueprint(detail_level=DetailLevel.STANDARD)
        
        result = blueprint.generate()
        
        assert result["detail_level"] == "STANDARD"
        assert result["errors"] == []
    
    def test_to_json(self):
        """Test conversion to JSON string."""
        blueprint = self.TestBlueprint(detail_level=DetailLevel.DETAILED)
        
        json_str = blueprint.to_json()
        
        # Parse back to dict to verify structure
        result = json.loads(json_str)
        
        assert result["detail_level"] == "DETAILED"
        assert result["errors"] == []
