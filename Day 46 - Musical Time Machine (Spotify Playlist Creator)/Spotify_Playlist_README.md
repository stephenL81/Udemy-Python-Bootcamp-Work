# Day 46 - Musical Time Machine (Spotify Playlist Creator)

## Description

This application creates a personalized Spotify playlist based on the UK Official Singles Chart from any chosen date. Users input a specific date, and the program scrapes the chart data from that week, searches for each song on Spotify, and automatically generates a playlist with all available tracks. This project demonstrates web scraping, API integration, OAuth authentication, and automated playlist creation.

The application combines data from the Official Charts Company (UK's official music charts) with Spotify's extensive music library to create a nostalgic musical time capsule from any date in chart history.

---

## How to Run

### 1. Install required dependencies
```bash
pip install beautifulsoup4 requests spotipy python-dotenv
```

### 2. Set up Spotify Developer Account
- Go to https://developer.spotify.com/dashboard
- Create a new app
- Note your **Client ID** and **Client Secret**
- Add redirect URI: `http://127.0.0.1:8888/callback`

### 3. Configure environment variables
Create a `.env` file in your project directory:
```
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
```

### 4. First run - OAuth authentication
On first run, the app will:
- Open your browser for Spotify authorization
- Ask you to log in and approve the app
- Redirect to a localhost page that won't load (this is normal!)
- Prompt you to paste the full redirect URL back into the terminal
- Save an authentication token for future use

### 5. Run the application
```bash
python main.py
```

Enter your chosen date when prompted (year, month, day).

---

## How It Works

### User Input & Date Formatting
The program prompts for a date in three parts (year, month, day) and formats it for the Official Charts URL structure. The `zfill(2)` method ensures single-digit months and days are zero-padded (e.g., "6" becomes "06") for proper URL construction.

### Web Scraping
Using BeautifulSoup, the program fetches the Official Charts singles chart page for the specified date. It extracts song titles and artist names from `<div class="description block">` elements, specifically targeting `<span>` tags without classes (the first span contains the song title, the second contains the artist name).

The scraper includes a User-Agent header to identify the request as coming from a legitimate browser, which helps prevent the site from blocking automated requests.

### Spotify Authentication (OAuth)
The application uses Spotipy's OAuth implementation to authenticate with Spotify's API. The `SpotifyOAuth` manager handles:
- Initial user authorization via browser
- Token storage and refresh
- Scope management (requesting permissions to create and modify playlists)

The required scope includes both `playlist-modify-private` and `playlist-modify-public` to ensure playlist creation works correctly.

### Song Matching
For each song in the scraped chart data, the program:
- Searches Spotify using both track name and artist name
- Retrieves the first matching result (most relevant match)
- Extracts the Spotify URI (unique identifier) for that track
- Handles cases where songs aren't found on Spotify

The dual search criteria (track + artist) significantly improves matching accuracy compared to searching by track name alone.

### Playlist Creation
Once all available songs are matched:
- A new playlist is created with a name indicating the chart date
- All found track URIs are added to the playlist in one batch operation
- The playlist appears in the user's Spotify account immediately

---

## Code Overview

```python
# Scrape Official Charts for song and artist data
soup = BeautifulSoup(response.text, "html.parser")
songs = soup.find_all(name="div", class_="description block")
song_list = []
for item in songs:
    song_data = item.find_all(name="span", class_=None)
    song_list.append({
        "song": song_data[0].text.strip(),
        "artist": song_data[1].text.strip()
    })

# Authenticate with Spotify using OAuth
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="playlist-modify-private playlist-modify-public"
    )
)

# Search Spotify for each song and collect URIs
for item in song_list:
    result = sp.search(q=f"track:{song} artist:{artist}", type="track", limit=1)
    if result["tracks"]["items"]:
        uri = result["tracks"]["items"][0]['uri']
        song_uris.append(uri)

# Create playlist and add all found tracks
playlist = sp.current_user_playlist_create(name=f"UK chart songs from {date}")
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
```

---

## Key Features

- **Date-based chart retrieval**: Access UK Singles Chart data from any historical date
- **Automated Spotify integration**: OAuth authentication handled seamlessly
- **Intelligent song matching**: Searches using both track and artist names for accuracy
- **Batch playlist creation**: Adds all songs in one operation for efficiency
- **Error handling**: Gracefully handles songs not found on Spotify
- **User-friendly interface**: Simple command-line prompts for date input
- **Secure credential management**: API credentials stored in environment variables

---

## Technical Skills Demonstrated

- **Web Scraping**: Using BeautifulSoup to parse HTML and extract structured data
- **API Integration**: Working with Spotify Web API via Spotipy library
- **OAuth 2.0 Authentication**: Implementing OAuth flow for secure API access
- **Data Transformation**: Converting scraped chart data into Spotify-compatible format
- **Error Handling**: Managing API rate limits and missing data gracefully
- **Environment Security**: Protecting API credentials with environment variables
- **String Manipulation**: Formatting dates and handling text data (strip, zfill)
- **List Comprehension**: Efficiently building data structures from scraped content

---

## Project Challenges & Solutions

### Challenge 1 - Song Matching Accuracy

**Issue:** Initial implementation searched only by song title, resulting in poor match accuracy. Songs with common titles returned incorrect results, and re-releases/covers were often mismatched.

**Solution:** Enhanced search queries to include both track name AND artist name (`track:{song} artist:{artist}`). This dual-criteria approach dramatically improved match accuracy, achieving approximately 85% successful matches across typical chart data.

### Challenge 2 - Website Structure Changes

**Issue:** The original course used Billboard.com charts, which subsequently implemented a paywall for historical chart data, making the project impossible to complete as originally designed.

**Solution:** Pivoted to the UK Official Charts (officialcharts.com), which provides free access to historical chart data. Adapted the web scraping logic to target the different HTML structure, identifying song titles and artists in `<span>` elements within `<div class="description block">` containers.

### Challenge 3 - Date Format Handling

**Issue:** Official Charts URLs require dates in YYYYMMDD format with zero-padded months and days. User input of single-digit months or days (e.g., "6" for June) would create malformed URLs.

**Solution:** Implemented Python's `zfill(2)` method to automatically pad single-digit inputs with leading zeros, ensuring consistent URL formatting regardless of user input style.

### Challenge 4 - Partial Match Results

**Issue:** Approximately 10-15% of chart songs cannot be found on Spotify due to:
- Artist name formatting differences (e.g., "feat." vs "featuring" vs "&")
- Retroactive title changes (historical songs renamed for re-releases)
- Regional licensing restrictions
- Songs not available on Spotify platform

**Solution:** Implemented graceful degradation - the program prints a notification for songs not found and continues processing the remaining tracks. This allows users to get 85-90% of chart songs in their playlist rather than failing entirely. Further improvements could include fuzzy matching algorithms and multiple search strategies, but the current success rate is acceptable for a learning project.

---

## Use Cases

- **Nostalgia trips**: Recreate the music atmosphere from significant personal dates (birthdays, anniversaries, etc.)
- **Music discovery**: Explore what was popular during different eras
- **Event planning**: Create themed playlists for decade parties or historical events
- **Music education**: Study chart trends and popular music evolution over time
- **Personal time capsules**: Build playlists from meaningful dates in your life

---

## Known Limitations

- **Playlist privacy**: Due to Spotipy API behavior, playlists are created as public by default. Users can manually set them to private in Spotify after creation.
- **Match accuracy**: Approximately 10-15% of songs may not be found due to artist name formatting variations, licensing restrictions, or availability on Spotify.
- **Chart coverage**: Limited to UK Official Singles Chart data; does not include other regional charts.
- **Historical data**: Chart data availability depends on Official Charts website archives.

---

## Notes

- The application creates a new playlist each time it runs, even if a playlist with the same date already exists
- Authentication tokens are cached locally after first authorization for convenient re-use
- Songs not found on Spotify are logged to the console but do not prevent playlist creation
- The Official Charts website automatically redirects dates to the Sunday of that chart week
- Search results prioritize exact matches but may occasionally return covers or alternative versions
