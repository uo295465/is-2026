#!/bin/bash

# crear la red de docker si no existe
docker network create pruebas 2>/dev/null || true

# lanzar los 3 contenedores servidores en la subred pruebas
docker run -d --rm --network pruebas -v $(pwd):/app python:3.7 python /app/udp_servidor6_broadcast.py
docker run -d --rm --network pruebas -v $(pwd):/app python:3.7 python /app/udp_servidor6_broadcast.py
docker run -d --rm --network pruebas -v $(pwd):/app python:3.7 python /app/udp_servidor6_broadcast.py

echo "Servidores iniciados correctamente."
docker ps

