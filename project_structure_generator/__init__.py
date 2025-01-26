import os
import pkg_resources
from pathlib import Path

def get_default_config_path():
    """
    Get the path to the default configuration file.

    Returns:
        Path: Path to the default project configuration JSON
    """
    # Get the package root directory
    package_root = Path(pkg_resources.resource_filename('project_structure_generator', ''))

    # Navigate to the configs directory
    config_path = package_root.parent / 'configs' / 'project_config.json'

    return config_path
