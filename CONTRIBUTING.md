# Contributing to show-file-tree

First off, thank you for considering contributing! Your help is greatly appreciated 🙌  

This document outlines the guidelines and best practices for contributing to **show-file-tree**, a small but powerful CLI tool for visualizing file and folder structures.  

---

## 🚀 How Can I Contribute?

### Reporting Bugs
- First, check if the bug has already been reported under **GitHub Issues**.  
- If not, open a new issue with:  
  - A **clear title and description**.  
  - Steps to reproduce the issue.  
  - A minimal code sample or test case showing the problem.  
  - Expected vs actual behavior.  

### Suggesting Enhancements
- Open a new issue with your enhancement idea.  
- Provide:  
  - A **clear description** of the proposed enhancement.  
  - The **benefit** it brings to users.  
  - Example use cases, if possible.  

### Pull Requests
1. **Fork the repo** and create your branch from `main`.  
2. **Set up your development environment**:  

   ```
   # Clone your fork
   git clone https://github.com/YOUR_USERNAME/show-file-tree.git
   cd show-file-tree
   ```

   ```
   # Create a virtual environment and activate it
   python -m venv .venv
   source .venv/bin/activate   # (Linux/macOS)
   .venv\Scripts\activate      # (Windows PowerShell)
   ```
   
   ```
   # Install dependencies for development
   pip install -e ".[all]"
   pip install pytest
   ```

3. **Make changes** and add tests for your feature or bug fix.
4. Run the test suite: [**pytest**](https://github.com/pytest-dev/pytest)
5. Format your code with [**Black**](https://github.com/psf/black) or [**Ruff**](https://github.com/astral-sh/ruff).
6. Commit your changes with a clear message.
7. Push your branch and **open a Pull Request** (PR).

---

## 📝 Branching Convention

| Prefix      | Purpose                                   | Example Branch Name     |
| ----------- | ----------------------------------------- | ----------------------- |
| `feature/`  | New features or functionality             | `feature/add-cli-tree`  |
| `fix/`      | Bug fixes or small corrections            | `fix/fix-path-handling` |
| `docs/`     | Documentation changes                     | `docs/update-readme`    |
| `wip/`      | Work-in-progress experiments              | `wip/template`          |
| `chore/`    | Misc tasks like setup, CI, configs        | `chore/add-gitignore`   |
| `refactor/` | Code restructuring without feature change | `refactor/cleanup-code` |

---

## ✅ Coding Standards

* Follow **[PEP 8](https://peps.python.org/pep-0008/)** style guidelines.
* Keep functions small, modular, and well-structured.
* Add **docstrings** to all public modules, functions, classes, and methods.
* Write **clear, readable commit messages**:

  * `Add: new feature xyz`
  * `Fix: bug in path handling`
  * `Docs: update contributing guide`

---

## 🧪 Testing

* Add or update tests for any new code.
* Run the full test suite with:

  ```bash
  pytest
  ```
* Ensure all tests pass before submitting a PR.

---

## 🙌 Ways to Contribute

* Report bugs
* Suggest enhancements
* Submit pull requests (features, bug fixes, documentation)
* Improve docs (README, examples, etc.)

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as this project (MIT).

