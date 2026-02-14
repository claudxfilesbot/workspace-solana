Orchestrator para la producci\u00f3n multimedia.

Funciones:
- check_setup: valida configuraci\u00f3n
- produce: workflow completo desde gui\u00f3n hasta video
- generate_script: genera gui\u00f3n con Gemini
- generate_assets: genera audio y music placeholders
- assemble_video: ensambla con FFmpeg

Dependencias:
- src/vertex_ai_client.py
- src/script_generator.py
- src/asset_generator.py
- src/video_assembler.py

Uso:
    from simple_orchestrator import ProductionOrchestrator
    orchestrator = ProductionOrchestrator()
    result = orchestrator.quick_test()