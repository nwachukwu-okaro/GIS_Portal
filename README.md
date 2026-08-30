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

## Portal authentication

The portal uses `accounts.User`, a custom email-and-password Django user,
with optional business information in `accounts.Profile`. There is no public
registration route: administrators create approved accounts in Django admin.
Catalogue pages, previews, assets and downloads require login; MinIO/PostGIS
uploads additionally require the `accounts.upload_data` permission.

Local development stores the same models in SQLite. Production stores Django
operational tables in the dedicated PostgreSQL `p_gisportal` schema using the
search path `p_gisportal,public`. Catalogue records remain in
`p_pycsw.records`, which application queries address explicitly.

Before the first production migration, create `p_gisportal` and grant the
Django database role `USAGE` and `CREATE` on it. Then run:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Do not add `p_pycsw` to Django's search path: that schema may contain the old
default-user migration history and would prevent a clean custom-user setup.
