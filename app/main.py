#!/usr/bin/env python3
"""Minimal container runner: execute a program, relay stdout/stderr, exit with child code."""

import subprocess
import sys


def main():
    if len(sys.argv) < 4:
        print("Usage: main.py <ignored> <ignored> <command> [args...]", file=sys.stderr)
        sys.exit(1)
    command = sys.argv[3]
    args = sys.argv[4:]
    result = subprocess.run([command] + args)
    sys.exit(result.returncode)
