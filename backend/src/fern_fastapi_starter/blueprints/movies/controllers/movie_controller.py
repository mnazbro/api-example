from fern_fastapi_starter.api.generated import Movie, InvalidMovieError, MovieId, MovieNotFoundError


class MovieController:
    def __init__(self):
        self._db: dict[str, Movie] = {}

    def get_movie(self, *, movie_id: str) -> Movie:
        movie = self._db.get(movie_id)
        if movie is None:
            raise MovieNotFoundError(MovieId.from_str(movie_id))
        return movie

    def get_all_movies(self) -> list[Movie]:
        return list(self._db.values())

    def create_movie(self, *, movie: Movie) -> None:
        movie_id = movie.id
        if movie_id in self._db:
            raise MovieNotFoundError(MovieId.from_str(movie_id))
        self._db[movie_id] = movie

    def delete_movie(self, *, movie_id: str) -> None:
        if movie_id in self._db:
            raise MovieNotFoundError(MovieId.from_str(movie_id))
        del self._db[movie_id]
