#!/usr/bin/env bash

echo "Starting"

flask db upgrade


echo "OK"

gunicorn app:app --bind=0.0.0.0:8000

exec "$@"
