"""Tests for the Album class."""

from album import Album


def run_tests():
    """Run simple assertion tests for all Album methods."""
    album = Album("Abbey Road", "The Beatles", 1969, False)
    assert str(album) == "Abbey Road by The Beatles (1969) (required)"
    assert album.is_vintage()

    album.mark_completed()
    assert album.is_completed
    assert str(album) == "Abbey Road by The Beatles (1969) (completed)"

    album.mark_required()
    assert not album.is_completed

    recent_album = Album("After the Music Stops", "Lecrae", 2006, True)
    assert not recent_album.is_vintage()
    print("All Album tests passed.")


if __name__ == "__main__":
    run_tests()