import json, requests, datetime, base64
from typing import List
from track import Track
from playlist import Playlist
import spotipy.util as util
from urllib.parse import urlencode
from constants import Constants


class SpotifyClient:
    """
    Spotify Client performs operations with Spotify API
    """

    def __init__(self, client_id: str, client_secret: str, redirect_uri: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret        
        self.redirect_uri = redirect_uri
        self.authorization_token = ""

    def setup(self, scope: str = None) -> None:
        """setup"""

        print("-- Init Spotify connection --")

        all_scopes = ""
        for scope in Constants.SCOPES.values():
            all_scopes += scope + " "

        token = self.__get_token(scope=all_scopes)
        self.authorization_token = token

        print(f"connection and user are ready!")

    def __get_token(self, scope: str) -> str:
        """get token"""

        if self.client_id == None or self.client_secret == None:
            raise Exception("Client Id and Client Secret must be set.")

        token = util.prompt_for_user_token(
            scope=scope,
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
        )

        return token

    def get_last_played_tracks(self, limit=10):
        """get las played"""

        endpoint = Constants.RECENTLY_PLAYED_ENDPOINT
        url = f"{endpoint}?limit={limit}"

        response = self.__execute_get_request(url)
        response_json = response.json()

        tracks = [
            Track(
                track["track"]["name"],
                track["track"]["id"],
                track["track"]["artists"][0]["name"],
            )
            for track in response_json["items"]
        ]

        return tracks

    def get_track_recommendations(self, seed_tracks, limit=10):
        """get tracks reccomm"""

        seed_tracks_url = ""

        for seed_track in seed_tracks:
            seed_tracks_url += seed_track.id + ","

        seed_tracks_url = seed_tracks_url[:-1]

        endpoint = Constants.RECOMMENDATIONS
        url = f"{endpoint}?seed_tracks={seed_tracks_url}&limit={limit}"

        response = self.__execute_get_request(url)
        response_json = response.json()

        tracks = [
            Track(track["name"], track["id"], track["artists"][0]["name"])
            for track in response_json["tracks"]
        ]

        return tracks

    def __search_track(self, query = None, search_type = None, album_search = None) -> Track:
        """search tracks"""

        if query == None:
            raise Exception("Empty query.")

        items = ['track', 'artist']
        if album_search == True:
            items.append('album')        
        
        query_build = ""
        if isinstance(query, dict):
            query_build = " ".join([f"{key}:{value}" for key, value in query.items() if key in items])
        
        endpoint = Constants.SEARCH_ENDPOINT
        query_params = urlencode({"q": query_build, "type": search_type.lower()})

        url = f"{endpoint}?{query_params}"
        response = self.__execute_get_request(url)
        response_json = response.json()
        
        tracks = [
            Track(track["name"], track["id"], track["artists"][0]["name"], track["album"]["name"])
            for track in response_json["tracks"]["items"]
        ]

        return tracks[0]

    def get_bandcamp_tracks_from_spotify(self, bandcamp_tracks) -> List[Track]:
        
        spotify_tracks = []

        for track in bandcamp_tracks:
            spotify_tracks.append(self.__search_track(track, 'track'))

        return spotify_tracks            

    def __create_playlist():
        pass

    def populate_playlist():
        pass

    def __execute_post_request(self, url, data):
        response = requests.post(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.authorization_token}",
            },
        )
        return response

    def __execute_get_request(self, url):
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.authorization_token}",
            },
        )
        return response
