class Constants:

    SCOPES = {
        "current_user_top_artists": "user-top-read",
        "current_user_recently_played": "user-read-recently-played",
        "current_user_top_tracks": "user-top-read",
        "current_user_playlists": "playlist-read-private",
    }

    SEARCH_ENDPOINT = "https://api.spotify.com/v1/search"
    LAST_PLAYED_ENDPOINT = "https://api.spotify.com/v1/me/player/recently-played"
    RECOMMENDATIONS_ENDPOINT = "https://api.spotify.com/v1/recommendations"

    BANDCAMP_ENDPOINT = "https://bandcamp.com/"

    REGEX_REMOVE_PARENTHESIS = r"[^\w ]"  # r"\([^()]*\)"
    REGEX_REMOVE_SPECIAL_WORDS = [r"\|*ft \|*", r"\|*featuring \|*", r"\|*feat \|*"]
