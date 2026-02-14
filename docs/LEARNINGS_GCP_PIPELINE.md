# Aprendizajes: Pipeline de Video Autónomo con Vertex AI

Este documento resume los desafíos técnicos y soluciones finales para el proyecto "NEURAL CODE".

## 1. Región y Compatibilidad (Veo 3.1)
- **Desafío:** Modelos nuevos como Veo 3.1 tienen disponibilidad limitada regionalmente.
- **Solución:** Consolidar toda la infraestructura en **us-central1**.

## 2. El Bug de los Operation IDs (UUID vs Long)
- **Descubrimiento:** La API de Vertex AI (Veo 3.1) devuelve UUIDs como `operation_id`, pero los comandos de consulta de Google (`gcloud` o SDKs) a veces requieren un formato numérico Long.
- **Error típico:** `The Operation ID must be a Long, but was instead: UUID-string`.
- **Estrategia de Bypass:** No depender de la consulta del ID. En su lugar, implementar un monitoreo directo del bucket de salida o de la respuesta final de la LRO para capturar la URI temporal del video.

## 3. Estructura de Petición Veo 3.1
- **Auditoría:** Veo 3.1 no soporta `outputConfig` dentro de la petición inicial de la misma forma que Imagen.
- **Solución:** Capturar la `gcsUri` temporal que devuelve el modelo al terminar la operación y mover el archivo manualmente con `gsutil` al bucket definitivo.

## 4. Scopes de Autenticación
- **Aprendizaje:** Para llamar a los modelos generativos, no basta con tener permisos de Storage; la sesión debe inicializarse con el scope `https://www.googleapis.com/auth/cloud-platform`.

## 5. Validación "Fail Fast"
- **Táctica:** El uso de frames estáticos (Imagen 4) permitió validar la dirección de arte antes de esperar los 15 minutos de renderizado de video, optimizando cuotas y tiempo.

---
*Documentado por claudxfilesbot - 2026-02-14*
