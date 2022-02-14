import inspect
import os
from spotifyClient import SpotifyClient
from bandcampScraper import BandcampScraper
from dotenv import load_dotenv


load_dotenv()


def main():

    # PART 0 - Init session
    spotify_client = SpotifyClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), os.getenv("REDIRECT_URI"))       
    spotify_client.setup()
    print(spotify_client.authorization_token)
    #PART 1 - Scrape bandcamp tracks
    bandcampScraper = BandcampScraper()
    bandcamp_shows_id_list = [1]
    seed_tracks = bandcampScraper.scrape(bandcamp_shows_id_list)

    #print(seed_tracks[-2:])
    #PART 2 - Get recommendations
    #spotify_recomm = spotify_client.get_track_recommendations(seed_tracks)    
    #t =spotify_client.search_track(seed_tracks[-2:-1][0], search_type='track', album_search=False)
    #print(t.id)
    #print(t.album)
    #a = (spotify_client.get_bandcamp_tracks_from_spotify(seed_tracks[-2:]))

    #PART 3 - Create + populate playlist 
    
    #spotify_client.populate_playlist(spotify_recomm)
    
   

if __name__ == "__main__":
    main()
