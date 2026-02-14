import os
import requests
import time
import json
import subprocess
from google.auth import default
from google.auth.transport.requests import Request

# Asegurar entorno
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/claudio.alcaman/.openclaw/workspace/vertex-express-key.json"

def generar_video_veo(prompt):
    credentials, project_id = default(scopes=['https://www.googleapis.com/auth/cloud-platform'])
    credentials.refresh(Request())
    PROJECT_ID = project_id or "project-a65bf396-8524-45f7-8d6"
    LOCATION = "us-central1"
    url = (f"https://{LOCATION}-aiplatform.googleapis.com/v1/"
           f"projects/{PROJECT_ID}/locations/{LOCATION}/"
           f"publishers/google/models/veo-3.1-generate-001:predictLongRunning")
    headers = {
        "Authorization": f"Bearer {credentials.token}",
        "Content-Type": "application/json"
    }
    payload = {
        "instances": [{"prompt": prompt}],
        "parameters": {"sampleCount": 1}
    }
    print(f"🎬 [API] Enviando petición auditada de video...")
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        return {"success": True, "operation_name": result.get("name", "")}
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
        return {"success": False}

def verificar_operacion(operation_name):
    credentials, _ = default(scopes=['https://www.googleapis.com/auth/cloud-platform'])
    credentials.refresh(Request())
    url = f"https://us-central1-aiplatform.googleapis.com/v1/{operation_name}"
    headers = {"Authorization": f"Bearer {credentials.token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else {"error": response.text}

def descargar_video(gcs_uri, destino_local):
    print(f"📦 Moviendo video desde Google Temporal a tu bucket...")
    cmd = f"gsutil cp {gcs_uri} gs://viedos-2026ai-us/output/clips/NEURAL_CODE_FINAL/video_final_veo.mp4"
    subprocess.run(cmd, shell=True, check=True)
    cmd_local = f"gsutil cp {gcs_uri} {destino_local}"
    subprocess.run(cmd_local, shell=True, check=True)
    print(f"✅ Proceso de descarga completado.")

if __name__ == "__main__":
    prompt = "A futuristic cyberpunk city at night with bright neon lights, digital rain with python code snippets, cinematic 4k quality, dramatic atmosphere"
    resultado = generar_video_veo(prompt)
    if resultado["success"]:
        op_name = resultado["operation_name"]
        print(f"⏳ Esperando renderizado... (Operación: {op_name})")
        for i in range(40): # Aumentamos a 40 intentos por seguridad
            time.sleep(30)
            status = verificar_operacion(op_name)
            if status.get("done"):
                print("🎉 ¡GOOGLE TERMINÓ EL RENDER!")
                try:
                    video_uri = status.get("response", {}).get("predictions", [{}])[0].get("gcsUri")
                    if video_uri:
                        print(f"📹 URI detectada: {video_uri}")
                        descargar_video(video_uri, "output/final/video_crudo.mp4")
                        print("🎬 Video listo para ensamble final.")
                    else:
                        print("⚠️ No se encontró la URI en la respuesta. Revisando estructura...")
                        print(json.dumps(status, indent=2))
                except Exception as e:
                    print(f"⚠️ Error extrayendo video: {e}")
                break
            else:
                print(f"[{i+1}/40] Renderizando neones... (Status: RUNNING)")
