#! /usr/bin/python
# Author: QA2.0 LIVE, V1.0
# Description: This program will demonstrate how to match string
# data using Regular Expressions.
"""
    Search a given file using regular expressions and display
    matched lines and groupings.
"""
import sys
import re

def search_pattern(pattern, file=r"C:\labs\words"):
    """ Display lines in a given file which match Regex """
    fh_in = open(file, mode="rt")

    # Iterate through file handle
    for line in fh_in:
        m = re.search(pattern, line) # Return None or RE Match object.
        if m:
            # The match object m has several methods with info about the match.
            print(f"Matched {m.group()} at char pos {m.start()} - {m.end()}, "
                  f"with groups {m.groups()}, "
                  f"first group is {m.groups()[0]}, " # Index tuple 0 = 1st
                  f"or {m.group(1)}") # More Pythonic way as 1 = 1st.

    fh_in.close()
    return None

def main():
    """ Demonstrate Regex groupings """
    search_pattern(r"^(.)(.).\2\1$") # Match lines 5 char palindromes.
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
