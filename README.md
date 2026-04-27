<div align="center">

<img src="assets/logo.png" alt="FileSort Pro Logo" width="220"/>

# FileSort Pro

**Intelligent Directory Organisation Tool**

[![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Version](https://img.shields.io/badge/Version-1.0.0-00D4AA?style=for-the-badge&logo=semantic-release&logoColor=white)](https://github.com/Infinite-Networker/FileSort-Pro/releases)
[![License](https://img.shields.io/badge/License-MIT-F7B731?style=for-the-badge&logo=open-source-initiative&logoColor=white)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-6C63FF?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Infinite-Networker/FileSort-Pro)
[![Status](https://img.shields.io/badge/Status-Stable-2ECC71?style=for-the-badge&logo=checkmarx&logoColor=white)](https://github.com/Infinite-Networker/FileSort-Pro)
[![Tests](https://img.shields.io/badge/Tests-Passing-27AE60?style=for-the-badge&logo=pytest&logoColor=white)](tests/)
[![Created By](https://img.shields.io/badge/Created%20By-Cherry%20Computer%20Ltd.-E74C3C?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Infinite-Networker/FileSort-Pro)

---

*A lightweight, high-performance Python CLI tool engineered to streamline directory organisation — developed by **Cherry Computer Ltd.***

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technical Specifications](#-technical-specifications)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Testing](#-testing)
- [Developer](#-developer)
- [Licence](#-licence)

---

## 🗂 Overview

**FileSort Pro** is a lightweight, Python-based command-line program engineered to streamline directory organisation. The utility scans a user-specified folder and generates a sorted list of files by name in **ascending lexicographical (A-Z) order**.

Designed for efficiency, it serves as a high-performance tool for users needing to manage cluttered directories through a simple yet elegant Command-Line Interface (CLI). FileSort Pro requires no third-party dependencies — built entirely on Python's robust standard library.

> *"Designed for efficiency. Built for reliability. Engineered by Cherry Computer Ltd."*

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔤 **Alphabetical Sorting** | Automatically identifies and arranges all files within a directory from A–Z using case-insensitive lexicographical ordering |
| 🎯 **Streamlined User Input** | Simple, intuitive prompt system — just enter the target folder path and let FileSort Pro do the rest |
| 🛡️ **Robust Error Handling** | Integrated mechanisms detect and report invalid directory paths, permission errors, and edge cases gracefully |
| ⚡ **Performance Optimised** | Built to run instantly — even directories with high file counts are processed without significant latency |
| 🎨 **Stylish CLI Interface** | Full ANSI colour-coded terminal output with animated spinners, Unicode file icons, and grouped A-Z sections |
| 👁️ **Hidden File Support** | Optional detection and display of hidden files (dotfiles) via `--hidden` flag |
| 📤 **Export Functionality** | Export your sorted file listing to a plain-text file with a single flag (`--export`) |
| 📝 **Persistent Logging** | All scan sessions are automatically logged to `filesort_pro.log` with timestamps |
| 📦 **Zero Dependencies** | Core functionality built entirely on Python's standard library (`os` module) |

---

## ⚙️ Technical Specifications

| Category | Specification |
|---|---|
| **Programming Language** | Python 3.7+ |
| **Core Libraries** | `os` (System File Management) |
| **Interface Type** | Command-Line Interface (CLI) |
| **Sorting Logic** | Lexicographical Ascending (A–Z), case-insensitive |
| **Error Handling** | Invalid paths, permission denied, empty directories |
| **Output Formats** | Styled terminal output · Plain-text export |
| **Logging** | File-based (`filesort_pro.log`) with timestamp |
| **Platform** | Windows · macOS · Linux |

---

## 📦 Installation

### Prerequisites

- **Python 3.7** or higher
- No third-party packages required for core use

### Clone the Repository

```bash
git clone https://github.com/Infinite-Networker/FileSort-Pro.git
cd FileSort-Pro
```

### (Optional) Install Development Dependencies

```bash
pip install -r requirements.txt
```

### (Optional) Install as a CLI Command

```bash
pip install .
# Then use from anywhere:
filesort-pro
```

---

## 🚀 Usage

### Interactive Mode

Run without arguments to launch the full interactive experience:

```bash
python filesort_pro.py
```

FileSort Pro will guide you through:
1. Entering the target directory path
2. Choosing whether to include hidden files
3. Choosing whether to export results

---

### Command-Line Mode

```bash
python filesort_pro.py [path] [options]
```

#### Arguments

| Argument | Description |
|---|---|
| `path` | Path to the directory to sort (defaults to current directory in interactive mode) |
| `--hidden`, `-H` | Include hidden files (dotfiles) in the output |
| `--export`, `-e` | Export sorted results to `filesort_output.txt` |
| `--help`, `-h` | Display the help message |

#### Examples

```bash
# Sort the current directory (interactive)
python filesort_pro.py

# Sort a specific directory
python filesort_pro.py /home/user/Documents

# Sort with hidden files included
python filesort_pro.py /home/user/Documents --hidden

# Sort and export results to file
python filesort_pro.py /home/user/Documents --export

# Full options
python filesort_pro.py /home/user/Documents --hidden --export

# Show help
python filesort_pro.py --help
```

---

### Example Output

```
  ███████╗██╗██╗     ███████╗███████╗ ██████╗ ██████╗ ████████╗
  ██╔════╝██║██║     ██╔════╝██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝
  █████╗  ██║██║     █████╗  ███████╗██║   ██║██████╔╝   ██║   
  ...
  ▸ SCAN RESULTS
  ──────────────────────────────────────────────────────────────
  Directory : /home/user/Documents
  Scanned   : 2025-07-31  14:22:07
  Scan Time : 0.83 ms
  ──────────────────────────────────────────────────────────────

  [ A ]
       1.  📝  annual_report.docx                   142.3 KB
       2.  🐍  automation_script.py                   4.1 KB

  [ B ]
       3.  📄  budget_overview.pdf                   88.7 KB

  [ C ]
       4.  📊  client_data.csv                       12.0 KB

  ──────────────────────────────────────────────────────────────
  ✔  Total:  4 visible  ·  2 hidden
```

---

## 📁 Project Structure

```
FileSort-Pro/
│
├── 📄  filesort_pro.py          # Main application — core logic & CLI
│
├── 🧪  tests/
│   └── test_filesort_pro.py    # Full unit test suite (unittest)
│
├── 🖼️  assets/
│   └── logo.png                # FileSort Pro official logo
│
├── 📋  README.md               # Project documentation (this file)
├── 📝  CHANGELOG.md            # Version history & release notes
├── 🤝  CONTRIBUTING.md         # Contribution guidelines
├── ⚙️  setup.py                # Package configuration for pip install
├── 📦  requirements.txt        # Optional development dependencies
└── ⚖️  LICENSE                 # MIT Licence
```

---

## 🔍 How It Works

FileSort Pro operates through a clean, three-stage pipeline:

```
┌─────────────────────────────────────────────────────────────┐
│                     FileSort Pro Pipeline                    │
├────────────────┬────────────────────┬────────────────────────┤
│  1. VALIDATE   │    2. SCAN         │    3. DISPLAY          │
│                │                    │                        │
│  • Path exists │  • os.listdir()    │  • ANSI colour output  │
│  • Is a dir    │  • Separate hidden │  • Grouped A-Z         │
│  • Readable    │  • Sort (A-Z)      │  • File icons + sizes  │
│                │  • Record timing   │  • Optional export     │
└────────────────┴────────────────────┴────────────────────────┘
```

### Core Algorithm

```python
# Sort logic — case-insensitive lexicographical ascending order
files = sorted(
    [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))],
    key=str.lower
)
```

The `os` module provides direct, cross-platform access to the filesystem without any external dependencies, keeping FileSort Pro lean, portable, and lightning-fast.

---

## 🧪 Testing

FileSort Pro ships with a comprehensive unit test suite covering all critical components.

### Run All Tests

```bash
pytest tests/ -v
```

### Run with Coverage Report

```bash
pytest tests/ -v --cov=filesort_pro --cov-report=term-missing
```

### Test Coverage

| Module | Tests |
|---|---|
| `TestPathValidation` | Valid directory · Non-existent path · File vs directory |
| `TestScanning` | Sorted order · Hidden separation · Empty dir · Case-insensitive · Timing |
| `TestExport` | File creation · Content accuracy · Header metadata |
| `TestHumanSize` | Bytes · KB · MB · GB · Zero bytes |
| `TestFileIcon` | Python · PDF · Image · Archive · Unknown · Empty ext |

---

## 👨‍💻 Developer

<div align="center">

| | |
|---|---|
| **Lead Developer** | Dr. Ahmad M. Ishanzai |
| **Date of Completion** | July 2025 |
| **Organisation** | Cherry Computer Ltd. |
| **Repository** | [github.com/Infinite-Networker/FileSort-Pro](https://github.com/Infinite-Networker/FileSort-Pro) |

</div>

---

## ⚖️ Licence

```
MIT License

Copyright (c) 2025 Cherry Computer Ltd.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
```

See [LICENSE](LICENSE) for the full licence text.

---

<div align="center">

<img src="assets/logo.png" alt="FileSort Pro" width="100"/>

**FileSort Pro** · Intelligent Directory Organisation

Made with ❤️ by **Cherry Computer Ltd.**

[![GitHub](https://img.shields.io/badge/GitHub-Infinite--Networker-181717?style=flat-square&logo=github)](https://github.com/Infinite-Networker/FileSort-Pro)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![MIT](https://img.shields.io/badge/Licence-MIT-F7B731?style=flat-square)](LICENSE)

</div>
