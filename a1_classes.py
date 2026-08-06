"""
CP1404/CP5632 Assignment 2 - Albums Archive console program.
Name: Ding Zuotian
Date: 26/7/2026
GitHub: https://github.com/ZuotianDing/cp1404-a1-ZuotianDing.git
"""

import random
from operator import attrgetter

from album import Album
from albumcollection import AlbumCollection

ALBUMS_FILENAME = "albums.json"
PROGRAM_NAME = "Albums Archive 2.0"
AUTHOR = "Ding Zuotian"
DISPLAY_CHOICE = "D"
RECOMMEND_CHOICE = "R"
ADD_CHOICE = "A"
MARK_CHOICE = "M"
QUIT_CHOICE = "Q"
REQUIRED_MARKER = "*"
COMPLETE_MARKER = " "
MENU = """Menu:
D - Display all albums
R - Recommend a random album
A - Add a new album
M - Mark an album as completed
Q - Quit"""


def main():
    """Run the console Albums Archive program."""
    print(f"{PROGRAM_NAME} - by {AUTHOR}")
    albums = AlbumCollection()
    try:
        albums.load_albums(ALBUMS_FILENAME)
    except FileNotFoundError:
        print(f"Error, {ALBUMS_FILENAME} not found!")
    print(f"{len(albums.albums)} albums loaded from {ALBUMS_FILENAME}")

    display_menu()
    choice = input(">>> ").strip().upper()
    while choice != QUIT_CHOICE:
        if choice == DISPLAY_CHOICE:
            display_albums(albums)
        elif choice == RECOMMEND_CHOICE:
            recommend_album(albums)
        elif choice == ADD_CHOICE:
            add_album(albums)
        elif choice == MARK_CHOICE:
            mark_album_completed(albums)
        else:
            print("Invalid menu choice")
        display_menu()
        choice = input(">>> ").strip().upper()

    albums.save_albums(ALBUMS_FILENAME)
    print(f"{len(albums.albums)} albums saved to {ALBUMS_FILENAME}")
    print("Have a nice day :)")


def display_menu():
    """Display the available menu commands."""
    print(f"\n{MENU}")


def display_albums(albums):
    """Display albums sorted by status and then by release year."""
    if not albums.albums:
        print("No albums!")
        return

    albums.albums.sort(key=attrgetter("is_completed", "year"))
    title_width = max(len(album.title) for album in albums.albums)
    artist_width = max(len(album.artist) for album in albums.albums)
    for number, album in enumerate(albums.albums, 1):
        marker = COMPLETE_MARKER if album.is_completed else REQUIRED_MARKER
        print(
            f"{marker}{number}. {album.title:<{title_width}} by "
            f"{album.artist:<{artist_width}} {album.year}"
        )
    required_count = albums.get_number_of_required_albums()
    print(
        f"{len(albums.albums)} albums in archive. "
        f"You still want to listen to {required_count} albums."
    )


def recommend_album(albums):
    """Recommend one randomly selected required album."""
    required_albums = [
        album for album in albums.albums if not album.is_completed
    ]
    if not required_albums:
        print("No albums left to listen to!")
        return
    print("Not sure what to listen to next?")
    album = random.choice(required_albums)
    print(f"How about... {album.title} by {album.artist}?")


def add_album(albums):
    """Read valid album details and add a required album."""
    title = get_non_empty_string("Title: ")
    artist = get_non_empty_string("Artist: ")
    year = get_positive_integer("Year: ")
    albums.add_album(Album(title, artist, year, False))
    print(f"{title} by {artist} ({year}) added to Albums Archive.")


def mark_album_completed(albums):
    """Mark a selected required album as completed."""
    if albums.get_number_of_required_albums() == 0:
        print("No required albums.")
        return

    display_albums(albums)
    print("Enter the number of an album to mark as completed")
    album = None
    while album is None:
        album_number = get_positive_integer(">>> ")
        try:
            album = albums.albums[album_number - 1]
        except IndexError:
            print("Invalid album number")
    if album.is_completed:
        print(f"You have already completed {album.title}")
    else:
        album.mark_completed()
        print(f"{album.title} by {album.artist} completed!")


def get_non_empty_string(prompt):
    """Read and return a non-blank string."""
    value = input(prompt).strip()
    while not value:
        print("Input cannot be blank")
        value = input(prompt).strip()
    return value


def get_positive_integer(prompt):
    """Read and return a valid positive integer."""
    is_valid = False
    number = 0
    while not is_valid:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("Number must be > 0")
            else:
                is_valid = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return number


if __name__ == "__main__":
    main()