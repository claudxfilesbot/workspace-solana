# CICLO DIGITAL DE UNA LACTANCIA (24 SEGUNDOS)

**Tema:** El viaje invisible de un mensaje de leche materna de la madre al bebé
**Formato:** REELS 9:16
**Duración:** 24 segundos
**Estilo:** CINEMÁTICO / ETEREO / CORPORATIVO NATURAL

---

## ESTRUCTURA DEL GUIÓN (3 MICRO-ESCENAS × 8 SEGUNDOS)

### MICRO-ESCENA 1 (0-8s): LA ESFERA MATERNA
**[VISUAL:]** Primer plano de la glándula mamaria, textura piel clara, microvasos vibrantes brillando con luz cálida, células madre activas produciendo leche, burbujas de líquido transparente subiendo lentamente, campo macroscópico mostrando organización celular, halo suave de luz emitida
**[MÚSICA:]** Etereo, ambiental, tono celestial, glockenspiel sutil, nada invasivo, frecuencia cálida
**[TIEMPO:]** 0-8s

### MICRO-ESCENA 2 (8-16s): EL VIAJE INVISIBLE
**[VISUAL:]** Primer plano de una gota de leche cayendo desde la textura mamaria, flujo dramático pero suave, cámara moviéndose con la gota subiendo, escena macro de la gota viajando por el ducto, pasando desde zona mamaria hacia zona corporal, luz cambiando de cálida (zona mamaria) a nítida (zona corporal), intersección donde músculo suave se expande
**[MÚSICA:]** Música cambia a tono médico-techno sutil, ritmo cardíaco audiovisual, sonido visual de oxígeno sanguíneo, in crescendo suave
**[TIEMPO:]** 8-16s

### MICRO-ESCENA 3 (16-24s): EL RECONOCIMIENTO
**[VISUAL:]** Primer plano de un recién nacido dormido, el bebé abre ligeramente los ojos en reacción a la presencia de la leche, movimiento pulmonar, ritmo de respiración visualmente reflejado, bebé abre suavemente la boca buscando, luz natural cambiando a naranja cálida indicando conexión afectiva, primer chupetón con éxito, la boca en cámara de bebé muestra satisfacción, sonido de primer chupetón auditivo, cámara desvaneciéndose hacia luz suave (kinesis estética)
**[MÚSICA:]** Tono celestial retoma pero con menor intensidad, con climas de luz de sol, viento suave de bienvenida, crossfade a negro con acorde final
**[TIEMPO:]** 16-24s

---

## DETALLES TÉCNICOS DE PRODUCCIÓN

### Instrucciones a Veo 3.1 (3 clips de 8s)

**Clip 1 (0-8s):**
```markdown
Genera un primer plano de una glándula mamaria humana con textura de piel clara.
MOSTRAR: microvasos vibrantes brillantes con luz cálida, células madre activas produciendo leche, burbujas de líquido transparente subiendo lentamente, organización celular macroscópica.
ESTILO: CINEMÁTICO, FLUJO DE SANGRE, ETEREO, NO INVASIVO.
FORMATO: 9:16 (1080x1920), 30 fps, 1080p.
PRIMER FRAME: textura piel clara con microvasos vibrantes.
ÚLTIMO FRAME: burbujas subiendo lentamente con luz cálida.
```

**Clip 2 (8-16s):**
```markdown
Genera una gota de leche cayendo desde una textura mamaria hacia abajo.
MOSTRAR: gota cayendo con flujo dramático pero suave, cámara moviéndose con la gota, escena macro de gota viajando por ducto desde zona mamaria hacia zona corporal, luz cambiando de cálida a nítida, intersección de músculo suave expandiéndose.
ESTILO: CINEMÁTICO, FLUIDO, MEDICO-TECHNO, SUTILMENTE DRAMÁTICO.
FORMATO: 9:16 (1080x1920), 30 fps, 1080p.
PRIMER FRAME: gota cayendo desde mamaria.
ÚLTIMO FRAME: gota cruzando intersección muscular.
```

