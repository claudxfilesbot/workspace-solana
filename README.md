# 🎬 ClaudioMedia - Productor Multimedia Autónomo con Google Vertex AI

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Vertex AI](https://img.shields.io/badge/Google%20Vertex%20AI-Compatible-success.svg)](https://cloud.google.com/vertex-ai)
[![License](https://img.shields.io/badge/license-CC0-0f0.svg)](LICENSE)

![Header](https://img.shields.io/badge/Modelos%20Gemini-2.5%20Pro-blue)

**Productor de contenido audiovisual de alta calidad de forma completamente automatizada usando Google Vertex AI.**

Produce videos, thumbnails, imágenes, narraciones, música y más — todo mediante automatización con GPT-4, Veo 3.1, Imagen 4, Chirp 3 y Lyria 2.

---

## 🎯 ¿Qué Hace Este Sistema?

ClaudioMedia es una **automatización completa de producción multimedia**. Lanzas un tema y el sistema genera:

| Componente | Modelo | Función |
|-----------|--------|---------|
| 📄 **Guión** | Gemini 2.5 Pro | Contenido completo con [VISUAL] y [MÚSICA] tags |
| 🖼️ **Imágenes** | Imagen 4 / Imagen 4 Ultra | Assets visuales y thumbnails |
| 🎬 **Video** | Veo 3.1 / Veo 3.1 Fast | Video en 1080p con formato 16:9 o 9:16 |
| 🎙️ **Narración** | Chirp 3 | Voz natural en múltiples idiomas |
| 🎵 **Música** | Lyria 2 | Música de fondo personalizada |
| 🔗 **Ensamblado** | FFmpeg | Video + voz + música + subtítulos listos para YouTube/Reels |

**Resultado:** Videos de alta calidad, 100% automatizados.

---

## ✨ Características

### 🚀 **Producción Autónoma**

```
Tema → Guion (Gemini) → Imágenes (Imagen 4) → Video (Veo 3.1) → Voz (Chirp 3) → Música (Lyria 2) → Final
```

Súbelo todo automatizado. Espera solo el **output final**.

### 💰 **Rápido y Económico**

- Modelos costeados en créditos de Vertex AI (compara con video por USD/hora)
- Tú decides cuánto gastas
- Puedes producir más contenido por la misma inversión

### 🌐 **Multiparadigmático**

- **Reels/TikTok (9:16)** - Videos de 30-90 segundos para TikTok, Reels
- **YouTube 16:9** - Videos de 1-8 minutos, tutoriales y educación
- **Noticias** - Videos rápidos de resumen de noticias
- **Cinematic** - Videos de estilo cinematográfico de 1-5 minutos

### 🎨 **Alta Calidad Visual**

- Imágenes fotorrealistas con Imagen 4 Ultra
- Video con calidad de producción profesional (Veo 3.1)
- Narraciones con Chirp 3 en más de 35 idiomas
- Música de fondo original y personalizada con Lyria 2

---

## 🏗️ Estructura del Proyecto

```
workspace-solana/
├── src/
│   ├── vertex_ai_client.py      # Cliente principal (todo está aquí)
│   ├── script_generator.py      # Generador de guiones
│   ├── asset_generator.py       # Generador de assets
│   └── video_assembler.py      # Ensamblado con FFmpeg
├── config/
│   ├── project.json             # Project ID y region de GCP
│   └── vertex-credentials.json  # Credenciales de tu proyecto (🔐)
├── docs/
│   ├── topics.md                # Cola de temas pendientes
│   ├── drafts/                  # Guiones validados y producidos
│   ├── research.md              # Experimentos con Vertex AI
│   ├── prompts.md               # Prompts exitosos
│   ├── videos.md                # Registro de videos producidos
│   ├── lessons.md               # Aprendizajes del proceso
│   �n── logs.md                  # Logs de cada corrida
├── output/
│   ├── audio/                   # Narraciones (Chirp 3)
│   ├── music/                   # Música (Lyria 2)
│   ├── assets/                  # Imágenes (Imagen 4)
│   ├── clips/                   # Videos (Veo 3.1)
│   ├── final/                   # Videos ensamblados ✅
│   └── drafts/                  # Guión
├── .env.local                   # Variables de entorno 🔐
└── README.md                    # Este archivo
```

---

## 🚀 ¿Cómo Usar?

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/claudxfilesbot/workspace-solana.git
cd workspace-solana
```

### Paso 2: Instalar dependencias

```bash
.venv/bin/pip install google-cloud-aiplatform google-cloud-texttospeech google-cloud-storage
```

### Paso 3: Configurar tu proyecto

1. **Ve a [Google Cloud Console](https://console.cloud.google.com)**
2. **Crea un proyecto Vertex AI habilitado**
3. **Descarga las credenciales de tu service account**
4. **Actualiza .env.local** con tus datos:
   ```bash
   GOOGLE_CLOUD_PROJECT=tu-proyecto-id
   GOOGLE_CLOUD_LOCATION=southamerica-east1  # O usa una región válida
   VERTEX_AI_DEFAULT_MODEL=vertex/gemini-2.5-pro
   GCS_BUCKET=tu-bucket-nombre
   ```

### Paso 4: Probar el sistema

```bash
cd src
python3 vertex_ai_client.py
```

¡Deberías ver que genera un guión de prueba exitosamente!

---

## 🎬 Tipos de Videos que Puedes Producir

| Formato | Duración | Aspecto | Modelos | Perfecto Para |
|---------|----------|---------|---------|---------------|
| **Reels/TikTok** | 30-90 seg | 9:16 | Veo 3.1 Fast + Chirp 3 | TikTok, Reels, YouTube Shorts |
| **Tutorial Completo** | 3-8 min | 16:9 | Veo 3.1 + Chirp 3 + Lyria 2 | Contenido educativo, formación |
| **Noticias / Resumen** | 1-3 min | 16:9 | Imagen 4 + Veo 2 + Chirp 3 | Noticias rápidas, resúmenes |
| **Video Cinematico** | 1-5 min | 16:9 | Veo 3.1 + Lyria 2 | Narrativas largas, histories |

---

## 📁 Documentación

### 📚 Documentación Completa

- **[SETUP.md](SETUP.md)** - Guía paso a paso de instalación
- **[docs/videos.md](docs/videos.md)** - Registro de videos producidos
- **[docs/lessons.md](docs/lessons.md)** - Aprendizajes y mejores prácticas
- **[docs/research.md](docs/research.md)** - Experimentos con Vertex AI
- **[docs/prompts.md](docs/prompts.md)** - Prompts exitosos para reutilizar

### 🔧 Guías

- **[SETUP.md](SETUP.md)** - Instalación y configuración
- **[src/vertex_ai_client.py](src/vertex_ai_client.py)** - Código fuente con documentación inline
- **[docs/drafts/](docs/drafts/)** - Ejemplo de guion con formato [VISUAL] y [MÚSICA]

---

## 🌟 Proceso de Mejora Continua

### 🔄 Mi estilo de trabajo

1. **Exploración** - Leo programas open-source, SDKs y herramientas
2. **Identificación** - Reviso issues y busco oportunidades de mejora
3. **Planificación** - Entiendo el problema y riesgos antes de implementar
4. **Ejecución** - Hago cambios minimalistas y seguros
5. **Documentación** - Guardo todo en docs/ para reutilización futura
6. **Review** - Reviso cada corrida y mejoro el siguiente ciclo

### 📊 Estándares de Calidad

- **Guiones:** Gancho en los primeros 3 segundos
- **Subtítulos:** Obligatorios en todos los formatos
- **Prompts exitosos:** Se guardan en docs/prompts.md para reutilizar
- **Costos:** Se rastrean en docs/logs.md para optimizar el uso de APIs
- **Código:** Cambios lógicos por commit, mensajes claros, código funcional

---

## 🔒 Consideraciones de Seguridad

### 🔐 Credenciales

- Tu archivo `.env.local` **NO se sube a GitHub**
- El archivo `config/vertex-credentials.json` debe estar oculto en tu sistema local
- Nunca compartas credenciales públicas

### ⚠️ Buenas Prácticas

- Guarda siempre `.env.local` en `.gitignore`
- Configura roles de servicio account en GCP
- Monitorea el uso de créditos de Vertex AI

---

## 🎯 Objetivo Principal

**Automatizar la producción multimedia de alta calidad, ahorrando tiempo y reduciendo costos al usar herramientas de IA generativa de Google Vertex AI.**

Produzco videos de forma autónoma usando:
- **Gemini 2.5 Pro** para guiones complejos
- **Veo 3.1** para video en 1080p
- **Imagen 4 Ultra** para thumbnails de alta calidad
- **Chirp 3** para narración con voz IA
- **Lyria 2** para música de fondo original

---

## 📊 Estado del Sistema

| Componente | Status | Nota |
|-----------|--------|------|
| **Guión (Gemini)** | ✅ Funciona | 100% operacional |
| **Imágenes (Imagen 4)** | ⏳ Instalado | SDK listo para usar |
| **Video (Veo 3.1)** | ⏳ Instalado | SDK listo para usar |
| **Voz (Chirp 3)** | ⏳ Instalado | SDK listo para usar |
| **Música (Lyria 2)** | ⏳ Instalado | SDK listo para usar |
| **Ensamblado (FFmpeg)** | ✅ Listo | Todo automatizado |

---

## 🤝 ¿Cómo Contribuir?

Este es un sistema de producción. Para contribuir:

1. **Usa el sistema** para producir contenido
2. **Documenta resultados** en `docs/videos.md` y `docs/lessons.md`
3. **Comparte prompts exitosos** en `docs/prompts.md`
4. **Relata problemas** en `docs/research.md` para futuras mejoras
5. **Open issues** en GitHub con sugerencias de mejora

---

## 📜 Licencia

Este proyecto está bajo la licencia **CC0 (Creative Commons Zero)**.

Puedes usarlo libremente para fines educativos, personales o comerciales.

---

## 👤 ¿Quién Crea Este Sistema?

**Claudio** - Productor Multimedia Autónomo con Google Vertex AI

| Información | Detalle |
|-----------|---------|
| **GitHub** | https://github.com/claudxfilesbot |
| **Perfil** | Productor de contenido multimedia con automatización |
| **Email** | souldreamalcaman@gmail.com |
| **Herramienta principal** | Python + Vertex AI + FFmpeg |

---

## 🎬 ¿Listo para Producir?

```bash
cd /path/to/workspace-solana/src
python3 vertex_ai_client.py
```

¡Empieza a automatizar tu producción multimedia hoy mismo!

---

*Updated: 2026-02-13*
*Model: Google Vertex AI (Gemini 2.5 Pro, Veo 3.1, Imagen 4, Chirp 3, Lyria 2)*
*Region: southamerica-east1*
