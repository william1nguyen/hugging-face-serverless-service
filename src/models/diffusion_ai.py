from .hugging_face import *

class DiffusionAI(HuggingFace):
    
    def transform_to_image(self, response):
        response = self.validate(response, Image.Image)
        image = Image.open(io.BytesIO(response))
        return image

    def display(self, response):
        image = self.transform_to_image(response=response)
        image.show()
