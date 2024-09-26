import io
import requests
from PIL import Image

class HuggingFace(object):
    def __init__(self, API_URL, token) -> None:
        self.API_URL = API_URL
        self.token = token

    def validate(self, response, type):
        try:
            image = Image.open(io.BytesIO(response))
            image.verify()
            if not type == Image.Image:
                raise TypeError(f"Response is not match type {type}")
        except:
            if not type == str:
                raise TypeError(f"Response is not match type {type}")

        return response

    def query(self, message):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        payload = {
            "inputs": message,
        }

        try:
            response = requests.post(self.API_URL, headers=headers, json=payload)
            return response.content
        except:
            return "Failed to query hugging face models"
