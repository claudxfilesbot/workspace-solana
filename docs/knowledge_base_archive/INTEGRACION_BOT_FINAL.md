# 🤖 Integración Final - Bot Autónomo de Videos Veo

## 📦 Archivos del Sistema

### 1. Script Principal (FUNCIONA - evita bug de Veo)
**`veo_sin_verificacion.py`** ✅
- Genera videos con Veo 3.1
- Busca en el bucket (evita el bug de verificación)
- Descarga automáticamente cuando encuentra el video

### 2. Bug Conocido de Veo
La API de Veo tiene un bug:
- Devuelve UUID como operation_id
- Pero requiere Long (número) para verificar
- Error: "The Operation ID must be a Long"

**Solución:** No verificar con operation_id, sino buscar en el bucket.

---

## 🚀 Integración en Bot de Telegram

### Código Completo del Bot
```python
# bot_neural_code_final.py

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import subprocess
import json
import time
import asyncio
from pathlib import Path

class NeuralCodeVideoBot:
    def __init__(self):
        self.pending_file = Path("videos_pendientes.json")
        self.pending = self._load()
    
    def _load(self):
        if self.pending_file.exists():
            return json.loads(self.pending_file.read_text())
        return {}
    
    def _save(self):
        self.pending_file.write_text(json.dumps(self.pending, indent=2))
    
    async def cmd_generar(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /generar <prompt>"""
        
        if not context.args:
            await update.message.reply_text(
                "🎬 Uso: /generar <descripción>\n\n"
                "Ejemplos:\n"
                "• /generar intro\n"
                "• /generar city\n"
                "• /generar cyberpunk city at night"
            )
            return
        
        prompt = " ".join(context.args)
        user_id = update.effective_user.id
        chat_id = update.effective_chat.id
        
        # Escenas pre-definidas
        SCENES = {
            "intro": "cinematic shot of programmer hands typing on keyboard with holographic code, blue neon lighting, cyberpunk aesthetic, 4k",
            "city": "futuristic cyberpunk city at night with neon signs, aerial drone shot, rain reflections, cinematic",
            "code_rain": "matrix-style digital rain with python code snippets, neon green, smooth animation, 4k",
            "neural": "abstract neural network with glowing nodes and connections, blue and orange colors, cinematic"
        }
        
        if prompt in SCENES:
            scene_name = prompt
            prompt = SCENES[prompt]
            await update.message.reply_text(f"🎬 Usando escena: {scene_name}")
        
        await update.message.reply_text(
            f"🎬 Generando video...\n"
            f"📝 {prompt[:100]}...\n\n"
            f"⏱️ Esto tomará 10-15 minutos.\n"
            f"Te avisaré cuando esté listo. 🚀"
        )
        
        # Generar video
        result = subprocess.run(
            ["python3", "veo_sin_verificacion.py", prompt],
            capture_output=True,
            text=True
        )
        
        # Extraer timestamp del output
        for line in result.stdout.split('\n'):
            if 'Timestamp:' in line:
                timestamp = int(line.split(':')[1].strip())
                
                # Guardar en pendientes
                self.pending[str(timestamp)] = {
                    "user_id": user_id,
                    "chat_id": chat_id,
                    "prompt": prompt,
                    "timestamp": timestamp
                }
                self._save()
                
                await update.message.reply_text(
                    f"✅ Video en cola!\n"
                    f"📋 ID: {timestamp}"
                )
                break
    
    async def verificar_videos_loop(self, app: Application):
        """Loop que busca videos completados cada 2 minutos"""
        
        while True:
            try:
                for timestamp, data in list(self.pending.items()):
                    
                    # Verificar si ya pasaron 15 minutos
                    elapsed = time.time() - data["timestamp"]
                    
                    if elapsed > 900:  # 15 minutos
                        
                        # Buscar video en el bucket
                        result = subprocess.run(
                            ["gsutil", "ls", "-l", "gs://viedos-2026ai-us/output/clips/VEO_REST_FINAL/"],
                            capture_output=True,
                            text=True
                        )
                        
                        # Buscar el más reciente
                        lines = [l for l in result.stdout.split('\n') if '.mp4' in l]
                        
                        if lines:
                            # Obtener URI del último video
                            video_uri = lines[-1].split()[-1]
                            
                            # Descargar
                            video_file = f"video_{timestamp}.mp4"
                            subprocess.run(
                                ["gsutil", "cp", video_uri, video_file],
                                capture_output=True
                            )
                            
                            # Enviar al usuario
                            with open(video_file, 'rb') as video:
                                await app.bot.send_video(
                                    chat_id=data["chat_id"],
                                    video=video,
                                    caption=(
                                        f"🎉 ¡Tu video de Neural Code está listo!\n\n"
                                        f"📝 {data['prompt'][:100]}"
                                    )
                                )
                            
                            # Limpiar
                            Path(video_file).unlink()
                            del self.pending[timestamp]
                            self._save()
                            
                            print(f"✅ Video enviado a {data['user_id']}")
            
            except Exception as e:
                print(f"❌ Error en loop: {e}")
            
            # Verificar cada 2 minutos
            await asyncio.sleep(120)

def main():
    # Tu token de Telegram
    TOKEN = "TU_TOKEN_AQUI"
    
    bot = NeuralCodeVideoBot()
    app = Application.builder().token(TOKEN).build()
    
    # Comandos
    app.add_handler(CommandHandler("generar", bot.cmd_generar))
    app.add_handler(CommandHandler("start", lambda u, c: u.message.reply_text(
        "🤖 Bot de Neural Code\n\n"
        "Comandos:\n"
        "/generar <prompt> - Genera un video con IA\n\n"
        "Escenas pre-definidas:\n"
        "• intro - Programador tecleando\n"
        "• city - Ciudad cyberpunk\n"
        "• code_rain - Lluvia de código\n"
        "• neural - Red neuronal"
    )))
    
    # Iniciar loop de verificación
    asyncio.create_task(bot.verificar_videos_loop(app))
    
    print("🤖 Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
```

---

## 📋 Archivos Necesarios
```
proyecto/
├── veo_sin_verificacion.py          # Script que genera videos
├── bot_neural_code_final.py         # Bot de Telegram
├── videos_pendientes.json           # DB de videos en proceso (auto-generado)
└── video_request_*.json             # Registros de peticiones
```

---

## 🔧 Setup
```bash
# 1. Instalar dependencias
pip install python-telegram-bot requests google-auth

# 2. Configurar token del bot
# Editar bot_neural_code_final.py línea 115

# 3. Ejecutar bot
python3 bot_neural_code_final.py
```

---

## ✅ Flujo Completo

1. Usuario: `/generar cyberpunk city`
2. Bot: Ejecuta `veo_sin_verificacion.py`
3. Bot: "✅ Video en cola. Te aviso en 15 min"
4. Script genera video en Veo (en background)
5. Loop del bot verifica cada 2 minutos
6. Después de 15 min, busca en el bucket
7. Encuentra el video → descarga → envía al usuario
8. Usuario recibe: "🎉 ¡Tu video está listo!" + video.mp4

**¡Completamente autónomo!** ✅

