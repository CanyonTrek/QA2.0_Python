#! /usr/bin/python
# Author: QA2.0 LIVE, V1.0
# Description: This program will demonstrate how to benchmark/profile code
# to improve performance and quality using the cProfile module.
"""
    Search a given file using regular expressions and display
    matched lines. Analyse performance of code change,
"""
import sys
import re

def search_pattern(pattern, file=r"C:\labs\words"):
    """ Display lines in a given file which match Regex """
    fh_in = open(file, mode="rt")
    reobj = re.compile(pattern)

    for line in fh_in:
        m = reobj.search(line) # Return None or RE Match object.
        if m:
            print(line, end="")
    fh_in.close()
    return None

def main():
    """ Demonstrate different Regex patterns """
    search_pattern(r"^.{19}$") # Match lines with exactly 19 chars.
    return None

if __name__ == "__main__":
    import cProfile
    cProfile.run("main()") # Display stats to console.
    # cProfile.run("main()", "stats.prof") # Write stats to file.
    sys.exit(0)

