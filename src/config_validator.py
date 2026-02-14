"""
Configuration validator for Vertex AI and project setup.
Ensures all necessary configuration is in place.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional
from utils.logger import logger
from utils.cost_tracker import tracker


class ConfigValidator:
    """Validate configuration for multimedia production."""

    REQUIRED_ENV_VARS = [
        "GOOGLE_CLOUD_PROJECT",
        "GOOGLE_CLOUD_LOCATION"
    ]

    REQUIRED_CONFIG_FILES = [
        "config/project.json"
    ]

    def __init__(self):
        self.config = {}

    def validate(self) -> Dict[str, Any]:
        """
        Validate all configuration.

        Returns:
            Dictionary of config status and errors
        """
        validation_results = {
            "status": "ok",
            "errors": [],
            "warnings": [],
            "project_id": None,
            "region": None
        }

        # Check environment variables
        self._validate_env_vars(validation_results)

        # Check config files
        self._validate_config_files(validation_results)

        # Check for project.json
        self._validate_project_json(validation_results)

        # Validate actual config content
        if self.config:
            self._validate_project_config(validation_results)

        return validation_results

    def _validate_env_vars(self, results: Dict[str, Any]):
        """Validate required environment variables."""
        for env_var in self.REQUIRED_ENV_VARS:
            value = os.getenv(env_var)
            if not value:
                error = f"Missing environment variable: {env_var}"
                results["errors"].append(error)
                logger.error(error)
            else:
                logger.info(f"✓ {env_var}: {value}")

    def _validate_config_files(self, results: Dict[str, Any]):
        """Validate required config files exist."""
        for config_file in self.REQUIRED_CONFIG_FILES:
            path = Path(config_file)
            if not path.exists():
                error = f"Missing config file: {config_file}"
                results["errors"].append(error)
                logger.error(error)
            else:
                logger.info(f"✓ Config file found: {config_file}")

    def _validate_project_json(self, results: Dict[str, Any]):
        """Load and validate project.json."""
        project_path = Path("config/project.json")
        if not project_path.exists():
            return

        try:
            with open(project_path, 'r') as f:
                self.config = json.load(f)

            results["project_id"] = self.config.get("projectId")
            results["region"] = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")

            logger.info(f"✓ Project loaded: {results['project_id']}")

        except json.JSONDecodeError as e:
            error = f"Invalid JSON in project.json: {e}"
            results["errors"].append(error)
            logger.error(error)

    def _validate_project_config(self, results: Dict[str, Any]):
        """Validate project.json content."""
        if not self.config:
            return

        project_id = self.config.get("projectId")

        if not project_id:
            error = "Project ID not found in project.json"
            results["errors"].append(error)
            logger.error(error)

        elif project_id == "YOUR_GCP_PROJECT_ID_HERE":
            error = "Project ID not configured. Update config/project.json"
            results["warnings"].append(error)
            logger.warning(error)

        else:
            # Load cost estimates
            tracker.add("gemini-2.5-pro", tokens=1000)
            tracker.add("veo-3.1", minutes=1)
            logger.info("✓ Cost estimates loaded")

    def print_summary(self, validation_results: Dict[str, Any]):
        """Print validation summary."""
        print("\n" + "="*60)
        print("VALIDACIÓN DE CONFIGURACIÓN")
        print("="*60)

        status = validation_results["status"]
        if status == "ok":
            print("✓ ESTADO: CONFIGURACIÓN VÁLIDA")
            print(f"  Proyecto: {validation_results['project_id']}")
        else:
            print("✗ ESTADO: ERRORES DETECTADOS")
            print(f"  Errores: {len(validation_results['errors'])}")

        if validation_results['warnings']:
            print(f"\n⚠️  Warnings ({len(validation_results['warnings'])}):")
            for warning in validation_results['warnings']:
                print(f"    - {warning}")

        print("="*60 + "\n")


# Singleton instance
config_validator = ConfigValidator()
