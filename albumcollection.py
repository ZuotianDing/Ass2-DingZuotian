"""Manage a collection of Album objects."""

import json
from operator import attrgetter

from album import Album

DEFAULT_SORT_KEY = "is_completed"


class AlbumCollection:
    """Store and manage a list of albums."""

    def __init__(self, albums=None):
        """Initialise the collection with an optional list of albums."""
        self.albums = albums if albums is not None else []

    def add_album(self, album):
        """Add one Album object to the collection."""
        self.albums.append(album)

    def get_number_of_required_albums(self):
        """Return the number of albums still required."""
        return sum(not album.is_completed for album in self.albums)

    def get_number_of_complete_albums(self):
        """Return the number of completed albums."""
        return sum(album.is_completed for album in self.albums)

    def load_albums(self, filename):
        """Load Album objects from a JSON file, replacing current contents."""
        with open(filename, "r", encoding="utf-8") as input_file:
            album_data = json.load(input_file)
        self.albums = [Album(**data) for data in album_data]

    def save_albums(self, filename):
        """Save all albums to a JSON file."""
        album_data = [vars(album) for album in self.albums]
        with open(filename, "w", encoding="utf-8") as output_file:
            json.dump(album_data, output_file, indent=4)

    def sort(self, key=DEFAULT_SORT_KEY):
        """Sort albums by the supplied attribute and then by title."""
        self.albums.sort(key=attrgetter(key, "title"))