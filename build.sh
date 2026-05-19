#!/bin/bash
set -o errexit

# Build script for Render

# Install dependencies
pip install -r requirements.txt

# Run migrations
python securitywebpage/manage.py migrate --noinput

# Collect static files
python securitywebpage/manage.py collectstatic --noinput
