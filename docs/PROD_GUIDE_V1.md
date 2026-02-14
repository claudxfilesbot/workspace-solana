# 📚 Documentación para Bot Autónomo: Generación de Videos
**Proyecto:** NEURAL CODE
**Versión:** 1.0
**Fecha:** 14 Febrero 2026
**Estado:** Producción ✅

---

## 🎯 Capacidades Reales del Sistema

### ✅ Lo que FUNCIONA (100% confiable):
1. **Imagen 3** (`imagen-3.0-generate-001`) - Generación de frames estáticos de alta calidad
2. **Google TTS** - Síntesis de voz en múltiples idiomas y voces neurales
3. **FFmpeg** - Ensamblaje de video, audio, efectos visuales y transiciones
4. **gsutil** - Gestión de archivos en Google Cloud Storage
5. **Google Cloud Storage** - Almacenamiento confiable en `gs://viedos-2026ai-us/`

### ❌ Lo que NO funciona por API:
1. **Veo 3.1 via predictLongRunning** - **Bug conocido:** Devuelve UUID como operation ID pero requiere Long integer para consultar estado
2. **VideoGenerationModel en Python SDK** - No existe en la versión actual del SDK
3. **imagegeneration@006** - Modelo deprecado desde Junio 2025 - Usar `imagen-3.0-generate-001` en su lugar

---

## 🔧 Workflows Disponibles

### Workflow 1: Video con Frame Estático + Efectos (⭐ RECOMENDADO)
**Usar cuando:** Necesitas resultado rápido, confiable y profesional
**Tiempo estimado:** 3-5 minutos
**Confiabilidad:** 99%
**Calidad:** Alta (HD 1920x1080)

(Ver implementación técnica en el script automatizado)

---

*Guardado por claudxfilesbot bajo instrucción de Claudio Alcaman.*
