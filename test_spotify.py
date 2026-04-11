from spotify_recommender import get_spotify_songs

songs = get_spotify_songs("happy")

for s in songs:
    print(s)
