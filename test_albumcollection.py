"""Tests for the AlbumCollection class."""

import json
import tempfile
from pathlib import Path

from album import Album
from albumcollection import AlbumCollection


def run_tests():
    """Run simple assertion tests for AlbumCollection behaviour."""
    albums = AlbumCollection()
    albums.add_album(Album("Z Album", "Artist B", 2000, False))
    albums.add_album(Album("A Album", "Artist A", 1970, True))
    albums.add_album(Album("B Album", "Artist C", 1990, False))

    assert albums.get_number_of_required_albums() == 2
    assert albums.get_number_of_complete_albums() == 1

    albums.sort()
    assert [album.title for album in albums.albums] == [
        "B Album", "Z Album", "A Album"
    ]
    albums.sort("year")
    assert [album.year for album in albums.albums] == [1970, 1990, 2000]

    with tempfile.TemporaryDirectory() as directory:
        filename = Path(directory) / "albums.json"
        albums.save_albums(filename)
        saved_data = json.loads(filename.read_text(encoding="utf-8"))
        assert len(saved_data) == 3

        loaded_albums = AlbumCollection()
        loaded_albums.load_albums(filename)
        assert len(loaded_albums.albums) == 3
        assert loaded_albums.albums[0].title == "A Album"
        assert loaded_albums.albums[0].is_completed

    print("All AlbumCollection tests passed.")


if __name__ == "__main__":
    run_tests()