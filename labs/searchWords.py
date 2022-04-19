#! /bin/python
# Name:        searchWords.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Search and display lines in multiple files using
# Regular expressions
"""
    Pattern searching Tool
"""

import sys
import re

def main():
    """ Main Program """
    fh_in = open(r"C:\labs\words", mode="rt")

    pattern = input("Enter search pattern: ")
    for line in fh_in:
        m = re.search(pattern, line)
        if m:
            print(line, end="")

    fh_in.close()
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)