import json
from pathlib import Path
from typing import Dict, Union, Optional, Any
import logging

class ProjectStructureCreator:
    """
    A class to create project structures based on JSON configuration.
    """

    def __init__(self,
                 base_path: Union[str, Path] = Path.cwd(),
                 logger: Optional[logging.Logger] = None):
        """
        Initialize ProjectStructureCreator.

        Args:
            base_path (Union[str, Path]): Base directory for project creation
            logger (logging.Logger, optional): Logger instance
        """
        # Create logger if not provided
        if logger is None:
            logger = logging.getLogger('project_creator')
            logger.setLevel(logging.INFO)

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)

            # Add handler if not already added
            if not logger.handlers:
                logger.addHandler(console_handler)

        self.base_path = Path(base_path)
        self.logger = logger

        # Ensure base path exists
        self.base_path.mkdir(parents=True, exist_ok=True)

    def _create_item(self, item_path: Path, item_content: Union[str, list, dict]) -> None:
        """
        Create a file or directory based on the item type.

        Args:
            item_path (Path): Path to the item to be created
            item_content (Union[str, list, dict]): Content or nested structure
        """
        try:
            # If it's a list or dict, it's a directory with contents
            if isinstance(item_content, (list, dict)):
                # Ensure directory exists
                item_path.mkdir(parents=True, exist_ok=True)

                # Recursively create contents
                if isinstance(item_content, list):
                    # List of files in this directory
                    for filename in item_content:
                        file_path = item_path / filename
                        file_path.touch(exist_ok=True)
                        self.logger.info(f"Created file: {file_path}")

                elif isinstance(item_content, dict):
                    # Nested directory structure
                    for subname, subcontent in item_content.items():
                        subpath = item_path / subname
                        self._create_item(subpath, subcontent)

            # If it's a string (potentially empty), create a file
            elif isinstance(item_content, str):
                item_path.touch(exist_ok=True)
                # If content is provided, write it
                if item_content:
                    item_path.write_text(item_content)
                self.logger.info(f"Created file: {item_path}")

            else:
                self.logger.warning(f"Unexpected content type for {item_path}: {type(item_content)}")

        except Exception as e:
            self.logger.error(f"Error creating {item_path}: {e}")

    def create_structure(self, structure: Dict[str, Any]) -> None:
        """
        Create project structure from configuration.

        Args:
            structure (Dict): Project structure configuration
        """
        try:
            # Iterate through top-level items in the structure
            for name, contents in structure.items():
                # Skip project_name if present
                if name == 'project_name':
                    continue

                # Create path for current item
                current_path = self.base_path / name

                # Create the item
                self._create_item(current_path, contents)

        except Exception as e:
            self.logger.error(f"Error creating project structure: {e}")

    @classmethod
    def create_from_config(cls,
                           config_file: Union[str, Path],
                           base_path: Union[str, Path] = Path.cwd()) -> 'ProjectStructureCreator':
        """
        Create project structure from a JSON configuration file.

        Args:
            config_file (Union[str, Path]): Path to config file
            base_path (Union[str, Path]): Base directory for project creation

        Returns:
            ProjectStructureCreator: Initialized instance with created structure
        """
        # Create an instance
        creator = cls(base_path)

        # Read configuration
        with open(config_file, 'r') as f:
            structure = json.load(f)

        # Create structure
        creator.create_structure(structure)

        return creator
