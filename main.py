"""
CP1404/CP5632 Assignment 2 - Albums Archive GUI.
Name: Ding Zuotian
Date: 26/7/2026
GitHub: https://github.com/ZuotianDing/cp1404-2026-2-a2-DingZuotian.git
"""

from pathlib import Path

from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.button import Button

from album import Album
from albumcollection import AlbumCollection

PROJECT_DIRECTORY = Path(__file__).parent
ALBUMS_FILENAME = PROJECT_DIRECTORY / "albums.json"
KV_FILENAME = PROJECT_DIRECTORY / "app.kv"
REQUIRED_COLOUR = (0.86, 0.34, 0.27, 1)
COMPLETE_COLOUR = (0.24, 0.58, 0.36, 1)
BUTTON_TEXT_COLOUR = (1, 1, 1, 1)
BUTTON_HEIGHT = 64
SORT_OPTIONS = ("Completed", "Title", "Artist", "Year")
SORT_KEYS = {
    "Completed": "is_completed",
    "Title": "title",
    "Artist": "artist",
    "Year": "year",
}


class AlbumsApp(App):
    """Manage and display an album collection using a Kivy GUI."""

    sort_options = SORT_OPTIONS

    def build(self):
        """Load the collection and construct the application interface."""
        self.title = "Albums Archive 2.0"
        self.album_collection = AlbumCollection()
        self.album_collection.load_albums(ALBUMS_FILENAME)
        self.album_collection.sort()
        self.root = Builder.load_file(str(KV_FILENAME))
        self.display_albums()
        return self.root

    def display_albums(self):
        """Create one colour-coded button for every sorted album."""
        album_container = self.root.ids.album_container
        album_container.clear_widgets()
        for album in self.album_collection.albums:
            colour = COMPLETE_COLOUR if album.is_completed else REQUIRED_COLOUR
            button = Button(
                text=f"{album.title}\n{album.artist} ({album.year})",
                size_hint_y=None,
                height=dp(BUTTON_HEIGHT),
                background_normal="",
                background_color=colour,
                color=BUTTON_TEXT_COLOUR,
                halign="left",
                valign="middle",
            )
            button.bind(size=self.set_button_text_size)
            button.album = album
            button.bind(on_release=self.handle_album_press)
            album_container.add_widget(button)
        self.update_required_status()

    @staticmethod
    def set_button_text_size(button, size):
        """Keep album button text wrapped within the button bounds."""
        button.text_size = (size[0] - dp(20), size[1])

    def sort_albums(self, sort_label):
        """Sort albums using the attribute selected in the spinner."""
        if sort_label not in SORT_KEYS or not self.root:
            return
        self.album_collection.sort(SORT_KEYS[sort_label])
        self.display_albums()
        self.root.ids.message_label.text = f"Sorted by {sort_label.lower()}."

    def handle_album_press(self, button):
        """Toggle an album status and report the change to the user."""
        album = button.album
        if album.is_completed:
            album.mark_required()
            message = f"You need to listen to {album.title}."
        else:
            album.mark_completed()
            message = f"You completed {album.title}."
        if album.is_vintage():
            message += " That was a vintage album."
        self.root.ids.message_label.text = message
        selected_sort = self.root.ids.sort_spinner.text
        self.album_collection.sort(SORT_KEYS[selected_sort])
        self.display_albums()

    def add_album(self):
        """Validate text fields and add a new required album."""
        title = self.root.ids.title_input.text.strip()
        artist = self.root.ids.artist_input.text.strip()
        year_text = self.root.ids.year_input.text.strip()
        if not title or not artist or not year_text:
            self.root.ids.message_label.text = "Please complete all fields."
            return
        try:
            year = int(year_text)
            if year <= 0:
                raise ValueError
        except ValueError:
            self.root.ids.message_label.text = "Please enter a valid number"
            return

        self.album_collection.add_album(Album(title, artist, year, False))
        selected_sort = self.root.ids.sort_spinner.text
        self.album_collection.sort(SORT_KEYS[selected_sort])
        self.clear_fields()
        self.root.ids.message_label.text = f"Added {title} by {artist}."
        self.display_albums()

    def clear_fields(self):
        """Clear all album inputs and the lower status message."""
        self.root.ids.title_input.text = ""
        self.root.ids.artist_input.text = ""
        self.root.ids.year_input.text = ""
        self.root.ids.message_label.text = ""
        self.root.ids.title_input.focus = True

    def update_required_status(self):
        """Show the current number of albums still to be listened to."""
        required_count = self.album_collection.get_number_of_required_albums()
        self.root.ids.required_label.text = (
            f"Albums to listen to: {required_count}"
        )

    def on_stop(self):
        """Save the album collection when the application closes."""
        self.album_collection.save_albums(ALBUMS_FILENAME)


if __name__ == "__main__":
    AlbumsApp().run()