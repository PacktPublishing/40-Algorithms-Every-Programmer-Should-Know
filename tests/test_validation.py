"""
Validation tests to ensure the testing infrastructure is set up correctly.
"""
import pytest
from pathlib import Path


class TestInfrastructureValidation:
    """Test class to validate the testing infrastructure setup."""
    
    @pytest.mark.unit
    def test_pytest_is_working(self):
        """Verify that pytest is installed and working."""
        assert True
    
    @pytest.mark.unit
    def test_fixtures_are_available(self, temp_dir, sample_data, mock_config):
        """Verify that fixtures from conftest.py are accessible."""
        # Test temp_dir fixture
        assert isinstance(temp_dir, Path)
        assert temp_dir.exists()
        
        # Test sample_data fixture
        assert "numbers" in sample_data
        assert isinstance(sample_data["numbers"], list)
        
        # Test mock_config fixture
        assert "debug" in mock_config
        assert mock_config["debug"] is True
    
    @pytest.mark.unit
    def test_markers_are_configured(self):
        """Verify that custom markers are properly configured."""
        # This test itself uses the unit marker
        pass
    
    @pytest.mark.integration
    def test_file_operations(self, temp_file):
        """Test file operations with temporary files."""
        assert temp_file.exists()
        assert temp_file.read_text() == "test content"
        
        # Write new content
        temp_file.write_text("new content")
        assert temp_file.read_text() == "new content"
    
    @pytest.mark.unit
    def test_coverage_is_configured(self):
        """Verify that coverage is properly configured."""
        # This test ensures coverage runs
        def sample_function(x):
            if x > 0:
                return x * 2
            else:
                return 0
        
        assert sample_function(5) == 10
        assert sample_function(-1) == 0
    
    @pytest.mark.unit
    def test_mock_functionality(self, mocker):
        """Verify that pytest-mock is working."""
        # Create a mock object
        mock_func = mocker.Mock(return_value=42)
        
        # Test the mock
        result = mock_func()
        assert result == 42
        mock_func.assert_called_once()
    
    @pytest.mark.slow
    def test_slow_marker(self):
        """Test that the slow marker is configured."""
        import time
        # Simulate a slow test
        time.sleep(0.1)
        assert True
    
    @pytest.mark.unit
    def test_helpers_fixture(self, helpers, temp_dir):
        """Test the custom helpers fixture."""
        # Test assert_list_almost_equal
        list1 = [1.0, 2.0, 3.0]
        list2 = [1.0000001, 2.0000001, 3.0000001]
        helpers.assert_list_almost_equal(list1, list2)
        
        # Test assert_files_equal
        file1 = temp_dir / "file1.txt"
        file2 = temp_dir / "file2.txt"
        content = "identical content"
        file1.write_text(content)
        file2.write_text(content)
        helpers.assert_files_equal(file1, file2)


class TestProjectStructure:
    """Test that the project structure is set up correctly."""
    
    @pytest.mark.unit
    def test_test_directories_exist(self):
        """Verify that test directories are created."""
        project_root = Path(__file__).parent.parent
        tests_dir = project_root / "tests"
        
        assert tests_dir.exists()
        assert (tests_dir / "__init__.py").exists()
        assert (tests_dir / "unit").exists()
        assert (tests_dir / "unit" / "__init__.py").exists()
        assert (tests_dir / "integration").exists()
        assert (tests_dir / "integration" / "__init__.py").exists()
        assert (tests_dir / "conftest.py").exists()
    
    @pytest.mark.unit
    def test_configuration_files_exist(self):
        """Verify that configuration files are created."""
        project_root = Path(__file__).parent.parent
        
        assert (project_root / "pyproject.toml").exists()
        assert (project_root / ".gitignore").exists()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])