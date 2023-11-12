#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import schedule
import time

dotenv_path = '/Users/elliotberdy/Library/CloudStorage/OneDrive-UCLAITServices/Notability/spotify-alarm/.env'

load_dotenv(dotenv_path)

song_name = 'good morning'
artist_name = 'alex aiono'

print("runnning Spotify script")

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
SPOTIPY_USERNAME = os.getenv('SPOTIPY_USERNAME')
SCOPE = 'user-library-read user-read-playback-state user-modify-playback-state'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

results = sp.search(q=f'track:{song_name} artist:{artist_name}', type='track')

if results['tracks']['items']:
    SPOTIFY_URI = results['tracks']['items'][0]['uri']
    print(f"Spotify URI for '{song_name}' by {artist_name}: {SPOTIFY_URI}")
else:
    print(f"No results found for '{song_name}' by {artist_name}")


def play_spotify_song():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                   client_secret=SPOTIPY_CLIENT_SECRET,
                                                   redirect_uri=SPOTIPY_REDIRECT_URI,
                                                   scope=SCOPE,
                                                   username=SPOTIPY_USERNAME))

    sp.start_playback(uris=[SPOTIFY_URI])


# Python script has to be running
    # using crontab to schedule the script instead

# schedule.every().day.at("12:20").do(play_spotify_song)

# while True:
    # schedule.run_pending()
    # time.sleep(1)


play_spotify_song()
