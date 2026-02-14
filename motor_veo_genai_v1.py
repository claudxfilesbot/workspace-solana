import os
import time
from google import genai
from google.genai.types import GenerateVideosConfig

# Configuración confirmada por Claudio
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/claudio.alcaman/.openclaw/workspace/vertex-express-key.json"
PROJECT_ID = "project-a65bf396-8524-45f7-8d6"
LOCATION = "us-central1"
DEFAULT_OUTPUT_BUCKET = "gs://viedos-2026ai-us/output/veo/"

def generar_video_veo_para_agente(prompt, output_bucket=DEFAULT_OUTPUT_BUCKET, timeout_minutos=15):
    start_time = time.time()
    try:
        client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)
        
        print(f"📡 [VEO 3.1] Enviando petición con código auditado...")
        operation = client.models.generate_videos(
            model="veo-3.1-generate-001",
            prompt=prompt,
            config=GenerateVideosConfig(
                aspect_ratio="16:9",
                output_gcs_uri=output_bucket,
            ),
        )

        max_checks = (timeout_minutos * 60) // 20
        check_count = 0
        while not operation.done and check_count < max_checks:
            check_count += 1
            print(f"⏳ Renderizando... Intento {check_count}/{max_checks} (20s)")
            time.sleep(20)
            operation = client.operations.get(operation)

        if operation.result and operation.result.generated_videos:
            video_uri = operation.result.generated_videos[0].video.uri
            print(f"✅ ¡EXITO TOTAL! Video en: {video_uri}")
            return {"success": True, "video_uri": video_uri}
        else:
            print("❌ Error: No se encontró video en la respuesta.")
            return {"success": False}
            
    except Exception as e:
        print(f"❌ Error en el proceso: {e}")
        return {"success": False}

if __name__ == "__main__":
    PROMPT = "A futuristic cyberpunk programmer's hands typing on a holographic keyboard, cinematic dolly-in shot, neon reflections, 4k quality, dramatic lighting"
    generar_video_veo_para_agente(PROMPT)
