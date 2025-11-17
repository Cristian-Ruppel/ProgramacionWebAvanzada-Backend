#!/bin/bash

# Le damos 5 segundos a Postgres para que termine de arrancar
echo "--- Esperando a que Postgres se levante (5 segundos)... ---"
sleep 8

# 1. Si no existe manage.py, crea el proyecto
if [ ! -f manage.py ]; then
  django-admin startproject app .
fi

# 2. Aplica las migraciones (esto sí es clave)
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# 3. Crea el superusuario SÓLO SI NO EXISTE
if [ ! -z "$DJANGO_SUPERUSER_NAME" ]; then
  echo "from django.contrib.auth.models import User; \
  User.objects.filter(username='$DJANGO_SUPERUSER_NAME').exists() \
  or User.objects.create_superuser('$DJANGO_SUPERUSER_NAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')" | python manage.py shell
fi

# 4. Arranca el servidor
python manage.py runserver 0.0.0.0:8000