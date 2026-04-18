from bs4 import BeautifulSoup
import requests
import spotipy
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

print("Which year do you want to travel to?")
year = input("Year: ")
month = input("Month: ")
day = input("Date: ")

#***************************  CODE TO GET WEB SCRAPE SONGS  *****************************************
date = int(f"{year}{month.zfill(2)}{day.zfill(2)}")
#The user agent details in the header are to identify me. Used to stop bots from scraping
header = {"user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
url = f"https://www.officialcharts.com/charts/singles-chart/{date}/7501"
response = requests.get(url = url, headers= header)

soup = BeautifulSoup(response.text,"html.parser")
songs = soup.find_all(name="div",class_ = "description block")
song_list = []
for item in songs:
    song_data = item.find_all(name="span", class_=None)
    song_list.append({
        "song": song_data[0].text.strip(),
        "artist": song_data[1].text.strip()
    })


#***************************  SPOTIPY CODE  **************************************************

#create the spotify client
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id = os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret = os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="playlist-modify-private playlist-modify-public"
    )
)

user_id = sp.current_user()["id"]
print(f"Logged in as: {user_id}")

song_uris = []
#loop through the list of songs/artists and add the spotify uri for the song to the song_uri list.
for item in song_list:
    song = item['song']
    artist = item['artist']
    result = sp.search(q=f"track:{song} artist:{artist}", type="track", limit=1)

    if result["tracks"]["items"]: #if it finds a match
        uri = result["tracks"]["items"][0]['uri']
        song_uris.append(uri)
    else:
        print(f"Song not found: {song}")

#Create the playlist
playlist = sp.current_user_playlist_create(
    name=f"UK chart songs from {day}/{month}/{year}",
    public=True,
    description="Auto-generated playlist from official charts"
)
sp.playlist_change_details(playlist['id'], public=False)

#Get the playlist id
playlist_id = playlist["id"]

#Use the song_uri list to add the songs to the playlist
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)

print(f"Playlist created!")