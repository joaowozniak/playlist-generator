import requests, json, re
from bs4 import BeautifulSoup
from constants import Constants

class BandcampShowTracks:

    def __init__(self, show_ids: list) -> None:
        self.show_ids = show_ids
        self.show_tracks = self.__scrapeTracks(show_ids)
    
    def __scrapeTracks(self, show_ids: list):
        tracks_names = []
        
        for id in show_ids:
            html_text = requests.get(f"{Constants.BANDCAMP_ENDPOINT}?show={id}").text
            soup = BeautifulSoup(html_text, "lxml")
            tracks = json.loads(soup.find(id="pagedata")["data-blob"])

            try:
                show_length = len(tracks["bcw_data"][str(id)]["tracks"])
                print(f"Bandcamp weekly show {id} has {show_length} tracks.")
            except:
                print(f"Bandcamp show {id} not found!")
                continue

            for i in range(0, len(tracks["bcw_data"][str(id)]["tracks"])): 
                title, artist, album = None, None, None

                try:        
                    title = re.sub(Constants.REGEX_REMOVE_PARENTHESIS, "", tracks["bcw_data"][str(id)]["tracks"][i]["title"])
                    title = title.lower()     
                    for regex in Constants.REGEX_REMOVE_SPECIAL_WORDS: title = re.sub(regex, "", title)                    
                except:
                    pass

                try:
                    artist = re.sub(Constants.REGEX_REMOVE_PARENTHESIS, "", tracks["bcw_data"][str(id)]["tracks"][i]["artist"])
                    artist = artist.lower()
                except:
                    pass

                try:                    
                    album = re.sub(Constants.REGEX_REMOVE_PARENTHESIS, "", tracks["bcw_data"][str(id)]["tracks"][i]["album_title"])
                except:
                    pass

                if (title, artist, album) == (None, None, None):
                    print("Track empty...") 
                    break

                else:
                    tracks_names.append({"track": title, "artist": artist, "album": album})

        return tracks_names