def add_songs(*args):
    song_data = {}

    result = ''

    for title, lyrics in args:
        if title not in song_data.keys():
            song_data[title] = ''

        current_lyrics = ''

        for line in lyrics:
            current_lyrics += f"{line}\n"

        song_data[title] += current_lyrics

    for song_title, song in song_data.items():
        result += f"- {song_title}\n"
        if song:
            result += song

    return result

