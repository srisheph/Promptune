
from ytmusicapi import YTMusic

# Initialize YouTube Music API
ytmusic = YTMusic()

def format_song_data(song):
    return {
        "title": song.get("title", "Unknown"),
        "artist": song["artists"][0]["name"] if song.get("artists") else "Unknown",
        "url": f"https://music.youtube.com/watch?v={song['videoId']}" if song.get("videoId") else None
    }

def get_recommended_songs(prompt):
    search_results = ytmusic.search(prompt, filter="songs")
    return [format_song_data(song) for song in search_results[:5]]


