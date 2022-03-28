class Track:
    """Track represents a piece of music on Spotify"""

    def __init__(self, name, id, artist, album) -> None:
        self.name = name
        self.id = id
        self.artist = artist
        self.album = album

    def __str__(self) -> str:
        return f"{self.name} by {self.artist}"

    def get_name(self):
        return self.name
