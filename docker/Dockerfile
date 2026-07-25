FROM python:3.12-slim

# Set working directory
WORKDIR /pycsw

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    libgdal-dev \
    gdal-bin \
    libxml2-dev \
    libxslt-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --no-cache-dir \
    pycsw \
    gunicorn \
    psycopg2-binary \
    boto3 \
    rasterio \
    setuptools==69.5.1 \
    sqlalchemy==1.4.52

# Copy project files
COPY config/pycsw.cfg /pycsw/config/pycsw.cfg
COPY scripts/ /pycsw/scripts/
COPY docker/wsgi.py /pycsw/wsgi.py

# Make ingestion script executable
RUN chmod +x /pycsw/scripts/run_ingest.sh

# Expose pycsw port
EXPOSE 8000

# Start pycsw with gunicorn using our wsgi entry point
CMD ["gunicorn", \
     "--bind", "0.0.0.0:8000", \
     "--workers", "2", \
     "--timeout", "60", \
     "--access-logfile", "-", \
     "--error-logfile", "-", \
     "--chdir", "/pycsw", \
     "wsgi:application"]
     