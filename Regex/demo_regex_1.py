#! /usr/bin/python
# Author: QA2.0 LIVE, V1.0
# Description: This program will demonstrate how to match string
# data using Regular Expressions.
"""
    Search a given file using regular expressions and display
    matched lines.
"""
import sys
import re

def search_pattern(pattern, file=r"C:\labs\words"):
    """ Display lines in a given file which match Regex """
    fh_in = open(file, mode="rt")

    # Iterate through file handle
    for line in fh_in:
        # m = re.match(pattern, line) # Match pattern at start of string.
        m = re.search(pattern, line) # Return None or RE Match object.
        if m:
            print(line, end="")

    fh_in.close()
    return None

def main():
    """ Demonstrate different Regex patterns """
    search_pattern(r"^the") # Match lines starting with 'the'.
    search_pattern(r"^ing$") # Match lines ending with 'ing'.
    search_pattern(r"^[A-Z]") # Match lines starting with a capital.
    search_pattern(r"\.") # Match lines with a dot.
    search_pattern(r"[aeiou][aeiou][aeiou]") # Match 3 consecutive vowels.
    search_pattern(r"[aeiou]{5,}")  # Match at least 5 consecutive vowels.
    search_pattern(r"^...................$") # Match lines with exactly 19 chars.
    search_pattern(r"^.{19}$") # Match lines with excatly 19 chars.
    search_pattern(r"^(.)(.).\2\1$") # Match lines 5 char palindromes.
    search_pattern(r"^(.).*\1$") # Match lines starting/ending with same char.
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)