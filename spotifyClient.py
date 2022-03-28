import requests
from typing import List
from track import Track
from playlist import Playlist
import spotipy.util as util
from urllib.parse import urlencode
from constants import Constants
from dotenv import load_dotenv
import os


class SpotifyClient:
    def __init__(self) -> None:
        self.authorization_token = SpotifyClientSetup(
            os.getenv("CLIENT_ID"),
            os.getenv("CLIENT_SECRET"),
            os.getenv("REDIRECT_URI"),
        ).setup()
        self.methods = SpotifyClientMethods(self.authorization_token)


class SpotifyClientSetup:
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.authorization_token = ""

    def setup(self, scope: str = None) -> None:
        print("--- Starting Spotify API connection ...")

        if self.client_id == None or self.client_secret == None:
            raise Exception("--- Client Id and Client Secret must be set.")

        all_scopes = ""
        for scope in Constants.SCOPES.values():
            all_scopes += scope + " "

        token = util.prompt_for_user_token(
            scope=all_scopes,
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
        )

        print(f"--- User {self.client_id} connected to Spotify API!")
        return token


class SpotifyClientMethods:
    def __init__(self, authorization_token) -> None:
        self.authorization_token = authorization_token

    def get_spotify_track_recommendations(self, seed_tracks, limit=10):
        seed_bandcamp_tracks = self.__get_tracks_from_spotify(seed_tracks)
        seed_tracks_url = ""
        count = 0

        for seed_track in seed_bandcamp_tracks:
            if count == 5:
                break
            if not seed_track:
                continue
            elif isinstance(seed_track, Track):
                seed_tracks_url += seed_track.id + ","
            count += 1

        url = f"{Constants.RECOMMENDATIONS_ENDPOINT}?seed_tracks={seed_tracks_url}&limit={limit}"
        response = self.__execute_get_request(url)
        response_json = response.json()

        tracks = [
            Track(
                track["name"],
                track["id"],
                track["artists"][0]["name"],
                track["album"]["name"],
            )
            for track in response_json["tracks"]
        ]
        return tracks

    def __get_tracks_from_spotify(self, bandcamp_tracks) -> List[Track]:
        spotify_tracks = []
        for track in bandcamp_tracks:
            print(track)
            spotify_tracks.append(self.search_track(track, "track", True))

        return spotify_tracks

    def search_track(
        self, query=None, search_type=None, artist_search=False, album_search=False
    ) -> List[Track]:
        # print("--- Searching track info in Spotify catalog...")
        if query == None:
            raise Exception("Empty query!")

        items = ["track"]  # , 'artist']
        if artist_search == True:
            items.append("artist")
        if album_search == True:
            items.append("album")

        query_build = ""
        if isinstance(query, dict):
            query_build = " ".join(
                [f"{value} " for key, value in query.items() if key in items]
            )

        query_params = urlencode(
            {"q": query_build.lower(), "type": search_type.lower()}
        )
        url = f"{Constants.SEARCH_ENDPOINT}?{query_params}"
        response = self.__execute_get_request(url)
        response_json = response.json()

        tracks = [
            Track(
                track["name"],
                track["id"],
                track["artists"][0]["name"],
                track["album"]["name"],
            )
            for track in response_json["tracks"]["items"]
        ]

        if not tracks:
            print(f"Track: {query} not found in Spotify. Trying again ...")
            return None

        else:
            return tracks[0]

    ###################################################

    def get_spotify_last_played_tracks(self, limit=10):
        print(f"--- Getting last {limit} played tracks ...")
        url = f"{Constants.LAST_PLAYED_ENDPOINT}?limit={limit}"
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
