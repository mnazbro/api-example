import React, { useState, useEffect, useCallback, ChangeEventHandler } from "react";
import "./App.css";
import { movieApiClient } from "./services/movie";
import { InputGroup, ControlGroup, Button, Tag } from "@blueprintjs/core";
import { Movie } from "./api/generated/api";

function App() {
    const [movies, setMovies] = useState<Movie[]>([]);
    const [movieName, setMovieName] = useState("");
    const [error, setError] = useState<Error>();

    useEffect(() => {
        movieApiClient.movie.getAllMovies()
            .then(allMovies => setMovies(allMovies))
            .catch(error => setError(error as Error));
    }, []);

    const handleClick = useCallback(() => {
        movieApiClient.movie.createMovie({
            id: `id-${movieName}`,
            title: movieName,
            rating: Math.random() * 5,
        })
        movieApiClient.movie.getAllMovies()
            .then(allMovies => setMovies(allMovies))
            .catch(error => setError(error as Error));
    }, [movieName]);
    const handleTextChange: ChangeEventHandler<HTMLInputElement> = (x) => {
        setMovieName(x.target.value)
    };
    return (
        <div className="App">
            {movies.map(movie => {
                return (
                    <div key={movie.id}>
                        <Tag>{movie.id}</Tag>
                        <Tag intent={"primary"}>{movie.title}</Tag>
                        <Tag intent={"warning"}>{movie.rating}</Tag>
                    </div>
                )
            })}
            <ControlGroup>
                <InputGroup onChange={handleTextChange} value={movieName}/>
                <Button onClick={handleClick}>Create movie</Button>
            </ControlGroup>
            {error != null && <pre>{JSON.stringify(error, undefined, 4)}</pre>}
        </div>
    );
}


export default App;
