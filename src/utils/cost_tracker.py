"""Cost tracking utility for API usage."""

import time
from pathlib import Path
from typing import Dict
from collections import defaultdict


class CostTracker:
    """
    Track and display costs for different Vertex AI models.
    """

    # Price estimates per 1000 tokens (approximate)
    MODEL_COSTS: Dict[str, float] = {
        "gemini-2.5-pro": 0.00125,      # USD
        "gemini-2.5-flash": 0.00005,   # USD
        "imagen-4": 0.00250,            # USD per image
        "veo-3.1": 0.01000,             # USD per minute
        "chirp-3": 0.00100,             # USD per audio unit
        "lyria-2": 0.00350,             # USD per audio unit
    }

    def __init__(self):
        self.costs = defaultdict(float)
        self.timestamp = time.time()

    def add(self, model: str, tokens: int = 0, minutes: float = 0, count: int = 0):
        """
        Add cost for a model usage.

        Args:
            model: Name of the model
            tokens: Number of tokens (for text generation)
            minutes: Duration in minutes (for video generation)
            count: Number of items (for image/audio generation)
        """
        price = self.MODEL_COSTS.get(model, 0)
        total_cost = 0

        if tokens > 0:
            cost_per_1000 = price
            total_cost = (tokens / 1000) * cost_per_1000

        if minutes > 0:
            cost_per_minute = price
            total_cost = minutes * cost_per_minute

        if count > 0:
            # Estimate based on rough usage
            total_cost = count * price

        self.costs[model] += total_cost
        return total_cost

    def print_summary(self):
        """Print a summary of all tracked costs."""
        print("\n" + "="*50)
        print("RESUMEN DE COSTOS - Producción Multimedia")
        print("="*50)
        print(f"Tiempo: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.timestamp))}")
        print("-"*50)

        if not self.costs:
            print("Sin costos registrados")
        else:
            for model, cost in sorted(self.costs.items()):
                print(f"{model:30s} {cost:8.4f} USD")
            print("-"*50)

            total = sum(self.costs.values())
            print(f"{'TOTAL'.:30s} {total:8.4f} USD")

        print("="*50 + "\n")


tracker = CostTracker()
