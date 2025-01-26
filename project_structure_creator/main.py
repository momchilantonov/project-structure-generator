import argparse
import sys
from pathlib import Path

# Use absolute imports from project_structure_creator
from project_structure_creator.project_structure_creator import ProjectStructureCreator
from project_structure_creator.logger_setup import setup_logger
from project_structure_creator import get_default_config_path

def create_project_cli():
    """
    Command-line interface for project structure creation.
    """
    # Create argument parser
    parser = argparse.ArgumentParser(description='Create project structure from JSON configurations.')

    # Mutually exclusive group for config selection
    config_group = parser.add_mutually_exclusive_group(required=True)

    config_group.add_argument(
        '-d', '--default',
        nargs='?',
        const=Path.cwd(),
        type=Path,
        help='Use default JSON project configuration (optional path)'
    )

    config_group.add_argument(
        '-c', '--custom',
        nargs='+',
        help='Use custom JSON configuration file (with optional path)'
    )

    # Parse arguments
    args = parser.parse_args()

    # Setup logger
    logger = setup_logger()

    try:
        # Determine config file and path
        if args.default is not None:
            # Default config
            config_file = get_default_config_path()
            project_path = args.default
        else:
            # Custom config
            if len(args.custom) == 1:
                # If only config file is provided
                config_file = Path(args.custom[0])
                project_path = Path.cwd()
            elif len(args.custom) == 2:
                # If config file and project path are provided
                config_file = Path(args.custom[0])
                project_path = Path(args.custom[1])
            else:
                raise ValueError("Invalid arguments for custom configuration")

        # Ensure project path exists
        project_path.mkdir(parents=True, exist_ok=True)

        # Create project structure
        ProjectStructureCreator.create_from_config(
            config_file=config_file,
            base_path=project_path
        )

        logger.info(f"Project structure created successfully in {project_path}")

    except Exception as e:
        logger.error(f"Failed to create project structure: {e}")
        sys.exit(1)

def main():
    """
    Main entry point for the application.
    """
    create_project_cli()

if __name__ == "__main__":
    main()
