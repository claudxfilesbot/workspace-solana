# test_vertex.py
from vertex_ai_client import VertexAIClient

client = VertexAIClient()
config = client.get_config()
print(f"Project: {config['project_id']}")
print(f"Model: {config['default_model']}")

# Test if SDK is loaded
try:
    from vertexai.generative_models import GenerativeModel
    print("\n✓ SDK loaded successfully!")
    model = GenerativeModel(config['default_model'])
    response = model.generate_content("Test prompt")
    print(f"✓ Generated: {response.text[:100]}")
except Exception as e:
    print(f"✗ Error: {e}")
