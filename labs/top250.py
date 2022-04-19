#! /bin/python
# Name:        top250.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Download the top 250 movies chosen by IMDb users.
"""
    Download and display online movie information.
"""
import imdb
def main():
    ia = imdb.IMDb()
    for movie in ia.get_top250_movies():
        print(movie)
    return None
if __name__ == "__main__":
    main()