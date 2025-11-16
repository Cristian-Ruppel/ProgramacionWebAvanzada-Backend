FROM python:3.12-bookworm

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install python3-dev libgdal-dev graphviz-dev -y --force-yes

WORKDIR /usr/src/app

RUN pip install --upgrade pip && pip install --upgrade setuptools

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# 1. Copiamos el script que creamos (runserver.sh) desde la raíz del proyecto
#    a una nueva carpeta /scripts/ dentro del contenedor.
COPY runserver.sh /scripts/runserver.sh

# 2. Le damos permisos de ejecución a ese script.
RUN chmod +x /scripts/runserver.sh

CMD ["/scripts/runserver.sh"]