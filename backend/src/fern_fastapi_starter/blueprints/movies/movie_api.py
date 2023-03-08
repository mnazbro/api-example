from fastapi import Depends

from fern_fastapi_starter.api.generated.resources.movie.service import AbstractMovieService
from fern_fastapi_starter.api.generated import Movie
from fern_fastapi_starter.blueprints.movies.controllers import MovieController


class MovieApi(AbstractMovieService):
    def __init__(self, movie_controller: MovieController = Depends(MovieController)):
        self._movie_controller = movie_controller

    def get_movie(self, *, movie_id: str) -> Movie:
        return self._movie_controller.get_movie(movie_id=movie_id)

    def get_all_movies(self) -> list[Movie]:
        return self._movie_controller.get_all_movies()

    def create_movie(self, *, body: Movie) -> None:
        self._movie_controller.create_movie(movie=body)

    def delete_movie(self, *, movie_id: str) -> None:
        self._movie_controller.delete_movie(movie_id=movie_id)
