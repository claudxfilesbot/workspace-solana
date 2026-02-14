"""
Script generator for videos using Gemini 2.5 Pro.
Generates scripts with [VISUAL] and [MÚSICA] tags.
"""

from vertex_ai_client import VertexAIClient
from utils.logger import logger
from utils.cost_tracker import tracker


class ScriptGenerator:
    """Generate scripts with structured tags for production."""

    def __init__(self):
        self.client = VertexAIClient()
        logger.info("ScriptGenerator initialized")

    def generate(
        self,
        topic: str,
        duration: int = 30,
        format: str = "cinematic",
        tone: str = "professional"
    ) -> str:
        """
        Generate a script for a video.

        Args:
            topic: Topic or concept for the video
            duration: Duration in seconds
            format: Video format (cinematic, educational, etc.)
            tone: Overall tone

        Returns:
            Generated script with [VISUAL] and [MÚSICA] tags
        """
        logger.info(f"Generating script for: {topic}")

        prompt = f"""
        Crea un guion de {duration} segundos sobre '{topic}'.
        Formato: {format}
        Tono: {tone}

        El formato debe ser:
        1. [VISUAL: Descripción visual detallada]
        2. Diálogo (opcional)
        3. [MÚSICA: Tono y estilo de música]

        Tipos de escenas a incluir:
        - Acto 1: Introducción y setup (10 segundos)
        - Acto 2: Desarrollo y tensión (20 segundos)
        - Acto 3: Conclusión o cliffhanger (10 segundos)

        Produce un script limpio y directo, en español.
        """

        try:
            script = self.client.generate_script(prompt)
            logger.info(f"Script generado exitosamente ({len(script)} caracteres)")
            return script

        except Exception as e:
            logger.error(f"Error generando guion: {e}")
            return self._generate_error_script(topic)

    def _generate_error_script(self, topic: str) -> str:
        """
        Generate an error fallback script.

        Args:
            topic: Original topic

        Returns:
            Error script
        """
        return f"""
        [VISUAL: Scene not generated due to API error. Add visual description here.]

        This script is a placeholder because the generation failed. To proceed:
        1. Check your Vertex AI configuration in config/project.json
        2. Verify you have a valid Google Cloud Project ID
        3. Retry the generation

        The topic was: {topic}
        """


# Singleton instance
script_generator = ScriptGenerator()
