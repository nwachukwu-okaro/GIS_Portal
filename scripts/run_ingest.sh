#!/bin/bash
echo "Starting ingestion — $(date)"
source /home/systra.info/pokaro/pycsw-env/bin/activate
python /home/systra.info/pokaro/pycsw-catalogue/scripts/ingest_minio.py
python /home/systra.info/pokaro/pycsw-catalogue/scripts/ingest_postgis.py
echo "Ingestion complete — $(date)"