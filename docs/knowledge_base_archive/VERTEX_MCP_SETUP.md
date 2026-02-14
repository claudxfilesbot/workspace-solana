# ✅ VERTEX AI MCP - SETUP COMPLETO

**Status:** FUNCIONANDO  
**Fecha:** 2026-02-12  
**MCP Server:** `/mcp-vertex-simple/server.py`  

---

## 🚀 Inicio Rápido

### Usar el MCP Directamente

```bash
# Ver herramientas disponibles
mcporter list --config /home/claudio.alcaman/.openclaw/workspace/config/mcporter.json

# Hacer una llamada
mcporter call --config /home/claudio.alcaman/.openclaw/workspace/config/mcporter.json \
  vertex.generate \
  prompt="¿Cuál es la capital de Francia?" \
  --output json
```

### Desde Python (Directo)

```python
import sys
sys.path.insert(0, '/home/claudio.alcaman/.openclaw/workspace')

from vertex_models import generate

# Usar cualquier modelo Gemini
resultado = generate('vertex/gemini-3-pro-preview', 'Tu prompt aquí')
print(resultado)
```

---

## 📊 Configuración

| Parámetro | Valor |
|-----------|-------|
| **Proyecto** | project-a65bf396-8524-45f7-8d6 |
| **MCP Server** | /mcp-vertex-simple/server.py |
| **MCP Config** | /config/mcporter.json |
| **SDK** | google-genai (Gemini) |
| **Modelos Disponibles** | gemini-3-pro-preview, gemini-2-5-flash |
| **Herramienta Expuesta** | `generate` |

---

## 🔌 Modelos Disponibles

```
✅ vertex/gemini-3-pro-preview (Reasoning, análisis profundo)
✅ vertex/gemini-2-5-flash (Rápido, multimodal)
⚠️  Claude modelos: Sin recursos en el proyecto
```

---

## 📝 Ejemplo de Uso - MCP

```bash
# Test simple
mcporter call --config config/mcporter.json vertex.generate \
  prompt="¿Qué es machine learning?" \
  --output json
```

**Respuesta esperada:**
```json
{
  "server": "vertex",
  "tool": "generate",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Machine learning es una rama de la IA..."
      }
    ]
  }
}
```

---

## 🔐 Credenciales

- **Ubicación:** `.vertex-key.json` (en workspace)
- **Formato:** Service Account JSON
- **Permisos:** Vertex AI User role ✅
- **Autenticación:** GOOGLE_APPLICATION_CREDENTIALS

**⚠️ IMPORTANTE:** 
- No compartir `.vertex-key.json`
- Rotar claves regularmente
- Después de terminar, considerar revocar

---

## 🛠️ Arquitectura

```
OpenClaw
    ↓
mcporter
    ↓
MCP Server (Python)
    ↓
vertex_models.generate()
    ↓
Google Genai SDK
    ↓
Vertex AI API (Gemini)
```

---

## ✨ Features

✅ **Múltiples modelos** - Alterna entre gemini-3-pro-preview y gemini-2.5-flash  
✅ **Caching de clientes** - Reutiliza conexiones  
✅ **Error handling** - Manejo de cuota exhausted (429)  
✅ **MCP compatible** - Funciona con cualquier cliente MCP  
✅ **Production ready** - Credenciales seguras, logging, timeouts  

---

## 🔧 Troubleshooting

### MCP offline
```bash
# Verificar que el servidor se inicia
python3 /mcp-vertex-simple/server.py &
# Debería responder a stdin/stdout
```

### Modelo no encontrado (404)
```bash
# Verificar disponibilidad
mcporter call vertex.generate prompt="test" 2>&1 | grep -i "404\|not found"
# Si 404: Modelo no habilitado en proyecto
```

### Cuota exhausted (429)
```bash
# Esperar 5-30 minutos o usar otro modelo
mcporter call vertex.generate prompt="..." model="vertex/gemini-2-5-flash"
```

---

## 📚 Documentación Relacionada

- `VERTEX_AI_SUMMARY.md` - Resumen ejecutivo
- `VERTEX_AI_RULES.md` - Reglas formales
- `VERTEX_AI_USAGE.md` - Guía de uso
- `VERTEX_AI_REPLICATION_GUIDE.md` - Cómo replicar

---

## ✅ Checklist

```
[✓] MCP Server creado y funcionando
[✓] mcporter configurado
[✓] Credenciales válidas
[✓] Gemini modelos accesibles
[✓] Documentación completa
[✓] Error handling implementado
[✓] Ready para producción
```

---

**MCP Vertex AI está listo para usar.** 🎯

Para usar en OpenClaw o desde Python, consulta la sección "Inicio Rápido" arriba.
