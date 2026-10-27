
#!/bin/bash
# Uso: ./registro.sh NOMBRE_DEL_EXPERIMENTO   (ejemplo: ./registro.sh exp1)
SALIDA="resultados_$1.txt"
TABLA="NOMBRE_TABLA"

{
  echo "===== $1 - $(date) ====="
  echo "--- Contenedores ---"
  docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
  echo "--- Consumo de contenedores ---"
  docker stats --no-stream
  echo "--- Host ---"
  echo "Núcleos: $(nproc)"
  uptime
  free -h
  top -bn1 | head -5
  echo "--- Registros en la base de datos ---"
  docker exec basedatos mariadb -u amigosuser -pamigospass amigosdb -e "SELECT COUNT(*) AS registros FROM $TABLA;"
  echo "--- Tiempo medio de respuesta (10 peticiones) ---"
  for URL in api html; do
    for i in $(seq 1 10); do
      curl -s -o /dev/null -w "%{time_total}\n" http://127.0.0.1/$URL/amigos
    done | awk -v u=$URL '{s+=$1} END {printf "/%s/amigos: %.4f s\n", u, s/NR}'
  done
} | tee "$SALIDA"