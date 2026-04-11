import webbrowser

def open_youtube(song_name, artist):
    query = f"{song_name} {artist}"
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(url)