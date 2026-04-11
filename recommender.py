import pandas as pd

# Load music dataset
music = pd.read_csv("data/music.csv")

def recommend_music(emotion):
    # Filter songs based on mood
    filtered = music[music['mood'] == emotion]

    # If no songs found, return random songs
    if len(filtered) == 0:
        return music.sample(5).to_dict(orient="records")

    # Return 5 songs max
    return filtered.sample(min(5, len(filtered))).to_dict(orient="records")
