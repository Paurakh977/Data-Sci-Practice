# Data Science Practice Project

## Overview
This repository is a comprehensive practice platform for mastering Python programming, with a focus on building a strong foundation in core Python concepts and advancing into intermediate topics relevant to data science, artificial intelligence, and software development. It includes practical examples and exercises to deepen understanding and provide hands-on experience.

## Topics Covered
The project is organized into directories and files that cover the following key areas:

### Python Data Structures
- Dictionaries: Explore dictionary operations and manipulations (`dict_ex.py`).
- JSON: Handle JSON data processing and conversion (`json_ex.py`).
- Lists: Implement list operations, comprehensions, and advanced techniques (`list_ex.py`).
- Tuples: Understand tuple usage and immutability (`tuple_ex.py`).

### Python File Handling
- File operations: Learn file reading, writing, and data processing techniques (`file_handling/comprehensions.py`, `file_handling/context_managers.py`).

### Python Advanced Concepts
- Date and Time: Work with datetime objects and time manipulation (`file_handling/date_time.py`).
- Decorators: Implement and understand function decorators for code reuse (`file_handling/decorators_ex.py`).
- Generators: Explore memory-efficient iterable sequences (`file_handling/generators_ex.py`).
- Iterators: Understand iteration protocols and custom iterators (`file_handling/iterators.py`).
- Lambda Functions: Use anonymous functions for concise code (`file_handling/lambda_func.py`).
- Regular Expressions: Master pattern matching and text processing with regex (`file_handling/regex_ex.py`).

This structure allows users to progressively build skills from basic data structures to advanced Python features, with practical examples in each file.

## Prerequisites
Before installing and using this project, ensure you have the following:
- Python 3.9 or higher installed on your system.
- `uv` (a fast Python package manager) installed. You can install it via:
  ```bash
  pip install uv
  ```

## Installation
This project uses a `pyproject.toml` file for dependency management and project configuration. Follow these steps to set up the project:

1. **Clone the Repository**  
   Clone this repository to your local machine using:
   ```bash
   git clone <repository_url>
   cd Data-Science-Practice-Project
   ```

2. **Install Dependencies with UV**  
   Use `uv` to install the project dependencies listed in `pyproject.toml`. Run:
   ```bash
   uv pip install .
   ```
   This command will create a virtual environment (if not already present) and install all required packages, including any Python libraries specified in `pyproject.toml`.

3. **Verify Installation**  
   Ensure everything is set up correctly by running:
   ```bash
   uv pip check
   ```
   You can also test a sample script (e.g., `python Python/Data_Structures/list_ex.py`) to verify Python functionality.

## Usage
- Navigate to the relevant directory (e.g., `Python/Data_Structures` or `Python/File_Handling`) to explore and run the example scripts.
- Each `.py` file contains executable code with comments explaining the concepts and implementations.
- To run a specific script, use:
  ```bash
  python <script_name>.py
  ```

   For example, to explore list operations, run:
   ```bash
   python Python/Data_Structures/list_ex.py
   ```

## Project Structure
```
Data-Science-Practice-Project/
├── Python/
│   ├── Data_Structures/
│   │   ├── dict_ex.py
│   │   ├── json_ex.py
│   │   ├── list_ex.py
│   │   └── tuple_ex.py
│   └── File_Handling/
│       ├── comprehensions.py
│       ├── context_managers.py
│       ├── date_time.py
│       ├── decorators_ex.py
│       ├── generators_ex.py
│       ├── iterators.py
│       ├── lambda_func.py
│       └── regex_ex.py
├── pyproject.toml
├── README.md
└── Roadmap.pdf

```
## Roadmap
For detailed milestones, planned enhancements, and future topics, refer to the `Roadmap.pdf` file located in the root directory.

## Contributing
We welcome contributions to enhance this project! To contribute:
1. Fork the repository and create a new branch for your feature or bug fix.
2. Follow the existing code style and add comments where necessary.
3. Run any tests (if applicable) and ensure the code works as expected.
4. Submit a pull request with a clear description of your changes.

Please ensure your contributions align with the project’s goal of providing clear, educational Python examples.

## License
This project is licensed under the [MIT License](LICENSE) – see the `LICENSE` file for details.