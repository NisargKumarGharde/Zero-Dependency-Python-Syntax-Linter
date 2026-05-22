# Lightweight Python Syntax Linter

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="48" alt="Python" title="Python" /> &nbsp;
</p>

## Project Overview
A lightweight, zero-dependency command-line utility designed to statically analyze Python (`.py`) scripts for syntax errors prior to runtime execution. By leveraging Python's built-in `compile()` function, this tool provides instant feedback on code validity, making it a fast pre-commit check or CI/CD pipeline step.

## Features
- **Zero External Dependencies:** Built entirely using the Python Standard Library.
- **Fast Static Analysis:** Evaluates the Abstract Syntax Tree (AST) directly via `compile()` without actually executing the code.
- **Precise Error Reporting:** Catches `SyntaxError` exceptions and outputs the exact file name, line number, and error message.
- **Robust Exception Handling:** Gracefully handles missing files and invalid paths.

## Quick Start

1. Clone the repository and navigate to the directory.
2. Run the linter against any Python script using the `-f` (file) flag:
   ```bash
   python "Python Syntax Checker.py" -f "Sample Test Cases.py"
   ```
