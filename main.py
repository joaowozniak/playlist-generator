import os
from spotifyClient import SpotifyClient
from bandcampScraper import BandcampScraper
from dotenv import load_dotenv


load_dotenv()


def main():

    spotify_client = SpotifyClient(
        os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), os.getenv("REDIRECT_URI")
    )

    bandcampScraper = BandcampScraper()

    tracks_names = bandcampScraper.scrape([17])
    track = tracks_names[-2:]

    spotify_client.setup()

    a = spotify_client.search_tracks(
        {
            "track": track[0]["title"],
            "artist": track[0]["artist"],
            "album": track[0]["album"][:13],
        },
        search_type="track",
    )
    print(a)
    # print(track[0]["title"])
    # num_tracks_to_visualise = 2
    # print(
    #    spotify_client.search(
    #        {"track": "The Third Adam", "artist": "Nu Era"}, search_type="track"
    #   )
    # )

    # last_played_tracks = spotify_client.get_last_played_tracks(num_tracks_to_visualise)

    # print(spotify_client.get_track_recommendations(last_played_tracks))


if __name__ == "__main__":
    main()
