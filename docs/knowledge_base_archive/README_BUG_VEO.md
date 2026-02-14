# 🐛 Bug Conocido de Veo API

## El Problema
La API de Veo tiene un bug:
- Al generar, devuelve: `operation_id = "214b3f3c-f3c7-4b72-8846-0ef00e952e4d"` (UUID)
- Al verificar, requiere: un número Long (entero)
- Resultado: Error 400 "The Operation ID must be a Long"

## Soluciones

### Opción 1: Usar la Consola Web
1. Genera desde CLI/API
2. Verifica en: https://console.cloud.google.com/vertex-ai/generative/multimodal/gallery
3. Descarga manualmente

### Opción 2: Esperar Tiempo Fijo (SIN VERIFICAR)
Simplemente espera 15 minutos y luego busca en el bucket:
```bash
# Generar
operation_name=$(python3 generar_solo.py "prompt")

# Esperar 15 minutos (sin verificar)
sleep 900

# Buscar en el bucket
gsutil ls -l gs://viedos-2026ai-us/output/clips/VEO_REST_FINAL/ | tail -1
```

### Opción 3: Polling del Bucket
Verificar periódicamente si apareció un video nuevo en el bucket
