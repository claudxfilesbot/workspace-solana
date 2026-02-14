"""
Video assembler for final production using FFmpeg.
Assembles video, audio, music, and transitions into final output.
"""

import subprocess
from pathlib import Path
from utils.logger import logger
from utils.file_manager import file_manager


class VideoAssembler:
    """Assemble final video with FFmpeg."""

    def __init__(self):
        logger.info("VideoAssembler initialized")

    def assemble(
        self,
        video_files: list,
        audio_files: list,
        music_file: str,
        output_filename: str = "output_final.mp4",
        output_dir: str = "output/final"
    ) -> str:
        """
        Assemble all video elements into final output.

        Args:
            video_files: List of video clip paths
            audio_files: List of audio files (dialogue, voiceover)
            music_file: Path to background music file
            output_filename: Name of final output file
            output_dir: Directory to save final output

        Returns:
            Path to assembled video
        """
        logger.info("Starting video assembly...")
        logger.info(f"  - Clips: {len(video_files)}")
        logger.info(f"  - Audio: {len(audio_files)}")
        logger.info(f"  - Music: {music_file}")

        # Create output path
        output_path = file_manager.get_path(output_dir, output_filename)

        # FFmpeg command construction
        # This is a template - real command will be user's specific one
        cmd = [
            "ffmpeg",
            "-i", "input_video.mp4",  # Placeholder - would be concatenated clips
            "-i", "input_audio.mp3",   # Placeholder - would be all audio merged
            "-i", music_file,
            "-c:v", "libx264",
            "-c:a", "aac",
            "-preset", "medium",
            "-crf", "23",
            output_path
        ]

        try:
            logger.info(f"Running FFmpeg command...")
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            logger.info(f"✓ Video assembled: {output_path}")
            return str(output_path)

        except subprocess.CalledProcessError as e:
            logger.error(f"FFmpeg error: {e.stderr}")
            raise
        except FileNotFoundError:
            logger.error("FFmpeg not found in PATH")
            raise

    def concatenate_clips(self, clip_paths: list, output_file: str) -> str:
        """
        Concatenate multiple video clips into one.

        Args:
            clip_paths: List of clip file paths
            output_file: Output filename for concatenated video

        Returns:
            Path to concatenated video
        """
        logger.info(f"Concatenating {len(clip_paths)} clips...")

        # Create temporary concat file
        concat_file = Path("temp_concat.txt")
        with open(concat_file, 'w') as f:
            for clip in clip_paths:
                f.write(f"file '{clip}'\n")

        try:
            cmd = [
                "ffmpeg",
                "-f", "concat",
                "-safe", "0",
                "-i", str(concat_file),
                "-c", "copy",
                output_file
            ]

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            logger.info(f"✓ Clips concatenated: {output_file}")
            return output_file

        except subprocess.CalledProcessError as e:
            logger.error(f"FFmpeg error: {e.stderr}")
            raise
        finally:
            # Clean up temp file
            if concat_file.exists():
                concat_file.unlink()


# Singleton instance
video_assembler = VideoAssembler()
