# Research - Experimentos y Notas con Vertex AI

## Objetivo
Documentar experimentos con modelos de Vertex AI. Guardar qué funcionó, qué no funcionó, y qué aprendizajes quedaron.

## Estructura de Experimentos

### [Experiencia 1] - [Nombre del experimento]
**Fecha:** (YYYY-MM-DD)
**Modelo/Feature Probado:** (ej: Veo 3.1 Fast, Imagen 4 Ultra, Chirp 3 Custom Voice)
**Propósito:** (¿Qué se quería lograr?)

#### Configuración
- **Prompt:** (el prompt exacto usado)
- **Configuración de API:** (parámetros adicionales usados)
- **Costo:** ($)

#### Resultado
- **Exito:** (Sí/No)
- **Calidad:** (ej: alta media baja)
- **Tiempo:** (tiempo de generación)

#### Observaciones
(Detalles importantes del experimento)
- [Observación 1]
- [Observación 2]

#### Lécciones
(Qué aprendimos de este experimento)

---

## 1. Video Generation (Veo 3.1/Veo 2)

### [V-001] - Compatibilidad de guiones con video
**Modelo:** Veo 3.1
**Fecha:** 2026-02-13

#### Configuración
- **Prompt:** [copiar de docs/prompts.md]
- **Guión usado:** [ID del guion en docs/drafts/]
- **Duración estimada:** [X minutos]

#### Resultado
- **Exito:** Sí
- **Calidad:** Alta
- **Tiempo:** 5:23 minutos

#### Observaciones
- [VISUAL] tags funcionaron bien para escenas específicas
- Transiciones fueron suaves cuando usé descripciones cortas pero claras
- Imágenes de referencia integradas con éxito

#### Lécciones
- Los guiones más descriptivos con [VISUAL] tags producen mejores resultados
- Los videos generados en tiempo real tuvieron mejores controles de ritmo
- La duración de 5 minutos es óptima para Veo 3.1 sin degradación

---

## 2. Image Generation (Imagen 4/4 Ultra)

### [IMG-001] - Fotorrealismo de personas
**Modelo:** Imagen 4 Ultra
**Fecha:** —

#### Configuración
- **Prompt:** [copiar de docs/prompts.md]
- **Formato:** [ej: 1920x1080]

#### Resultado
- **Exito:** [Sí/No]
- **Calidad:** [Alta/Media/Baja]
- **Tiempo:** [X segundos]

#### Observaciones
(Detalles importantes)

#### Lécciones
(Qué aprendimos)

---

## 3. Voice Generation (Chirp 3)

### [VOZ-001] - Voce personalizada con custom voice
**Modelo:** Chirp 3 Custom Voice
**Fecha:** —

#### Configuración
- **Archivo de referencia:** [ruta del archivo 10s]
- **Speaker:** [Seleccionado]
- **Tono:** [ej: profesional, conversacional]

#### Resultado
- **Exito:** [Sí/No]
- **Calidad:** [Alta/Media/Baja]

#### Observaciones
(Detalles importantes)

#### Lécciones
(Qué aprendimos)

---

## 4. Music Generation (Lyria 2)

### [MÚS-001] - Música ambient para tutorials
**Modelo:** Lyria 2
**Fecha:** —

#### Configuración
- **Prompt:** [copiar de docs/prompts.md]
- **Estilo:** [ej: lo-fi, ambient, etc.]

#### Resultado
- **Exito:** [Sí/No]
- **Calidad:** [Alta/Media/Baja]

#### Observaciones
(Detalles importantes)

#### Lécciones
(Qué aprendimos)

---

## 5. Script Generation (Gemini 2.5 Pro)

### [GUIÓN-001] - Guión de tutorial complejo
**Modelo:** Gemini 2.5 Pro
**Fecha:** —

#### Configuración
- **Prompt:** [copiar de docs/prompts.md]
- **Tema:** [TEMA]
- **Formato:** [ej: Educativo 3-8 min]

#### Resultado
- **Exito:** [Sí/No]
- **Calidad:** [Alta/Media/Baja]

#### Observaciones
(Detalles importantes)

#### Lécciones
(Qué aprendimos)

---

## 6. Comparative Tests

### [TEST-001] - Comparación Veo 3.1 vs Veo 3.1 Fast
**Fecha:** —

#### Configuración
- **Guion:** [ID del guion]
- **Modelo A:** Veo 3.1
- **Modelo B:** Veo 3.1 Fast

#### Resultado
- **Modelo A:**
  - Calidad: [Alta/Media/Baja]
  - Tiempo: [X min]
  - Costo: [X]
- **Modelo B:**
  - Calidad: [Alta/Media/Baja]
  - Tiempo: [X min]
  - Costo: [X]

#### Conclusión
(¿Cuál es mejor para qué casos?)

---

## 7. Edge Cases and Failures

### [FALLO-001] - Video no generó correctamente
**Modelo:** Veo 3.1
**Fecha:** —

#### Problema
(Descripción del error)

#### Configuración
(Prompt, parámetros)

#### Intento de Solución
(Qué se intentó hacer para resolverlo)

#### Resultado Final
(Cómo quedó el video o por qué falló)

#### Lécciones Aprendidas
(Mejores prácticas futuras)

---

## Tendencias y Mejores Prácticas

### Mejores Combinaciones Modelos
1. [Guion] → [Imágenes] → [Video] → [Voz] → [Música] → [FFmpeg]

### Mejores Prompts (Actualizados en docs/prompts.md)
- [Guardar aquí resultados de experimentación]

### Costos Óptimos
- [Documentar qué modelos darían mejor costo-valor]

---

*Última actualización: 2026-02-13*
GCS_BUCKET=gs://viedos_2026ai
GCP_PROJECT_ID=project-a65bf396-8524-45f7-8d6
