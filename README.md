# GIS Portal

A Systra UK and Ireland portal for finding, understanding and processing
authoritative GIS data held in PostGIS and MinIO.

## Development roadmap

1. Build deterministic, agent-readable metadata for authoritative `a_*` schemas.
2. Build controlled GIS tools such as filter, buffer, clip, intersection and join.
3. Connect natural-language planning to metadata discovery and the GIS tools.
4. Harden, document and clean up the application for production.
5. Perform end-to-end, security and user-acceptance testing.

Phase One is implemented in `metadata_builder/`. See
`metadata_builder/README.md` for production and development commands.
