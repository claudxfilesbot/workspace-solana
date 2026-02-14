# SETUP.md - Gu\u00eda de Configuraci\u00f3n

## R\u00e1pido

Si ya tienes las credenciales configuradas, solo ejecuta:

```bash
# 1. Instalar dependencias
pip install google-cloud-aiplatform google-cloud-texttospeech google-cloud-storage vertexai

# 2. Test de conexi\u00f3n
python src/vertex_ai_client.py
```

## Paso a Paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/claudxfilesbot/workspace-solana.git
cd workspace-solana
```

### 2. Configurar variables de entorno

El archivo `.env.local` debe contener:

```bash
# Google Cloud Configuration
GOOGLE_APPLICATION_CREDENTIALS=.secrets/vertex-credentials.json
GOOGLE_CLOUD_PROJECT=project-a65bf396-8524-45f7-8d6
GOOGLE_CLOUD_LOCATION=global
VERTEX_AI_DEFAULT_MODEL=vertex/gemini-3-pro-preview

# Output Configuration
OUTPUT_BUCKET=tu-bucket-nombre
OUTPUT_PREFIX=output/
```

### 3. Instalar dependencias

```bash
pip install google-cloud-aiplatform
pip install google-cloud-texttospeech
pip install google-cloud-storage
pip install vertexai
```

### 4. Verificar instalaci\u00f3n

```bash
python src/vertex_ai_client.py
```

Si todo est\u00e1 bien, ver\u00e1s:
```
🚀 Iniciando test de integración con Google Cloud...

1️⃣  Cargando configuración...
✅ Configuración cargada:
   Project ID: project-a65bf396-8524-45f7-8d6
   Location: global
   Default Model: vertex/gemini-3-pro-preview

2️⃣  Test de conexión a Vertex AI...
✅ Guion generado exitosamente (XXX caracteres)

3️⃣  Test de configuración de credenciales...
   Credenciales: project-a65bf396-8524-45f7-8d6@iam.gserviceaccount.com

========================================
✅ TEST COMPLETADO
========================================

⚠️  Notas importantes:
   1. SDK de Google Cloud SDK necesita instalar: pip install google-cloud-aiplatform
   2. Cada API necesita sus propios paquetes:
      - Guiones: google-cloud-aiplatform (Gemini)
      - Video: google-cloud-aiplatform (Veo)
      - Imágenes: google-ai-unity (Imagen)
      - Voz: google-cloud-texttospeech (Chirp 3)
      - Música: google-cloud-texttospeech (Lyria 2)
   3. Necesito obtener las credenciales instaladas correctamente
```

## Modelos Disponibles

| Modelo | Propósito | SDK |
|--------|-----------|-----|
| gemini-3-pro-preview | Guiones complejos, razonamiento | google-cloud-aiplatform |
| veo-3.1 | Video 1080p hasta 60s | google-cloud-aiplatform |
| veo-3.1-fast | Videos rápidos, prototipos | google-cloud-aiplatform |
| veo-2 | Control de cámara | google-cloud-aiplatform |
| imagen-4 | Imágenes fotorrealistas | google-ai-unity |
| imagen-4-ultra | Máxima calidad | google-ai-unity |
| imagen-4-fast | Generación rápida | google-ai-unity |
| chirp-3 | Narración con voz IA | google-cloud-texttospeech |
| lyria-2 | Música original | google-cloud-texttospeech |

## Próximos Pasos

1. ✅ Confirmar que funciona el test
2. 📋 Agregar temas a `docs/topics.md`
3. 📝 Usar guion de ejemplo para testear producción completa
4. 🚀 Producir primer video real

---

*Última actualización: 2026-02-13*