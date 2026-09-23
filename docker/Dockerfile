# ============================================================
# Systra GIS Data Portal — Dockerfile
# ============================================================
FROM python:3.12-slim

# ── System dependencies ─────────────────────────────────────
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    libgdal-dev \
    gdal-bin \
    libxml2-dev \
    libxslt-dev \
    && rm -rf /var/lib/apt/lists/*

# ── Working directory ───────────────────────────────────────
WORKDIR /app

# ── Python dependencies ─────────────────────────────────────
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# ── Application code ────────────────────────────────────────
COPY . /app/

# ── Static files ────────────────────────────────────────────
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

# ── Port ────────────────────────────────────────────────────
EXPOSE 8001

# ── Entrypoint ──────────────────────────────────────────────
CMD ["gunicorn", \
     "--bind", "0.0.0.0:8001", \
     "--workers", "3", \
     "--timeout", "120", \
     "--access-logfile", "-", \
     "--error-logfile", "-", \
     "portal.wsgi:application"]
