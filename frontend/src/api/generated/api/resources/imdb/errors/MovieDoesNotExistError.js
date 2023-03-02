/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as errors from "../../../../errors";
export class MovieDoesNotExistError extends errors.ImdbApiError {
    constructor(body) {
        super({
            message: "MovieDoesNotExistError",
            statusCode: 404,
            body: body,
        });
        Object.setPrototypeOf(this, MovieDoesNotExistError.prototype);
    }
}
