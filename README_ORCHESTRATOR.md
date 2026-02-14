Orquestador de Producción Multimedia - V1.0

Descripción
-----------
Sistema centralizado que orquesta todas las funciones del módulo `src/` para facilitar la producción multimedia.

Componentes Principales
-----------------------

1. **ProductionOrchestrator** (`src/orchestrator.py`)
   - Orquestador principal de workflow completo
   - Coordinación de todas las fases de producción
   - Validación de configuración

2. **Main CLI** (`src/main.py`)
   - Interfaz de línea de comandos para producción
   - Parámetros: --topic, --duration, --quick

3. **Simple Wrapper** (`src/simple_orchestrator.py`)
   - Wrapper simple para testing
   - Integración rápida con los módulos existentes

Módulos Coordinados
-------------------

- `script_generator.py`: Generación de guiones con Gemini 2.5 Pro
- `asset_generator.py`: Producción de assets multimedia
- `video_assembler.py`: Ensamblaje final con FFmpeg
- `config_validator.py`: Validación de configuración
- `utils/`: Logger, Cost Tracker, File Manager

Workflow Completo
------------------

1. **Validación**: Verificar configuración con config_validator
2. **Guión**: Generar script con script_generator
3. **Assets**: Producir audio y music con asset_generator
4. **Video**: Ensamblar con video_assembler

Uso
---

```bash
python3 src/main.py --topic "Tema del video" --duration 60
python3 src/simple_orchestrator.py
```

Objetivo
--------

Estructura modular y mantenible que permite:
- Replicación fácil
- Evitar duplicación de código
- Integración simple con herramientas existentes
- Testing individual de cada componente

Estándar de Producción: 24 segundos (3x8 segundos)