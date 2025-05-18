"""
Base data models for blueprint generation.

These models provide the foundation for representing code elements,
files, and blueprints in a structured format optimized for AI consumption.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum, auto
from pathlib import Path
from typing import Dict, List, Optional, Set, Union
import json


class DetailLevel(Enum):
    """Enum representing the level of detail for blueprint generation."""
    MINIMAL = auto()
    STANDARD = auto()
    DETAILED = auto()

    @classmethod
    def from_string(cls, value: str) -> 'DetailLevel':
        """Convert string to DetailLevel enum.
        
        Args:
            value: String representation of detail level
            
        Returns:
            Corresponding DetailLevel enum value
            
        Raises:
            ValueError: If the string doesn't match any detail level
        """
        normalized = value.upper()
        if normalized in cls.__members__:
            return cls[normalized]
        raise ValueError(f"Invalid detail level: {value}. Must be one of: minimal, standard, detailed")


class ElementKind(Enum):
    """Enum representing the kind of code element."""
    FUNCTION = auto()
    CLASS = auto()
    METHOD = auto()
    PROPERTY = auto()
    MODULE = auto()
    FILE = auto()
    DIRECTORY = auto()


@dataclass
class BlueprintError:
    """Represents an error that occurred during blueprint generation."""
    message: str
    path: Optional[str] = None
    element_name: Optional[str] = None
    exception: Optional[Exception] = None

    def to_dict(self) -> Dict:
        """Convert to dictionary representation."""
        return {
            "message": self.message,
            "path": self.path,
            "element_name": self.element_name,
            "exception_type": type(self.exception).__name__ if self.exception else None,
        }


@dataclass
class FileInfo:
    """Basic information about a file."""
    path: Path
    name: str
    extension: str
    is_directory: bool = False
    exists: bool = True
    size: Optional[int] = None
    errors: List[BlueprintError] = field(default_factory=list)

    @classmethod
    def from_path(cls, path: Union[str, Path]) -> 'FileInfo':
        """Create FileInfo from a path.
        
        Args:
            path: Path to file or directory
            
        Returns:
            FileInfo object with basic file information
        """
        path_obj = Path(path)
        try:
            return cls(
                path=path_obj,
                name=path_obj.name,
                extension=path_obj.suffix.lstrip('.'),
                is_directory=path_obj.is_dir(),
                exists=path_obj.exists(),
                size=path_obj.stat().st_size if path_obj.is_file() and path_obj.exists() else None
            )
        except Exception as e:
            return cls(
                path=path_obj,
                name=path_obj.name,
                extension=path_obj.suffix.lstrip('.'),
                exists=False,
                errors=[BlueprintError(
                    message=f"Error accessing file {path}: {str(e)}",
                    path=str(path_obj),
                    exception=e
                )]
            )

    def to_dict(self) -> Dict:
        """Convert to dictionary representation."""
        return {
            "path": str(self.path),
            "name": self.name,
            "extension": self.extension,
            "is_directory": self.is_directory,
            "exists": self.exists,
            "size": self.size,
            "errors": [error.to_dict() for error in self.errors] if self.errors else None
        }


@dataclass
class RelationshipInfo:
    """Information about relationships between code elements."""
    source: str
    target: str
    relationship_type: str  # e.g., "calls", "inherits", "imports"
    source_location: Optional[str] = None
    target_location: Optional[str] = None

    def to_dict(self) -> Dict:
        """Convert to dictionary representation."""
        return {
            "source": self.source,
            "target": self.target,
            "relationship_type": self.relationship_type,
            "source_location": self.source_location,
            "target_location": self.target_location
        }


@dataclass
class CodeElement:
    """Base class for representing a code element."""
    name: str
    kind: ElementKind
    file_path: Optional[Path] = None
    relationships: List[RelationshipInfo] = field(default_factory=list)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary representation."""
        return {
            "name": self.name,
            "kind": self.kind.name,
            "file_path": str(self.file_path) if self.file_path else None,
            "relationships": [r.to_dict() for r in self.relationships] if self.relationships else []
        }


class BlueprintBase(ABC):
    """Base class for all blueprint types."""
    
    def __init__(self, detail_level: DetailLevel = DetailLevel.MINIMAL):
        """Initialize blueprint.
        
        Args:
            detail_level: Level of detail to include in the blueprint
        """
        self.detail_level = detail_level
        self.errors: List[BlueprintError] = []
    
    def add_error(self, error: BlueprintError) -> None:
        """Add an error to the blueprint.
        
        Args:
            error: Error to add
        """
        self.errors.append(error)
    
    @abstractmethod
    def generate(self) -> Dict:
        """Generate the blueprint.
        
        Returns:
            Dictionary representation of the blueprint
        """
        pass
    
    def to_json(self, indent: int = 2) -> str:
        """Convert blueprint to JSON string.
        
        Args:
            indent: Number of spaces for indentation
            
        Returns:
            JSON string representation of the blueprint
        """
        return json.dumps(self.generate(), indent=indent)
