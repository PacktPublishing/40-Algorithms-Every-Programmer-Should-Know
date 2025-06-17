"""
Shared pytest fixtures and configuration for all tests.
"""
import os
import sys
import tempfile
import shutil
from pathlib import Path
from typing import Generator, Any, Dict, List
import pytest


# Add the project root to Python path to enable imports
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """
    Create a temporary directory for test files.
    
    Yields:
        Path: Path to the temporary directory
    """
    temp_path = Path(tempfile.mkdtemp())
    yield temp_path
    # Cleanup after test
    if temp_path.exists():
        shutil.rmtree(temp_path)


@pytest.fixture
def temp_file(temp_dir: Path) -> Generator[Path, None, None]:
    """
    Create a temporary file for testing.
    
    Args:
        temp_dir: Temporary directory fixture
        
    Yields:
        Path: Path to the temporary file
    """
    temp_file_path = temp_dir / "test_file.txt"
    temp_file_path.write_text("test content")
    yield temp_file_path


@pytest.fixture
def sample_data() -> Dict[str, Any]:
    """
    Provide sample data for testing algorithms.
    
    Returns:
        Dict containing various sample data structures
    """
    return {
        "numbers": [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
        "sorted_numbers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "strings": ["apple", "banana", "cherry", "date", "elderberry"],
        "matrix": [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        "graph": {
            "A": ["B", "C"],
            "B": ["A", "D", "E"],
            "C": ["A", "F"],
            "D": ["B"],
            "E": ["B", "F"],
            "F": ["C", "E"]
        }
    }


@pytest.fixture
def mock_config() -> Dict[str, Any]:
    """
    Provide mock configuration for testing.
    
    Returns:
        Dict containing test configuration
    """
    return {
        "debug": True,
        "max_iterations": 100,
        "threshold": 0.01,
        "output_dir": "/tmp/test_output",
        "algorithm_params": {
            "learning_rate": 0.01,
            "batch_size": 32,
            "epochs": 10
        }
    }


@pytest.fixture
def sample_csv_data(temp_dir: Path) -> Path:
    """
    Create a sample CSV file for testing.
    
    Args:
        temp_dir: Temporary directory fixture
        
    Returns:
        Path to the created CSV file
    """
    csv_path = temp_dir / "sample.csv"
    csv_content = """id,name,value
1,Alice,100
2,Bob,200
3,Charlie,300
4,David,400
5,Eve,500"""
    csv_path.write_text(csv_content)
    return csv_path


@pytest.fixture
def sample_json_data(temp_dir: Path) -> Path:
    """
    Create a sample JSON file for testing.
    
    Args:
        temp_dir: Temporary directory fixture
        
    Returns:
        Path to the created JSON file
    """
    import json
    json_path = temp_dir / "sample.json"
    json_data = {
        "users": [
            {"id": 1, "name": "Alice", "active": True},
            {"id": 2, "name": "Bob", "active": False},
            {"id": 3, "name": "Charlie", "active": True}
        ],
        "settings": {
            "theme": "dark",
            "notifications": True
        }
    }
    json_path.write_text(json.dumps(json_data, indent=2))
    return json_path


@pytest.fixture(autouse=True)
def reset_random_seed():
    """
    Reset random seed before each test for reproducibility.
    """
    import random
    
    random.seed(42)
    try:
        import numpy as np
        np.random.seed(42)
    except ImportError:
        pass  # NumPy might not be installed


@pytest.fixture
def capture_stdout() -> Generator[List[str], None, None]:
    """
    Capture stdout during test execution.
    
    Yields:
        List that will contain captured output lines
    """
    import io
    from contextlib import redirect_stdout
    
    captured_lines = []
    string_io = io.StringIO()
    
    with redirect_stdout(string_io):
        yield captured_lines
    
    captured_lines.extend(string_io.getvalue().splitlines())


# Markers for different test types
def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )


# Custom assertions
class Helpers:
    """Helper methods for tests."""
    
    @staticmethod
    def assert_files_equal(file1: Path, file2: Path) -> None:
        """Assert that two files have identical content."""
        assert file1.read_text() == file2.read_text()
    
    @staticmethod
    def assert_list_almost_equal(list1: List[float], list2: List[float], tolerance: float = 1e-6) -> None:
        """Assert that two lists of floats are almost equal."""
        assert len(list1) == len(list2)
        for a, b in zip(list1, list2):
            assert abs(a - b) < tolerance


@pytest.fixture
def helpers() -> Helpers:
    """Provide helper methods for tests."""
    return Helpers()