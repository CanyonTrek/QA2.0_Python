#! /usr/bin/python
# Author: QA2.0 LIVE, V1.0
# Description: This program will demonstrate how to copy collections
# by memory reference, shallow copy and deep copy.
"""
    Copying Collections.
"""
import sys
import pprint
import copy

def main():
    """ Copy Collections """
    movies = { 'Donald': ['Dracula', 'Deliverance', 'Descendants'],
               'Mira': ['Matrix', 'Mad Max', 'Magnolia'],
               'Sarah': ['Seven', 'Scream', 'Saving Private Ryan']
    }

    # Comment each of the following on at a time!
    films = movies # Copy by memory reference
    # films = movies.copy() # Shallow Copy, nested objects are shared.
    # films = copy.deepcopy(movies) # Deep copy to all nested levels.

    movies['Mira'][1] = 'Magnificent Seven'
    movies['Brian'] = ['Braveheart', 'Brave', 'Babe']

    pprint.pprint(movies)
    print("-" * 60)
    pprint.pprint(films)
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)