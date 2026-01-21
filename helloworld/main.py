"""Top-level implementation of the helloworld program.

This module contains the actual implementation of the CLI program.
The repository also includes a small wrapper script (`helloworld.py`) that
imports this module and calls `main()`. When installed, an entry point is also
created that points at `helloworld.main:main`.

Overall flow:
1) Define an argparse.ArgumentParser at import time (global `parser`).
2) In `main()`, normalize argv, validate CLI args (only --help/--version).
3) Print the greeting.
4) Return an exit code (0 for success).
"""

import argparse
import sys

import helloworld


# Create the CLI argument parser once at module import time.
# This keeps `main()` small and makes the parser reusable if the module is
# imported by other code.
parser = argparse.ArgumentParser(
        description='A simple example program to print a friendly greeting.')
# `action='version'` makes argparse handle `--version` automatically:
# it prints the version string and exits before the rest of main() runs.
parser.add_argument('--version', action='version',
        version='helloworld ' + helloworld.__version__)


# PUBLIC_INTERFACE
def main(argv=None):
    """Program entry point used by both the wrapper script and the installed CLI.

    Args:
        argv: Optional list of command-line arguments. If None, defaults to
            sys.argv (the real command line).

    Returns:
        int: Process exit code (0 indicates success).
    """
    # Allow callers (including tests) to pass an explicit argv; otherwise use the
    # actual command line.
    if argv is None:
        argv = sys.argv

    # The helloworld program doesn't expect any arguments.
    # This parse step has two purposes:
    #   - It supports standard `--help` and `--version` behavior.
    #   - It rejects unexpected/unrecognized arguments so users get a helpful
    #     error message instead of silently ignoring them.
    #
    # We intentionally parse argv[1:] to skip the program name at argv[0].
    parser.parse_args(argv[1:])

    # Core behavior of the program: print a friendly greeting.
    print("Hello, world")

    # Return a conventional success status code for the OS/shell.
    return 0
