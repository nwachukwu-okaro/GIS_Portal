#!/bin/sh
set -eu

# Run after the portal_static volume has been mounted so Nginx sees the
# current CSS and other static assets, even when the volume already existed.
python manage.py collectstatic --noinput

exec gunicorn \
  --bind 0.0.0.0:8001 \
  --workers 3 \
  --timeout 120 \
  --access-logfile - \
  --error-logfile - \
  portal.wsgi:application
