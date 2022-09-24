#!/bin/sh
gunicorn 'app:app' \
    --bind '0.0.0.0:5000' \
    --workers 1 \
    --access-logfile "-" \
    --error-logfile "-" \
    --capture-output \
    --reload