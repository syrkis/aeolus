FROM python:3.11.4

WORKDIR /workspace

RUN apt-get update && apt-get install -y gdal-bin libgdal-dev

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt