def get_movies():
    movies = []
    try:
        with open("exercises/nov1/movie.txt") as file:
            for line in file:
                movie = line.strip()
                movies.append(movie)
    except FileNotFoundError:
        print("Invalid file name.")

    return movies

movies = get_movies()

for movie in movies:
    print(movie)