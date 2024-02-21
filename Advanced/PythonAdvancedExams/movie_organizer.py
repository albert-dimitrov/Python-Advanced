def movie_organizer(*args):
    mery_collection = {}
    return_text = ''

    for movie, genre in args:
        if genre not in mery_collection:
            mery_collection[genre] = []

        mery_collection[genre].append(movie)

    mery_collection = sorted(mery_collection.items(), key=lambda x: (-len(x[1]), x[0]))

    for genre, movies in mery_collection:
        return_text += f"{genre} - {len(movies)}\n"
        for name in sorted(movies):
            return_text += f'* {name}\n'

    return return_text
