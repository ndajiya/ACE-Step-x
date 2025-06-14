# fireworks_upload.py
from fireworks.client import Fireworks
import os

fw = Fireworks(api_key=os.getenv("FIREWORKS_API_KEY"))

fw.upload_model(
    model_path=".",  # Root directory
    model_name="ace-step-x-agent",
    description="ACE-Step-X: An advanced reasoning agent framework with multi-modal support",
    requirements_path="requirements.txt"
)