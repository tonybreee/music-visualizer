import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI

def spotify_login():
    auth_manager = SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope="user-library-read"
    )
    return auth_manager.get_authorize_url()

def get_spotify_song(song_id, token):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(token))
    track = sp.track(song_id)
    return {
        "title": track["name"],
        "artist": track["artists"][0]["name"],
        "album_cover": track["album"]["images"][0]["url"],
        "bpm": sp.audio_features(song_id)[0]["tempo"]
    }
