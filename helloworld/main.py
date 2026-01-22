"""Top-level implementation of the helloworld program.

This module holds the actual application logic for the command-line program.

High-level flow:
1) Build an argparse.ArgumentParser at import-time (module load).
2) Expose a `main(argv=None)` function that:
   - determines the argument list (defaults to sys.argv),
   - validates CLI options (e.g., --help / --version),
   - prints the greeting,
   - returns an integer exit code.

Note: The repository root script `helloworld.py` and the installed console entrypoint
(defined in pyproject.toml) both call `helloworld.main:main`.
"""

import argparse
import sys

import helloworld

# Create the argument parser once at module import time.
# This keeps `main()` small and allows `--help`/`--version` to behave consistently
# whenever this module is used as a CLI entrypoint.
parser = argparse.ArgumentParser(
        description='A simple example program to print a friendly greeting.')
# `action='version'` is handled directly by argparse; it prints the given version string
# and exits cleanly without us needing to special-case it.
parser.add_argument('--version', action='version',
        version='helloworld ' + helloworld.__version__)


def main(argv=None):
    """Program entrypoint.

    Args:
        argv: Optional list of CLI arguments. If None, defaults to `sys.argv`.

    Returns:
        Process exit code as an int (0 indicates success).
    """
    # When called as a console script, argv will usually be None.
    # In that case we default to the real command-line arguments from the OS.
    if argv is None:
        argv = sys.argv

    # The helloworld program doesn't expect any positional arguments.
    # This parse step exists to:
    # - support standard `--help` and `--version` flags,
    # - and fail fast on unrecognized/extra arguments (argparse will print an error
    #   message and exit with a non-zero status automatically).
    parser.parse_args(argv[1:])

    # Core "business logic" of this example: print a friendly greeting.
    print("Hello, world")

    # Returning 0 signals success. The wrapper script/entrypoint will use this
    # as the process exit status (e.g., via sys.exit()).
    return 0
