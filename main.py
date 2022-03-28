from spotifyClient import *
from bandcampShowTracks import BandcampShowTracks

load_dotenv()


def main():

    # PART 0 - Init session
    spotify_client = SpotifyClient()
    print(spotify_client.authorization_token)

    # PART 1 - Scrape bandcamp tracks
    bandcampShowTracks = BandcampShowTracks([1, 6, 9])

    # PART 2 - Get recommendations
    spotify_recomm = spotify_client.methods.get_spotify_track_recommendations(
        bandcampShowTracks.show_tracks
    )

    # PART 3 - Create + populate playlist
    # spotify_client.populate_playlist(spotify_recomm)


if __name__ == "__main__":
    main()