**Clip 3 (16-24s):**
```markdown
Genera un primer plano de un recién nacido dormido con ojos abriéndose en reacción.
MOSTRAR: bebé abriendo ojos suavemente en reacción a la leche, movimiento pulmonar, ritmo respiratorio visual, bebé abriendo boca buscando, primer chupetón con éxito, boca de bebé mostrando satisfacción, sonido de primer chupetón visual.
ESTILO: CINEMÁTICO, CASERO, EMOTIVO, CONEXIÓN Afectiva.
FORMATO: 9:16 (1080x1920), 30 fps, 1080p.
PRIMER FRAME: bebé dormido.
ÚLTIMO FRAME: baby con boca abierta en chupetón.
```

### Instrucciones a Chirp 3 (Narración de 24s)

```markdown
GENERA UNA NARRACIÓN EN ESPAÑOL para un video de 24 segundos sobre "El viaje invisible de la lactancia materna".

CARACTERÍSTICAS DE LA VOZ:
- Idioma: Español (Latinoamérica)
- Speaker: María (cálcida, maternal, femenina pero profesional)
- Tono: Etereo, emocional, corporativo, sin overwhelmt
- Ritmo: moderado, cada frase de ~8 segundos con pausas claras
- Clarity: clara y suave

CARACTERÍSTICAS TÉCNICAS:
- Bitrate: 192 kbps (alta calidad)
- Sample rate: 44.1 kHz
- Formato: WAV
- Silence padding: 500ms antes y después

ESTILO: narrativa cinematográfica, flujo minimalista, voz femenina maternal

Estructura (24s total):
- 0s-8s: "La leche es un viaje arquitectónico"
- 8s-16s: "Cada gota viaja por sistemas corporales complejos"
- 16s-24s: "Y llega exactamente donde necesita estar"

IDIOMA: Español
```

### Instrucciones a Lyria 2 (Música de 24s)

```markdown
GENERA MÚSICA DE FONDO para un video de 24 segundos sobre "El viaje invisible de la lactancia materna".

CONTEXTO: Viwes corporativo-éptico de lactancia
TONO: Etereo, emocional, biológico, misterioso, dulce
ESTILO: Ambient, glockenspiel sutil, nada invasivo, orquesta clínica

DETALLES:
- Duración: 1:00 minutos, compatible con video
- BPM: 60-70 BPM (pausas para narración)
- Instrumentos: glockenspiel, pads, violín sutil, piano de salón
- Voz: sin voz

FORMATO:
- MP3 de alta calidad
- Fade in/out de 5-10 segundos
- Volúmenes balanceados, música entre 25-30% del volumen total

REGLAS DE ORO:
- Música debe ser neutral y no invasiva
- No entrometerse con narración
- Cambios sutiles por cada escena sin shocks
- Usar Lyria 2 para máxima fidelidad
```

### Instrucciones a FFmpeg (Ensamblaje Final)

