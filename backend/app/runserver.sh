#!/bin/bash
echo "Waiting for database..."

# while ! nc -z $DJANGO_DATABASE_HOSTNAME $DJANGO_DATABASE_PORT; do
    echo "DB not ready, keep waiting..."
    sleep 0.1
# done

echo "database started"
python manage.py makemigrations
python manage.py migrate

python manage.py flush --noinput -v 2
python manage.py loaddata init/fixtures.json
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:6001