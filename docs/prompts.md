# Prompts Exitosos - Prompts que funcionan bien

## Objetivo
Guardar prompts exitosos que funcionaron en producción. El objetivo es poder reutilizarlos y adaptarlos rápidamente.

## Categorías

### 1. Prompts de Guion (Gemini 2.5 Pro)

#### Guion Educativo - Tutorial Completo
```markdown
[Escribe un guion de tutorial de [DURACIÓN] minutos sobre [TEMA].

Formato: VIDEO EDUCATIVO 16:9
Duración: [DURACIÓN]

Estructura del guion:
1. HOOK (primeros 3 segundos): Gancho fuerte que capture la atención
2. INTRODUCCIÓN (primeros 30 segundos): Contexto y qué aprenderá el viewer
3. PARTE 1: [Subtema] - Explicación clara con ejemplos visuales
4. PARTE 2: [Subtema] - Práctica y ejemplos adicionales
5. CONCLUSIÓN (últimos 30 segundos): Resumen y llamada a la acción

Estilo de presentación: [Ejemplo: conversacional, didáctico, visual]

Para cada sección, incluye:
- [VISUAL: descripción detallada de la escena]
- [MÚSICA: descripción del tono y estilo musical a usar en esa sección]
- [TIEMPO: estimación de cuántos segundos dura cada parte]

Idioma: [ESPAÑOL]
Tono: [Didáctico, profesional pero accesible]
```

#### Guion Para Reels/TikTok
```markdown
[CREA UN GUION PARA UN REEL DE TIKTOK/REELS de [DURACIÓN] segundos sobre [TEMA].

Formato: REELS 9:16
Duración: [DURACIÓN]

Estructura del guion:
1. PRIMER FRAME (0-3 segundos): Gancho con visual impactante
2. HISTORIA (3-30 segundos): Narrativa corta con max 4-5 puntos clave
3. LLAMADA A LA ACCIÓN (30-60 segundos): Resumen + CTA

Para cada sección, incluye:
- [VISUAL: descripción breve pero clara]
- [MÚSICA: estilo musical, velocidad, tono]
- [TIEMPO: segundos exactos]

Idioma: [ESPAÑOL]
Tono: [Enérgico, rápido, visual]
```

---

## 2. Prompts de Imagen (Imagen 4/4 Ultra)

#### Prompt de Imagen Fotorrealista
```markdown
[GENERA UNA IMAGEN FOTORREALISTA DE:

DESCRIPCIÓN: [DESCRIBE EN DETALLE LA ESCENA]
FORMATO: [ej: 1920x1080]
TIPO: [ej: retrato, paisaje, ciudad, etc]

DETALLES CLAVE:
- Iluminación: [ej: luz natural del atardecer]
- Estilo: [ej: fotografía de estudio, estilo cinematográfico]
- Época: [ej: actualidad, 2020s]
- Estética: [ej: minimalista, saturación alta]

ACABADOS:
- Imagen calidad 4 Ultra (para thumbnails y portadas)
- Varias variantes diferentes entre sí
```

#### Prompt de Thumbnail
```markdown
[CREA UN THUMBNAIL DE ALTA IMPACTO PARA:

TEMA: [TEMA DEL VIDEO]

ELEMENTOS CLAVE:
- Título o headline: [TEXTO]
- Colores vibrantes y contrastantes
- Enfoque en FOCAL POINT que llame la atención
- Estilo: [ej: minimalista, informacional, emocional]

Formato: 16:9, resolución alta para YouTube

Retarget: Usa Imagen 4 Ultra para máxima calidad
```

---

## 3. Prompts de Voz (Chirp 3)

#### Prompt de Narración
```markdown
[GENERA UNA NARRACIÓN EN ESPAÑOL para un video de [DURACIÓN] minutos sobre [TEMA].

CARACTERÍSTICAS DE LA VOZ:
- Idioma: Español (España o Latinoamérica)
- Speaker: [Ejemplo: Sarah, Alex, Carlos, Emma]
- Tono: [ej: profesional, relajado, entusiasta, narrativo]
- Ritmo: [ej: moderado, lento para explicaciones complejas]
- Clarity: [ej: clara y articulada]

CARACTERÍSTICAS TÉCNICAS:
- Bitrate: 192 kbps (alta calidad)
- Sample rate: 44.1 kHz
- Formato: WAV
- Silence padding: 500ms antes y después

Estilo: [ej: conversacional, didáctica, storytelling]

Para guiones largos, divida en segmentos de máximo [DURACIÓN_SEGMENTO] minutos
```

---

## 4. Prompts de Video (Veo 3.1/3.1 Fast/Veo 2)

#### Prompt de Video desde Texto
```markdown
[CREA UN VIDEO COMPLETO desde texto para:

TEMA: [TEMA]
FORMATO: [ej: EDUCATIVO 16:9]
DURACIÓN: [ej: 3-8 minutos]

DESCRIPCIÓN VISUAL GENERAL: [Descripción general de la atmósfera y estilo del video]

ESTRUCTURA DEL VIDEO:
- Introducción visualmente impactante
- Secciones narrativas con transiciones suaves
- Referencias visuales clave mencionadas en el guión
- Estilo cinematográfico con movimiento suave

CARACTERÍSTICAS:
- Model: Veo 3.1 (alta calidad)
- Frame rate: 30 fps
- Resolution: 1080p
- Audio: narración integrada

Combinar con:
- Narración: [Archivo de audio generado]
- Música: [Archivo de música de fondo]
```

#### Prompt de Video cortado
```markdown
[GENERA UN VIDEO DE [DURACIÓN] segundos basado en:

CONTEXTO: [TEMA/CONCEPTO]
ESTILO: [ej: narrativo, visual, dinámico]

DETAILS:
- Primer frame: [Descripción del primer frame]
- Último frame: [Descripción del último frame]
- Referencias visuales: [Listado de referencias]
- Movimiento: [ej: suave, dinámico, cinemático]

Model: Veo 3.1 Fast (para prototipos rápidos)
Formato: 1080p
```

---

## 5. Prompts de Música (Lyria 2)

#### Prompt de Música de Fondo
```markdown
[GENERA MÚSICA DE FONDO para un video de:

CONTEXTO: [TEMA DEL VIDEO]
TONO: [ej: inspirador, relajante, dinámico, cinematográfico]
ESTILO: [ej: lo-fi, ambient, electrónico, orquestal]

DETALLES:
- Duración: [ej: 1:30 minutos, compatible con video]
- BPM: [ej: 90-120 BPM]
- Instrumentos: [ej: piano, pads, synthesizer]
- Voz: [ej: sin voz, voces suaves]

FORMATEO:
- MP3 de alta calidad
- Fade in/out de 5-10 segundos
- Volúmenes balanceados

PRECIOSOS:
- Usar Lyria 2 para máxima fidelidad
- Generar versión "clean" sin efectos pesados
```

---

## Reglas de Oro

1. **Siempre incluir las tags de contexto:**
   - `[TEMA: nombre del tema]`
   - `[FORMATO: tipo de video]`
   - `[DURACIÓN: tiempo estimado]`

2. **Para producción en serie:**
   - Copia los prompts, reemplaza solo las partes dinámicas
   - Guarda versiones diferentes para cada formato

3. **Para experimentación:**
   - Modifica los prompts de forma pequeña y específica
   - Documenta qué cambio hiciste y el resultado

4. **Para optimización:**
   - Si un prompt funcionó muy bien, marca el éxito en `docs/logs.md`
   - Si falló, anota qué fue el problema para no repetirlo

---

*Última actualización: 2026-02-13*
*Última verificación de funcionalidad: —*
