"""File management utilities for organizing production outputs."""

import os
import shutil
from pathlib import Path
from typing import List, Optional
from .logger import logger


class FileManager:
    """Handle file operations for organized production outputs."""

    def __init__(self, base_dir: str = "output"):
        """
        Initialize file manager.

        Args:
            base_dir: Base directory for all outputs
        """
        self.base_dir = Path(base_dir)
        self._create_structure()

    def _create_structure(self):
        """Create the standard output directory structure."""
        # Create base structure
        self.base_dir.mkdir(parents=True, exist_ok=True)

        # Create subdirectories
        for subdir in ["audio", "music", "assets/images", "assets/video", "clips", "final"]:
            (self.base_dir / subdir).mkdir(parents=True, exist_ok=True)

        logger.info("File manager structure created")

    def get_path(self, *relative_path: str) -> Path:
        """
        Get a full path to a file in the output directory.

        Args:
            *relative_path: Path components relative to output/

        Returns:
            Full Path object
        """
        return self.base_dir.joinpath(*relative_path)

    def copy_source(self, source_path: str, target_dir: str, filename: Optional[str] = None) -> Path:
        """
        Copy a file to the appropriate output directory.

        Args:
            source_path: Path to source file
            target_dir: Target subdirectory (audio, music, clips, etc.)
            filename: Custom filename (uses original if not provided)

        Returns:
            Path to copied file
        """
        source = Path(source_path)
        if not source.exists():
            logger.error(f"Source file not found: {source_path}")
            return None

        if filename is None:
            filename = source.name

        target = self.get_path(target_dir, filename)

        shutil.copy2(source, target)
        logger.info(f"Copiado: {source_path} -> {target}")
        return target

    def ensure_dir(self, *relative_path: str):
        """
        Ensure a directory exists.

        Args:
            *relative_path: Path components
        """
        dir_path = self.base_dir.joinpath(*relative_path)
        dir_path.mkdir(parents=True, exist_ok=True)

    def clean_outputs(self, dry_run: bool = False):
        """
        Clean output directories (optional for testing).

        Args:
            dry_run: Print what would be deleted without deleting
        """
        dirs_to_clean = [
            "clips",
            "final",
            "assets/images"
        ]

        print("\nDirectorios a limpiar:")
        for d in dirs_to_clean:
            dir_path = self.base_dir / d
            if dir_path.exists():
                file_count = sum(1 for _ in dir_path.rglob("*") if _.is_file())
                print(f"  - {d}/ ({file_count} archivos)")

        if not dry_run:
            for d in dirs_to_clean:
                dir_path = self.base_dir / d
                if dir_path.exists():
                    shutil.rmtree(dir_path)
                    logger.info(f"Limpiado: {dir_path}")


file_manager = FileManager()
