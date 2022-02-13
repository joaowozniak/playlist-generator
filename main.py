import os
from spotifyClient import SpotifyClient
from bandcampScraper import BandcampScraper
from dotenv import load_dotenv


load_dotenv()


def main():

    # PART 0 - Init session
    spotify_client = SpotifyClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), os.getenv("REDIRECT_URI"))       
    spotify_client.setup()
    
    #PART 1 - Scrape bandcamp tracks
    bandcampScraper = BandcampScraper()
    bandcamp_shows_id_list = [1]

    tracks_show_id = bandcampScraper.scrape(bandcamp_shows_id_list)

    #PART 2 - Get recommendations
    #spotify_recomm = spotify_client.get_track_recommendations(tracks_show_id)
    #print(tracks_show_id[-1:])
    print(spotify_client.search_tracks(tracks_show_id[-2:-1][0], search_type='track', album_search=False))

    #PART 3 - Create + populate playlist 
    
    #spotify_client.populate_playlist(spotify_recomm)
    
   

if __name__ == "__main__":
    main()
