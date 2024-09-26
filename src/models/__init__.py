from ..common.config import AppConfig

from .diffusion_ai import DiffusionAI

diffusion_model = DiffusionAI(
    API_URL=AppConfig.HUGGING_FACE_DIFFUSION_API_URL,
    token=AppConfig.HUGGING_FACE_TOKEN
)
