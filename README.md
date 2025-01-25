# Project Structure Creator

## Overview
A flexible utility for creating project structures from JSON configurations.

## Installation
```bash
pip install -e .
```

## Usage

### Default Configuration
Create a project structure using the default configuration in the current directory:
```bash
project-creator -d
```

Create a project structure using the default configuration in a specific directory:
```bash
project-creator -d /path/to/project
```

### Custom Configuration
Create a project structure using a custom JSON configuration in the current directory:
```bash
project-creator -c /path/to/config.json
```

Create a project structure using a custom JSON configuration in a specific directory:
```bash
project-creator -c /path/to/config.json /path/to/project
```

## Configuration File
The JSON configuration file should define the project structure. Example:

```json
{
  "src": {
    "core": {
      "utils": ["__init__.py", "helpers.py"],
      "models": ["__init__.py", "base_model.py"]
    }
  },
  "tests": ["__init__.py", "test_main.py"]
}
```

## License
[Specify your license]

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
