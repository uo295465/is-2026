#!/bin/bash

# Detener el contenedor anterior si estaaba corriendo
docker stop nginx 2>/dev/null || true

# Lanzar el contenedor con los dos sitios, puertos 80 y 81 mapeados
docker run --rm -d \
  --network pruebas \
  --name nginx \
  -p 80:80 \
  -p 81:81 \
  -v $(pwd)/html:/usr/share/nginx/html \
  -v $(pwd)/html2:/usr/share/nginx/html2 \
  -v $(pwd)/sitios_nginx:/etc/nginx/conf.d \
  nginx

echo "Nginx desplegado correctamente con los dos sitios web."