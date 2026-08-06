"""Represent an album in the Albums Archive application."""

VINTAGE_YEAR = 1977


class Album:
    """Store details about one album and its completion status."""

    def __init__(self, title="", artist="", year=0, is_completed=False):
        """Initialise an album from its title, artist, year and status."""
        self.title = title
        self.artist = artist
        self.year = year
        self.is_completed = is_completed

    def __str__(self):
        """Return a readable description including the album status."""
        status = "completed" if self.is_completed else "required"
        return f"{self.title} by {self.artist} ({self.year}) ({status})"

    def mark_completed(self):
        """Change the album status to completed."""
        self.is_completed = True

    def mark_required(self):
        """Change the album status to required."""
        self.is_completed = False

    def is_vintage(self):
        """Determine whether the album was released in or before 1977."""
        return self.year <= VINTAGE_YEAR