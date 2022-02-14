class Constants():

    SCOPES = {
        "current_user_top_artists": "user-top-read",
        "current_user_recently_played": "user-read-recently-played",
        "current_user_top_tracks": "user-top-read",
        "current_user_playlists": "playlist-read-private",
    }

    SEARCH_ENDPOINT = "https://api.spotify.com/v1/search"
    RECENTLY_PLAYED_ENDPOINT = "https://api.spotify.com/v1/me/player/recently-played"
    RECOMMENDATIONS = "https://api.spotify.com/v1/recommendations"

    BANDCAMP_ENDPOINT = "https://bandcamp.com/"

    REGEX_REMOVE_PARENTHESIS = r"\([^()]*\)"
