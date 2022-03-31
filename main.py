from spotifyClient import *
from bandcampShowTracks import BandcampShowTracks

load_dotenv()

def main():

    # PART 0 - Init session
    spotifyClient = SpotifyClient()
    print(spotifyClient.authorizationToken)

    # PART 1 - Scrape bandcamp tracks
    bandcampShowTracks = BandcampShowTracks([1])

    # PART 2 - Get bandcamp tracks from spotify (if not found returns highest rated track from same artist)
    spotifyClient.methods.get_bandcamp_tracks_from_spotify(bandcampShowTracks.show_tracks)

    #spotifyClient.methods.populate_spotify_playlist_with_bandcamp_track(bandcampShowTracks)
    
    
    # PART 2 - Get recommendations
    #spotify_recomm = spotify_client.methods.get_spotify_track_recommendations(
    #    bandcampShowTracks.show_tracks
    #)

    # PART 3 - Create + populate playlist
    # spotify_client.populate_playlist(spotify_recomm)


if __name__ == "__main__":
    main()
