import os
import pkg_resources
from .project_structure_creator import ProjectStructureCreator
from .logger_setup import setup_logger


def get_config_path(filename='project_config.json'):
    return pkg_resources.resource_filename('project_structure_creator',
                                           os.path.join('..', 'configs', filename))

# No config parser import to avoid potential circular imports
__all__ = [
    'ProjectStructureCreator',
    'setup_logger'
]
