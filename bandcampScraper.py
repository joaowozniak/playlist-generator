from ast import Constant
import requests, json, re
from bs4 import BeautifulSoup
from constants import Constants


class BandcampScraper:
    
    def scrape(self, show_ids: list):
        tracks_names = []
        
        for id in show_ids:

            html_text = requests.get(f"{Constants.BANDCAMP_ENDPOINT}?show={id}").text
            soup = BeautifulSoup(html_text, "lxml")
            tracks = json.loads(soup.find(id="pagedata")["data-blob"])

            for i in range(0, 34):
                try:
                    title = re.sub(
                        Constants.REGEX_REMOVE_PARENTHESIS,
                        "",
                        tracks["bcw_data"][str(id)]["tracks"][i]["title"],
                    )

                    artist = re.sub(
                        Constants.REGEX_REMOVE_PARENTHESIS,
                        "",
                        tracks["bcw_data"][str(id)]["tracks"][i]["artist"],
                    )

                    album = re.sub(
                        Constants.REGEX_REMOVE_PARENTHESIS,
                        "",
                        tracks["bcw_data"][str(id)]["tracks"][i]["album_title"],
                    )

                    tracks_names.append(
                        {"track": title, "artist": artist, "album": album}
                    )
                except:
                    continue

        return tracks_names
