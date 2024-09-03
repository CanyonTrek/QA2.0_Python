#!/usr/bin/env python
# Name:        menu.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: A fun and interactive demo program for QA2.0 Python LIVE.

"""
    A fun program that allows users to choose from a variety of
    interesting options, including accessing the latest weather
    reports, crime data, and top movies. The program demonstrates
    Python skills such as web scraping, API consumption, and
    basic SQLite database interactions.
"""

import sys
import police_data
import weather_data
import movies

# Displayed menu options
MENU_TEXT = """
    Fun Data Menu
    -------------
    1. Display Online Public Weather Data in Browser
    2. Display Online Public UK Police Data on Screen
    3. Display/Search Top Movies from Letterboxd
    Q. Quit
"""

def display_menu():
    """Displays the top-level menu and handles user input."""
    while True:
        print(MENU_TEXT)
        option = input("Enter an option (1-3, Q to quit): ").strip().lower()

        if option == "1":
            weather_data.weather_menu()
        elif option == "2":
            police_data.police_menu()
        elif option == "3":
            movies.menu()
        elif option == "q":
            print("Quitting...")
            break
        else:
            print("Invalid option, please try again.")
    return None

def main():
    """Entry point for the program. Initiates the top-level menu."""
    display_menu()
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
