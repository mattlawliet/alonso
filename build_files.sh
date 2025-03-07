#!/bin/bash
echo "Starting build process..."

# Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# Create necessary directories and files for static content
mkdir -p static/myapp/img/
touch static/myapp/img/favicon.ico

# Only run migrations if DATABASE_URL is set
if [ -n "$DATABASE_URL" ]; then
  echo "Database URL found, running migrations..."
  python manage.py makemigrations
  python manage.py migrate
else
  echo "No DATABASE_URL found, skipping migrations"
fi

# Collect static files
python manage.py collectstatic --noinput

echo "Build process completed"