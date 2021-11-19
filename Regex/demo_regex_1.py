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


def main():
    """ Demonstrate different Regex patterns """
    fh_in = open(r"C:\labs\words", mode="rt")

    # Iterate through file handle
    for line in fh_in:
        # m = re.search(r"^the", line)  # Match lines starting with 'the'.
        # m = re.search(r"ing$", line)  # Match lines ending with 'ing'.
        # m = re.search(r"^[A-Z]", line)  # Match lines starting with a capital.
        # m = re.search(r"\.", line)  # Match lines with a dot.
        # m = re.search(r"[aeiou][aeiou][aeiou]", line)  # Match 3 consecutive vowels.
        # m = re.search(r"[aeiou]{5,}", line)  # Match at least 5 consecutive vowels.
        # m = re.search(r"^...................$", line)  # Match lines with exactly 19 chars.
        # m = re.search(r"^.{19}$", line)  # Match lines with excatly 19 chars.
        # m = re.search(r"^(.)(.).\2\1$", line)  # Match lines 5 char palindromes.
        # m = re.match(r"(.)(.).\2\1$", line)  # Match lines 5 char palindrome using match().
        m = re.search(r"^(.).*\1$", line)  # Match lines starting/ending with same char.

        if m:
            print(line, end="")

    fh_in.close()
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)