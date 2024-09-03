#! /bin/python
# Name:        movies.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will download the top 250 movies from IMDB
# and will allow the user to display the top-n ranked movies or search
# for their favourite movies.
# FIX:  pip install -U git+https://github.com/cinemagoer/cinemagoer
"""
    Download and display the Top 250 Movies Data from IMDB.
"""
import sys
import requests
from bs4 import BeautifulSoup

import re

movie_menu = """
    Movies Menu
    -----------
    1. Get online movie ranking from IMDB
    2. Display top ranking movies
    3. Search for movie
"""

def get_movies():
    """ Web Scrape the top 250 movies online from letterboxd.com """
    # Base URL of the Letterboxd Top 250 movies page
    base_url = "https://letterboxd.com/jack/list/official-top-250-films-with-the-most-fans/page/{}/"
    top_movies = {} # Movie info - 'title': [rank, rating, img_url]

    # Loop through pages (assuming there are a few pages, update as needed)
    for page_num in range(1, 4):  # Adjust range according to the number of pages
        # Send a GET request to fetch the page content
        url = base_url.format(page_num)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all movie containers
        movie_tags = soup.find_all("li", class_="poster-container")

        # Extract movie details
        for rank, movie in enumerate(movie_tags, start=1 + len(top_movies)):
            # Extract the title from the 'alt' attribute of the image
            title = movie.find('img', class_='image').get('alt')
            # Extract the link using the 'data-target-link' attribute
            link = movie.find('div', class_='really-lazy-load').get('data-target-link')
            full_link = f"https://letterboxd.com{link}"
            # Extract the rating using the 'data-owner-rating' attribute
            rating = movie.get('data-owner-rating')

            top_movies[title] = [rank, rating, full_link]
    return top_movies

def display_movies(movies, top=250):
    """ Display top movies in a given dict """
    if not movies:
        print("No movies to display.")
    else:
        for movie, info in movies.items():
            rank, rating, link = info
            print(f"{rank:>4d} {movie:<s}, {rating}/10 - {link}")
            if int(rank) == int(top): break
    return None

def search_movies(pattern=r".", movies=None):
    """ Search for pattern in a given dict of movies """
    if not movies:
        print("No movies to search.")
    else:
        for movie, info in movies.items():
            rank, rating, link = info
            if re.search(pattern, movie, re.IGNORECASE):
                print(f"{rank:>4} {movie:<s}, {rating}/10 - {link}")
    return None

def menu():
    """ Movie Menu """
    films = {}
    while True:
        print(movie_menu)
        option = input("Enter option (1-3, [qQ=quit]): ").strip().lower()

        if option == "1":
            films = get_movies()
            print(f"Fetched {len(films)} movies")
        elif option == "2":
            top = input("How many top movies do you want to display [default=250]: ").strip() or "250"
            display_movies(films, top)
        elif option == "3":
            pattern = input("Enter title search pattern: ").rstrip()
            search_movies(pattern, films)
        elif option == "q":
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again")

    return None

if __name__ == "__main__":
    menu()
    sys.exit(0)