```bash
# Ensamblaje de 3 clips de 8s + narración + música + subtítulos

ffmpeg -y \
  -i clips/escena1_8s.mp4 \
  -i clips/escena2_8s.mp4 \
  -i clips/escena3_8s.mp4 \
  -i audio/narracion_lactancia_24s.wav \
  -i audio/musica_ambient_lactancia_24s.mp3 \
  -filter_complex "\
    [0:v]scale=iw*1.15:ih*1.15,format=yuv420p,pad=ih*0.768:iw*1.15:0:(ow-iw)/2:(oh-ih)/2,format=yuv420p[clip1];\
    [1:v]scale=iw*1.15:ih*1.15,format=yuv420p,pad=ih*0.768:iw*1.15:0:(ow-iw)/2:(oh-ih)/2,format=yuv420p[clip2];\
    [2:v]scale=iw*1.15:ih*1.15,format=yuv420p,pad=ih*0.768:iw*1.15:0:(ow-iw)/2:(oh-ih)/2,format=yuv420p[clip3];\
    [0:a][1:a][2:a]concat=n=3:v=1:a=1[audio] \
  " \
  -map "[clip1]" -map 3:a -i clips/escena2_8s.mp4 -map 4:a \
  -filter_complex "\
    [clip1][clip2]xfade=transition=fade:duration=0.5:transition_color=#00000000:output_width=9/16,output_height=16/9,format=yuv420p[clip12];\
    [clip12][clip3]xfade=transition=fade:duration=0.5:transition_color=#00000000:output_width=9/16,output_height=16/9,format=yuv420p[final];\
    [final][audio]amix=inputs=2:duration=first:dropout_transition=2,normalize=1[audio_final] \
  " \
  -map "[audio_final]" \
  -shortest \
  -c:v libx264 \
  -preset medium \
  -crf 23 \
  -c:a aac \
  -b:a 192k \
  -pix_fmt yuv420p \
  output/final/lactancia_viaje_invisible_24s.mp4

# Notas de FFmpeg:
# - scale*iw*1.15/ih*1.15: zoompan de 1.15x
# - pad: centra el video en 9:16 con aspecto 0.5625
# - xfade: crossfade de 0.5s entre clips
# - amix: mezcla narración y música, prioritario volumen narración
```

---

## ESTRUCTURA DE PRODUCCIÓN AUTÓNOMA

### Paso 1: Guion y Previsualización
- ✅ Guion completo generado con 3 micro-escenas de 8s
- 📝 Cada escena tiene [VISUAL], [MÚSICA], [TIEMPO]
- 📋 Prompts claros para Veo 3.1

### Paso 2: Audio (Chirp 3)
- 🎙️ Generar narración de 24s con Chirp 3
- 🎵 Generar música de fondo de 24s con Lyria 2
- 🎧 Probar mezcla de audio y sincronización

### Paso 3: Video (Veo 3.1)
- 📺 Generar 3 clips de 8s cada uno con Veo 3.1
- 🎨 Usar los prompts exactos de arriba

### Paso 4: Edición (FFmpeg)
- 🔗 Ensamblar clips con crossfade de 0.5s
- 🎯 Aplicar zoompan de 1.15x a cada clip
- 🎹 Balancear volumen audio (narración prioridad, música al 25-30%)

### Paso 5: Validación y Publicación
- ✅ Validar que video dure ~24s
- ✅ Validar sincronización audio-video
- ✅ Probar con vista previa
- 🚀 Publicar en Reels/TikTok

---

## NOTAS DE PRODUCCIÓN

### Tono
- Etereo, emocional, corporativo, sin overwhelmt
- Nacionalmente sensible: mostrar lactancia natural y cómoda
- No explícito, no pornográfico, no explotador
- Siempre con contexto médico-corporativo

### Modelos a usar
- Guion: Gemini 2.5 Pro (aquí está)
- Video: Veo 3.1 (3 clips de 8s)
- Narración: Chirp 3 (María - cálida)
- Música: Lyria 2 (ambient)
- Edición: FFmpeg (crossfade, zoompan)

### Estructura de archivos
```
proyecto/
├── docs/
│   ├── drafts/
│   │   └── lactancia_viaje_invisible_24s.md
│   ├── prompts/
│   └── logs/
├── output/
│   ├── audio/
│   │   ├── narracion_lactancia_24s.wav
│   │   └── musica_ambient_lactancia_24s.mp3
│   ├── clips/
│   │   ├── escena1_8s.mp4
│   │   ├── escena2_8s.mp4
│   │   └── escena3_8s.mp4
│   └── final/
│       └── lactancia_viaje_invisible_24s.mp4
```

---

## FORMATO DE ENTREGA

**Archivo final:** `output/final/lactancia_viaje_invisible_24s.mp4`
**Estado:** GUION COMPLETO GENERADO
**Fecha de creación:** 2026-02-14
**Versión:** v1.0 (24s, 3 micro-escenas)

---

*Guion listo para producción — validar con Claudio antes de generar assets*
