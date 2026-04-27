#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════╗
║                        FileSort Pro                              ║
║              Intelligent Directory Organisation Tool             ║
║                                                                  ║
║  Lead Developer : Dr. Ahmad M. Ishanzai                          ║
║  Organisation   : Cherry Computer Ltd.                           ║
║  Version        : 1.0.0                                          ║
║  Completed      : July 31, 2025                                  ║
╚══════════════════════════════════════════════════════════════════╝

FileSort Pro is a lightweight, Python-based command-line program
engineered to streamline directory organisation. The utility scans
a user-specified folder and generates a sorted list of files by name
in ascending (A-Z) lexicographical order.
"""

import os
import sys
import time
import logging
from datetime import datetime
from typing import List, Optional, Tuple

# ─────────────────────────────────────────────
#  ANSI Colour Palette
# ─────────────────────────────────────────────
class Colours:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"

    # Foreground
    WHITE   = "\033[97m"
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE    = "\033[94m"
    GREY    = "\033[90m"

    # Background
    BG_BLACK = "\033[40m"
    BG_DARK  = "\033[48;5;232m"


# ─────────────────────────────────────────────
#  Logging Configuration
# ─────────────────────────────────────────────
LOG_FILE = "filesort_pro.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("FileSortPro")


# ─────────────────────────────────────────────
#  Banner & UI Helpers
# ─────────────────────────────────────────────
BANNER = f"""
{Colours.BOLD}{Colours.WHITE}
  ███████╗██╗██╗     ███████╗███████╗ ██████╗ ██████╗ ████████╗
  ██╔════╝██║██║     ██╔════╝██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝
  █████╗  ██║██║     █████╗  ███████╗██║   ██║██████╔╝   ██║   
  ██╔══╝  ██║██║     ██╔══╝  ╚════██║██║   ██║██╔══██╗   ██║   
  ██║     ██║███████╗███████╗███████║╚██████╔╝██║  ██║   ██║   
  ╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
{Colours.CYAN}                        ██████╗ ██████╗  ██████╗ 
                        ██╔══██╗██╔══██╗██╔═══██╗
                        ██████╔╝██████╔╝██║   ██║
                        ██╔═══╝ ██╔══██╗██║   ██║
                        ██║     ██║  ██║╚██████╔╝
                        ╚═╝     ╚═╝  ╚═╝ ╚═════╝ {Colours.RESET}
{Colours.GREY}  ─────────────────────────────────────────────────────────────
{Colours.WHITE}  Intelligent Directory Organisation Tool  {Colours.CYAN}v1.0.0
{Colours.GREY}  Lead Developer: {Colours.WHITE}Dr. Ahmad M. Ishanzai  {Colours.GREY}│  Organisation: {Colours.CYAN}Cherry Computer Ltd.
  ─────────────────────────────────────────────────────────────{Colours.RESET}
