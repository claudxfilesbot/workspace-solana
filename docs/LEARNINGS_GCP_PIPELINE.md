# Aprendizajes: Pipeline de Video Autónomo con Vertex AI

Este documento resume los desafíos técnicos y soluciones encontradas durante la configuración del pipeline para "NEURAL CODE".

## 1. Región y Compatibilidad (Veo 3.1)
- **Desafío:** Modelos nuevos como Veo 3.1 tienen disponibilidad limitada regionalmente. Intentar operar en regiones de Sudamérica causó fallos de API.
- **Solución:** Consolidar toda la infraestructura (Buckets, Vertex AI, Service Agents) en **us-central1**.

## 2. Permisos del "Service Agent" (El eslabón perdido)
- **Desafío:** La cuenta de servicio del usuario tenía permisos, pero el video no aparecía en el bucket.
- **Aprendizaje:** Vertex AI usa una identidad interna llamada "Service Agent" (`service-PROJECT_NUMBER@gcp-sa-aiplatform.iam.gserviceaccount.com`) para depositar archivos.
- **Solución:** Otorgar el rol `Storage Object Admin` explícitamente a esta identidad en el bucket destino.

## 3. Manejo de Credenciales
- **Estrategia:** El uso de una llave JSON local activa (`vertex-express-key.json`) permitió autonomía total para herramientas CLI (`gcloud`, `gsutil`) y scripts de Python.

## 4. Validación "Fail Fast"
- **Táctica:** Antes de renders largos, validar con videos de 5s o subidas directas de archivos pequeños. Esto ahorró costos y tiempo de depuración.

---
*Documentado por claudxfilesbot - 2026-02-13*
