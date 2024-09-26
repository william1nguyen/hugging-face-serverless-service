import os
from dotenv import load_dotenv

load_dotenv()

class AppConfig(object):

    HUGGING_FACE_DIFFUSION_API_URL = os.getenv("HUGGING_FACE_DIFFUSION_API_URL")
    HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")
