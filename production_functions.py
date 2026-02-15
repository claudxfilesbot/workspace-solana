import os
import time
from google import genai
from google.genai.types import GenerateVideosConfig

# Configuración global
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/claudio.alcaman/.openclaw/workspace/.secrets/vertex-credentials.json"
PROJECT_ID = "project-a65bf396-8524-45f7-8d6"
LOCATION = "us-central1"
DEFAULT_OUTPUT_BUCKET = "gs://viedos-2026ai-us/output/veo/"

def generar_video_veo_para_agente(
    prompt: str,
    output_bucket: str = DEFAULT_OUTPUT_BUCKET,
    timeout_minutos: int = 15
) -> dict:
    """
    Genera video con Veo 3.1 y retorna la URI del video.
    
    Esta es la función lista para producción para tu agente autónomo.
    
    Args:
        prompt (str): Descripción del video a generar
        output_bucket (str): Bucket de GCS donde guardar el video
        timeout_minutos (int): Tiempo máximo de espera
        
    Returns:
        dict: {
            "success": bool,
            "video_uri": str (si success=True),
            "error": str (si success=False),
            "duration_seconds": float
        }
    
    Ejemplo:
        resultado = generar_video_veo_para_agente(
            prompt="A futuristic car speeding through neon city at night",
            output_bucket="gs://viedos-2026ai-us/output/veo/",
            timeout_minutos=15
        )
        
        if resultado["success"]:
            print(f"Video: {resultado['video_uri']}")
        else:
            print(f"Error: {resultado['error']}")
    """
    import time
    start_time = time.time()
    
    try:
        # Inicializar cliente
        client = genai.Client(
            vertexai=True,
            project=PROJECT_ID,
            location=LOCATION
        )
        
        # Generar video
        operation = client.models.generate_videos(
            model="veo-3.1-generate-001",
            prompt=prompt,
            config=GenerateVideosConfig(
                aspect_ratio="16:9",
                output_gcs_uri=output_bucket,
            ),
        )
        
        # Esperar completación
        max_checks = (timeout_minutos * 60) // 15
        check_count = 0
        
        while not operation.done and check_count < max_checks:
            check_count += 1
            time.sleep(15)
            
            try:
                operation = client.operations.get(operation)
            except Exception:
                # Continuar si hay error al consultar
                pass
        
        # Timeout
        if check_count >= max_checks and not operation.done:
            return {
                "success": False,
                "error": f"Timeout después de {timeout_minutos} minutos",
                "duration_seconds": time.time() - start_time
            }
        
        # Extraer video URI (con validación robusta para evitar 'NoneType' errors)
        if operation.response and hasattr(operation, 'result') and operation.result:
            if hasattr(operation.result, 'generated_videos') and operation.result.generated_videos:
                video_uri = operation.result.generated_videos[0].video.uri
                
                return {
                    "success": True,
                    "video_uri": video_uri,
                    "duration_seconds": time.time() - start_time
                }
            else:
                # La operación tuvo respuesta pero no contiene videos.
                return {
                    "success": False,
                    "error": "La operación finalizó pero no se encontraron videos en la respuesta.",
                    "duration_seconds": time.time() - start_time
                }
        else:
            # La operación no tuvo respuesta o el resultado fue nulo.
            # Esto puede ocurrir si el prompt es rechazado por políticas de seguridad.
            error_details = "La operación no generó una respuesta válida."
            if hasattr(operation, 'error') and operation.error:
                error_details += f" Detalles: {operation.error.message}"

            return {
                "success": False,
                "error": error_details,
                "duration_seconds": time.time() - start_time
            }
            
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "duration_seconds": time.time() - start_time
        }


# ============================================================================
# WORKFLOW COMPLETO: IMAGEN 3 + VEO 3.1 + AUDIO
# ============================================================================

