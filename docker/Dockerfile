# ============================================================
# Systra GIS Data Portal — Django portal image
# ============================================================
FROM python:3.12-slim

WORKDIR /app

# Runtime and build libraries required by Django, PostGIS, Fiona and GeoPandas.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gdal-bin \
    libgdal-dev \
    libgeos-dev \
    libpq-dev \
    libproj-dev \
    proj-bin \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy only the application files needed by the portal. In particular, do not
# copy .env or generated metadata into the image build context.
COPY manage.py /app/manage.py
COPY portal /app/portal
COPY accounts /app/accounts
COPY catalogue /app/catalogue
COPY templates /app/templates
COPY static /app/static
COPY docker/entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

# Seed the image's static directory for first-time volume creation. The
# entrypoint repeats this after the named volume is mounted at runtime.
RUN DJANGO_SECRET_KEY=build-time-collectstatic-only \
    DJANGO_DEBUG=False \
    GIS_DB_USER=placeholder \
    GIS_DB_PASSWORD=placeholder \
    GIS_DB_HOST=placeholder \
    GIS_DB_NAME=placeholder \
    MINIO_ACCESS_KEY=placeholder \
    MINIO_SECRET_KEY=placeholder \
    PYCSW_STAC_URL=mock \
    python manage.py collectstatic --noinput

EXPOSE 8001

ENTRYPOINT ["/app/entrypoint.sh"]
