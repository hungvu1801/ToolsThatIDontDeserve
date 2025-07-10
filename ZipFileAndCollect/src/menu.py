import os
import sys

from src.collect_files import collect_files
from src.zip_files import zip_files


def clear_console():
    """Clears the console screen based on the operating system."""
    if sys.platform.startswith('win'):
        os.system('cls')  # Command for Windows
    else:
        os.system('clear')

def run_command(choice: str="3") -> None:
    if choice == "1":
        print("ZIP Files...")
        zip_files()
        return 1
    elif choice == "2":
        print("Collect Files...")
        collect_files()
        return 1
    else:
        print("Exit program.")
        return 0

def display_menu():
    print("="*37)
    print(" Command Menu ".center(37, "="), end=None)
    print(f"|{' ' * 35}|")
    print("| 1. ZIP Files.".ljust(35), "|")
    print(f"|{' ' * 35}|", end=None)
    print("| 2. Collect Files.".ljust(35), "|")
    print(f"|{' ' * 35}|")
    print("| 3. Exit.".ljust(35), "|")
    print("="*37)
