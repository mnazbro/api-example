import { MovieApiClient } from "../api";

const SERVER = "http://localhost:8080"

export const movieApiClient = new MovieApiClient({
    environment: SERVER,
});
