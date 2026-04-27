# Contributing to FileSort Pro

Thank you for your interest in contributing to **FileSort Pro**!  
This project is developed and maintained by **Cherry Computer Ltd.**

---

## Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/your-username/FileSort-Pro.git
   cd FileSort-Pro
   ```
3. **Create a branch** for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

FileSort Pro requires only Python 3.7+. Install optional dev dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
pytest tests/ -v --cov=filesort_pro
```

## Code Style

- Follow **PEP 8** conventions
- Run `black filesort_pro.py` before committing
- Run `flake8 filesort_pro.py` to check for issues
- Add type hints where applicable (`mypy` compatible)

## Submitting a Pull Request

1. Ensure all tests pass
2. Update `CHANGELOG.md` with your changes
3. Push your branch and open a Pull Request against `main`
4. Describe your changes clearly in the PR description

## Code of Conduct

Be respectful, constructive, and professional in all interactions.

---

*Cherry Computer Ltd. — Lead Developer: Dr. Ahmad M. Ishanzai*
