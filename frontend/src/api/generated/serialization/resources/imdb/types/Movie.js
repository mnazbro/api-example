/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as core from "../../../../core";
export const Movie = core.serialization.object({
    id: core.serialization.lazy(async () => (await import("../../..")).MovieId),
    title: core.serialization.string(),
    rating: core.serialization.number(),
});