"""


def print_separator(char: str = "─", width: int = 65, colour: str = Colours.GREY) -> None:
    """Print a styled separator line."""
    print(f"{colour}{char * width}{Colours.RESET}")


def print_header(title: str) -> None:
    """Print a styled section header."""
    print(f"\n{Colours.BOLD}{Colours.CYAN}  ▸ {title}{Colours.RESET}")
    print_separator()


def print_success(message: str) -> None:
    print(f"  {Colours.GREEN}✔  {Colours.WHITE}{message}{Colours.RESET}")


def print_warning(message: str) -> None:
    print(f"  {Colours.YELLOW}⚠  {Colours.YELLOW}{message}{Colours.RESET}")


def print_error(message: str) -> None:
    print(f"  {Colours.RED}✘  {Colours.RED}{message}{Colours.RESET}")


def print_info(message: str) -> None:
    print(f"  {Colours.BLUE}ℹ  {Colours.WHITE}{message}{Colours.RESET}")


def animated_spinner(message: str, duration: float = 1.2) -> None:
    """Display a brief animated spinner."""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        frame = frames[i % len(frames)]
        sys.stdout.write(
            f"\r  {Colours.CYAN}{frame}{Colours.RESET}  {Colours.WHITE}{message}{Colours.RESET}"
        )
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write("\r" + " " * 70 + "\r")
    sys.stdout.flush()


# ─────────────────────────────────────────────
#  Core Logic
# ─────────────────────────────────────────────

class FileSortPro:
    """
    Core engine for FileSort Pro.

    Scans a directory, sorts files lexicographically (A-Z),
    and presents results via a styled CLI interface.
    """

    VERSION      = "1.0.0"
    ORGANISATION = "Cherry Computer Ltd."
    DEVELOPER    = "Dr. Ahmad M. Ishanzai"

    def __init__(self, path: str) -> None:
        self.path        : str            = os.path.abspath(path)
        self.files       : List[str]      = []
        self.hidden_files: List[str]      = []
        self.scan_time   : Optional[float] = None

    # ── Validation ──────────────────────────
    def validate_path(self) -> Tuple[bool, str]:
        """
        Validate the supplied directory path.

        Returns:
            (True, "") on success
            (False, reason) on failure
        """
        if not os.path.exists(self.path):
            return False, f"Path does not exist: '{self.path}'"
        if not os.path.isdir(self.path):
            return False, f"Path is not a directory: '{self.path}'"
        if not os.access(self.path, os.R_OK):
            return False, f"Permission denied — cannot read: '{self.path}'"
        return True, ""

    # ── Scanning ────────────────────────────
    def scan(self) -> None:
        """Scan the directory and separate visible from hidden files."""
        start = time.perf_counter()
        try:
            entries = os.listdir(self.path)
        except PermissionError as exc:
            logger.error("Permission error during scan: %s", exc)
            raise

        all_files    = [e for e in entries if os.path.isfile(os.path.join(self.path, e))]
        self.files        = sorted(
            [f for f in all_files if not f.startswith(".")],
            key=str.lower
        )
        self.hidden_files = sorted(
            [f for f in all_files if f.startswith(".")],
            key=str.lower
        )
        self.scan_time = time.perf_counter() - start
        logger.info("Scanned '%s' — %d visible, %d hidden files found in %.4fs",
                    self.path, len(self.files), len(self.hidden_files), self.scan_time)

    # ── Display ─────────────────────────────
    def display_results(self, show_hidden: bool = False) -> None:
        """Render sorted file list to the terminal."""
        print_header("SCAN RESULTS")
        print(f"  {Colours.GREY}Directory : {Colours.WHITE}{self.path}{Colours.RESET}")
        print(f"  {Colours.GREY}Scanned   : {Colours.WHITE}{datetime.now().strftime('%Y-%m-%d  %H:%M:%S')}{Colours.RESET}")
        print(f"  {Colours.GREY}Scan Time : {Colours.CYAN}{self.scan_time * 1000:.2f} ms{Colours.RESET}")
        print_separator()

        display_list = self.files + (self.hidden_files if show_hidden else [])

        if not display_list:
            print_warning("No files found in this directory.")
            return

        # Group by first letter for visual clarity
        current_letter = ""
        for idx, filename in enumerate(display_list, start=1):
            first_char = filename[0].upper() if not filename.startswith(".") else "·"

            if first_char != current_letter:
                current_letter = first_char
                print(
                    f"\n  {Colours.BOLD}{Colours.MAGENTA}[ {current_letter} ]{Colours.RESET}"
                )

            ext   = os.path.splitext(filename)[1].lower()
            icon  = _file_icon(ext)
            size  = _human_size(os.path.getsize(os.path.join(self.path, filename)))
            num   = f"{Colours.GREY}{idx:>4}.{Colours.RESET}"
            name  = f"{Colours.WHITE}{filename}{Colours.RESET}"
            meta  = f"{Colours.GREY}{size:>9}{Colours.RESET}"

            print(f"    {num}  {icon}  {name}  {meta}")

        print_separator()
        print(
            f"\n  {Colours.GREEN}✔  {Colours.BOLD}Total:{Colours.RESET}"
            f"  {Colours.CYAN}{len(self.files)}{Colours.RESET} visible"
            + (
                f"  ·  {Colours.GREY}{len(self.hidden_files)} hidden{Colours.RESET}"
                if self.hidden_files else ""
            )
        )

    # ── Export ──────────────────────────────
    def export_results(self, output_path: str = "filesort_output.txt") -> None:
        """Export sorted file list to a plain-text file."""
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write("FileSort Pro — Sorted Directory Listing\n")
                f.write(f"Generated by Cherry Computer Ltd. | {self.DEVELOPER}\n")
                f.write(f"Directory  : {self.path}\n")
                f.write(f"Timestamp  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total Files: {len(self.files)}\n")
                f.write("─" * 60 + "\n\n")
                for idx, name in enumerate(self.files, start=1):
                    size = _human_size(os.path.getsize(os.path.join(self.path, name)))
                    f.write(f"  {idx:>4}.  {name:<45}  {size:>9}\n")
            print_success(f"Results exported → {output_path}")
            logger.info("Results exported to '%s'", output_path)
        except OSError as exc:
            print_error(f"Export failed: {exc}")
            logger.error("Export error: %s", exc)


# ─────────────────────────────────────────────
#  Utility Helpers
# ─────────────────────────────────────────────

def _file_icon(ext: str) -> str:
    """Return a Unicode icon for common file extensions."""
    icons = {
        # Documents
        ".pdf": "📄", ".doc": "📝", ".docx": "📝", ".txt": "📃",
        ".md":  "📋", ".rst": "📋", ".odt":  "📝",
        # Spreadsheets
        ".xlsx": "📊", ".xls": "📊", ".csv": "📊", ".ods": "📊",
        # Images
        ".png": "🖼 ", ".jpg": "🖼 ", ".jpeg": "🖼 ", ".gif": "🖼 ",
        ".svg": "🖼 ", ".bmp": "🖼 ", ".webp": "🖼 ",
        # Audio / Video
        ".mp3": "🎵", ".wav": "🎵", ".flac": "🎵",
        ".mp4": "🎬", ".mov": "🎬", ".avi":  "🎬", ".mkv": "🎬",
        # Archives
        ".zip": "📦", ".tar": "📦", ".gz": "📦", ".rar": "📦", ".7z": "📦",
        # Code
        ".py":  "🐍", ".js": "📜", ".ts": "📜", ".html": "🌐",
        ".css": "🎨", ".json": "⚙ ", ".yaml": "⚙ ", ".toml": "⚙ ",
        ".sh":  "💻", ".bash": "💻", ".c": "💾", ".cpp": "💾",
        ".java": "☕", ".go": "🔵", ".rs": "🦀",
        # Executables
        ".exe": "⚡", ".bin": "⚡", ".dmg": "⚡",
    }
    return icons.get(ext, "📁")


def _human_size(num_bytes: int) -> str:
    """Convert bytes to a human-readable string."""
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if num_bytes < 1024.0:
            return f"{num_bytes:.1f} {unit}"
        num_bytes /= 1024.0
    return f"{num_bytes:.1f} PB"


# ─────────────────────────────────────────────
#  Interactive Menu
# ─────────────────────────────────────────────

def interactive_menu() -> None:
    """Run the interactive FileSort Pro session."""
    os.system("clear" if os.name != "nt" else "cls")
    print(BANNER)

    print_header("WELCOME")
    print_info("FileSort Pro — Intelligent Directory Organisation Tool")
    print_info(f"Created by {Colours.CYAN}Cherry Computer Ltd.{Colours.WHITE} · Lead Developer: Dr. Ahmad M. Ishanzai")
    print_separator()

    # ── Get directory path ───────────────────
    print(f"\n  {Colours.BOLD}{Colours.WHITE}Enter the path to the directory you wish to sort.{Colours.RESET}")
    print(f"  {Colours.GREY}(Type 'q' to quit, or press Enter to use current directory){Colours.RESET}\n")

    raw_input = input(f"  {Colours.CYAN}Directory Path › {Colours.WHITE}").strip()

    if raw_input.lower() in ("q", "quit", "exit"):
        print(f"\n  {Colours.YELLOW}Goodbye!{Colours.RESET}\n")
        sys.exit(0)

    target_path = raw_input if raw_input else os.getcwd()

    # ── Validate ─────────────────────────────
    sorter = FileSortPro(target_path)
    animated_spinner("Validating directory path…")

    valid, reason = sorter.validate_path()
    if not valid:
        print_error(reason)
        logger.warning("Validation failed: %s", reason)
        print()
        sys.exit(1)

    print_success(f"Directory validated: {sorter.path}")

    # ── Show hidden? ─────────────────────────
    show_h = input(
        f"\n  {Colours.CYAN}Include hidden files? {Colours.GREY}[y/N] › {Colours.WHITE}"
    ).strip().lower() in ("y", "yes")

    # ── Export? ─────────────────────────────
    do_export = input(
        f"  {Colours.CYAN}Export results to file? {Colours.GREY}[y/N] › {Colours.WHITE}"
    ).strip().lower() in ("y", "yes")

    # ── Scan ─────────────────────────────────
    animated_spinner("Scanning directory…", duration=1.0)
    sorter.scan()

    # ── Display ──────────────────────────────
    sorter.display_results(show_hidden=show_h)

    # ── Export ───────────────────────────────
    if do_export:
        default_out = "filesort_output.txt"
        out_name = input(
            f"\n  {Colours.CYAN}Output filename {Colours.GREY}[{default_out}] › {Colours.WHITE}"
        ).strip()
        sorter.export_results(out_name or default_out)

    # ── Footer ───────────────────────────────
    print(f"\n  {Colours.GREY}Log saved to: {Colours.WHITE}{LOG_FILE}{Colours.RESET}")
    print(f"\n  {Colours.DIM}© 2025 Cherry Computer Ltd.  ·  FileSort Pro v{FileSortPro.VERSION}{Colours.RESET}\n")


# ─────────────────────────────────────────────
#  CLI Entry-Point  (non-interactive)
# ─────────────────────────────────────────────

def cli_sort(path: str, show_hidden: bool = False, export: bool = False) -> None:
    """
    Non-interactive programmatic entry-point.

    Args:
        path        : Directory to sort.
        show_hidden : Whether to include hidden files.
        export      : Whether to export results to a text file.
    """
    sorter = FileSortPro(path)
    valid, reason = sorter.validate_path()
    if not valid:
        print_error(reason)
        sys.exit(1)

    sorter.scan()
    sorter.display_results(show_hidden=show_hidden)
    if export:
        sorter.export_results()


# ─────────────────────────────────────────────
#  Main
# ─────────────────────────────────────────────

def main() -> None:
    args = sys.argv[1:]

    if not args:
        # Full interactive experience
        interactive_menu()
        return

    # Simple CLI usage:  filesort_pro.py <path> [--hidden] [--export]
    path        = args[0]
    show_hidden = "--hidden" in args or "-H" in args
    do_export   = "--export" in args or "-e" in args

    if path in ("-h", "--help"):
        print(BANNER)
        print(f"  {Colours.BOLD}USAGE:{Colours.RESET}")
        print(f"    python filesort_pro.py [path] [options]\n")
        print(f"  {Colours.BOLD}OPTIONS:{Colours.RESET}")
        print(f"    {Colours.CYAN}--hidden, -H{Colours.RESET}   Include hidden files (dotfiles)")
        print(f"    {Colours.CYAN}--export, -e{Colours.RESET}   Export results to filesort_output.txt")
        print(f"    {Colours.CYAN}--help,   -h{Colours.RESET}   Show this help message\n")
        print(f"  {Colours.GREY}Examples:")
        print(f"    python filesort_pro.py                    # Interactive mode")
        print(f"    python filesort_pro.py /home/user/docs    # Sort specific directory")
        print(f"    python filesort_pro.py . --hidden --export{Colours.RESET}\n")
        return

    cli_sort(path, show_hidden=show_hidden, export=do_export)


if __name__ == "__main__":
    main()
