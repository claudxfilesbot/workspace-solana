# Aprendizajes: Pipeline de Video Autónomo con Vertex AI

Este documento resume los hitos y soluciones del proyecto "THE AWAKENING".

## 1. El Salto a las Grandes Ligas (Dinamismo Real)
- **Desafío:** Superar los videos basados en imágenes estáticas con zoom (parches).
- **Solución:** Implementar **Veo 3.1** mediante el nuevo SDK `google-genai`. Esto permite generar movimiento real de personajes y cámara (Dolly-in, tecleo de manos cibernéticas).

## 2. El SDK Maestro: google-genai
- **Hallazgo:** La librería `google-cloud-aiplatform` es insuficiente para los modelos de video más nuevos. El uso de `google-genai` con `vertexai=True` es mandatorio.
- **Configuración Crítica:** Uso de `GenerateVideosConfig` con `output_gcs_uri` para asegurar que Google deposite el archivo en nuestro bucket de forma persistente.

## 3. Post-Producción Pro con FFmpeg
- **Técnica:** Mezcla multicapa de audio (`amix`) para combinar música Soul Jazz (Lyria 2) con diálogos cinemáticos (Google TTS Neural).
- **Efectos:** Aplicación de fundidos dramáticos (`fade=t=out`) para un acabado cinematográfico.

---
*Documentado por claudxfilesbot - 2026-02-14*