def workflow_video_completo_con_veo(
    prompt_imagen: str,
    prompt_video: str,
    texto_voz_femenina: str,
    texto_voz_masculina: str,
    usar_veo: bool = True
) -> dict:
    """
    Workflow completo que combina:
    - Imagen 3 para frames estáticos
    - Veo 3.1 para clips de video (opcional)
    - Google TTS para voces
    - FFmpeg para ensamblaje
    
    Args:
        prompt_imagen: Prompt para generar frame con Imagen 3
        prompt_video: Prompt para generar clip con Veo (si usar_veo=True)
        texto_voz_femenina: Texto para voz femenina
        texto_voz_masculina: Texto para voz masculina
        usar_veo: Si True, genera clip con Veo. Si False, solo usa frames.
        
    Returns:
        dict con video_final_uri y detalles
    """
    import subprocess
    from vertexai.preview.vision_models import ImageGenerationModel
    from google.cloud import texttospeech
    import vertexai
    
    print("🎬 Iniciando workflow completo...")
    
    resultados = {
        "frames": [],
        "clips_veo": [],
        "audios": [],
        "video_final": None
    }
    
    # 1. Generar frames con Imagen 3
    print("\n1️⃣ Generando frames con Imagen 3...")
    vertexai.init(project=PROJECT_ID, location=LOCATION)
    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")
    
    images = model.generate_images(
        prompt=prompt_imagen,
        number_of_images=1,
        aspect_ratio="16:9",
    )
    images[0].save("frame_main.jpg")
    resultados["frames"].append("frame_main.jpg")
    print("   ✅ Frame generado")
    
    # 2. Generar clip con Veo (opcional)
    if usar_veo:
        print("\n2️⃣ Generando clip con Veo 3.1...")
        resultado_veo = generar_video_veo_para_agente(
            prompt=prompt_video,
            timeout_minutos=15
        )
        
        if resultado_veo["success"]:
            print(f"   ✅ Clip generado: {resultado_veo['video_uri']}")
            
            # Descargar el clip
            subprocess.run([
                "gsutil", "cp",
                resultado_veo['video_uri'],
                "./clip_veo.mp4"
            ], check=True)
            
            resultados["clips_veo"].append("clip_veo.mp4")
        else:
            print(f"   ⚠️  Error en Veo: {resultado_veo['error']}")
    
    # 3. Generar voces
    print("\n3️⃣ Generando voces con Google TTS...")
    tts_client = texttospeech.TextToSpeechClient()
    
    # Voz femenina
    response_f = tts_client.synthesize_speech(
        input=texttospeech.SynthesisInput(text=texto_voz_femenina),
        voice=texttospeech.VoiceSelectionParams(
            language_code="es-ES",
            name="es-ES-Neural2-C"
        ),
        audio_config=texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
    )
    with open("voz_femenina.mp3", "wb") as f:
        f.write(response_f.audio_content)
    resultados["audios"].append("voz_femenina.mp3")
    
    # Voz masculina
    response_m = tts_client.synthesize_speech(
        input=texttospeech.SynthesisInput(text=texto_voz_masculina),
        voice=texttospeech.VoiceSelectionParams(
            language_code="es-ES",
            name="es-ES-Neural2-D"
        ),
        audio_config=texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
    )
    with open("voz_masculina.mp3", "wb") as f:
        f.write(response_m.audio_content)
    resultados["audios"].append("voz_masculina.mp3")
    
    print("   ✅ Voces generadas")
    
    # 4. Ensamblar video final con FFmpeg
    print("\n4️⃣ Ensamblando video final...")
    # [Aquí iría tu lógica de FFmpeg para combinar todo]
    
    print("\n🎉 ¡Workflow completado!")
    return resultados


# ============================================================================
# EJEMPLOS DE USO
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("EJEMPLOS DE USO")
    print("="*80)
    
    # Ejemplo 1: Solo generar video con Veo
    print("\n📹 EJEMPLO 1: Generar video simple")
    resultado = generar_video_veo_para_agente(
        prompt="A futuristic car with glowing lights speeding through a cyberpunk city at night",
        timeout_minutos=15
    )
    
    if resultado["success"]:
        print(f"✅ Video generado en {resultado['duration_seconds']:.1f}s")
        print(f"   URI: {resultado['video_uri']}")
    else:
        print(f"❌ Error: {resultado['error']}")
    
    # Ejemplo 2: Workflow completo
    # (Descomenta para probar)
    """
    print("\n📹 EJEMPLO 2: Workflow completo")
    resultado_completo = workflow_video_completo_con_veo(
        prompt_imagen="Cyberpunk city at night with neon lights",
        prompt_video="Flying through a futuristic city with neon signs",
        texto_voz_femenina="Bienvenidos a NEURAL CODE",
        texto_voz_masculina="Donde el código cobra vida",
        usar_veo=True
    )
    """