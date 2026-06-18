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

## Why I Built This

[#why-i-built-this](#why-i-built-this)

Most Python linters (flake8, pylint, ruff) pull in their own dependency trees, which is overkill when all you need is a fast "will this even compile" check before a commit or CI step. This tool answers that one question using only the standard library, so it can run anywhere Python runs, with zero install friction.

## Engineering Decisions

[#engineering-decisions](#engineering-decisions)

**Why `compile()` instead of `ast.parse()`?** Both catch `SyntaxError`, but `compile()` also exercises Python's bytecode compilation step, catching a slightly broader class of structural issues while staying purely standard-library.

**Why CLI-first?** A `-f` flag interface makes it trivial to drop into a pre-commit hook or a CI step as a single shell command, without needing a config file or project setup.

## What's Next

[#whats-next](#whats-next)

- Support linting multiple files or glob patterns in one run
- Add a `.pre-commit-hooks.yaml` so it can be installed directly via the pre-commit framework
- Optional `--strict` mode for basic style checks (unused imports, line length) beyond pure syntax validity

## Quick Start

1. Clone the repository and navigate to the directory.
2. Run the linter against any Python script using the `-f` (file) flag:
   ```bash
   python "Python Syntax Checker.py" -f "Sample Test Cases.py"
   ```
