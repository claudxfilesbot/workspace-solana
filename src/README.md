# src/ - Scripts y Herramientas Personalizadas

## Propósito

Directorio para scripts y herramientas personalizadas que soportan el flujo de producción con Vertex AI.

## Estructura

```
src/
├── vertex_ai_client.py      # Cliente base para Vertex AI APIs
├── script_generator.py      # Generador de guiones con Gemini
├── asset_generator.py       # Generador de assets (video, imágenes, voz, música)
├── video_assembler.py      # Ensamblador final con FFmpeg
├── config_validator.py     # Validador de configuración
└── utils/                   # Utilidades compartidas
    ├── logger.py
    ├── cost_tracker.py
    └── file_manager.py
```

## Scripts Individuales

### vertex_ai_client.py
Cliente base para todos los modelos de Vertex AI. Necesita integración real con MCP Vertex que ya existe en el sistema.

### script_generator.py
Usa Gemini 2.5 Pro para generar guiones completos con [VISUAL] y [MÚSICA] tags.

### asset_generator.py
Orquesta la generación de todos los assets:
1. Narración con Chirp 3
2. Imágenes con Imagen 4
3. Video con Veo 3.1
4. Música con Lyria 2

### video_assembler.py
Usa FFmpeg para ensamblar:
- Video base
- Narración de voz
- Música de fondo
- Subtítulos
- Transiciones

## Próximos Pasos

1. **Integrar MCP Vertex**: Ya existe MCP-Vertex en el sistema, conectar client.py con él
2. **Implementar sincronización**: Usar llaves MCP-Vertex y llaves MCP-Vertex-simple
3. **Agregar tests**: Unit tests para cada script
4. **Documentar API endpoints**: Crear docs/api/ con endpoints de cada modelo

## Dependencias

- Google Cloud SDK
- MCP Vertex (ya instalado en el sistema)
- FFmpeg (ya instalado)

---

*Última actualización: 2026-02-13*
