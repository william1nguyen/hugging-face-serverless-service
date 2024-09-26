import io
from PIL import Image
from flask import Blueprint
from src.models import diffusion_model
from flask import send_file
from flask import request

diffusion_blueprint = Blueprint("diffusion", __name__, url_prefix="/diffusion")


@diffusion_blueprint.route("/image", methods=["POST"])
def generategene_image():
    prompt = request.json.get("prompt")

    response = diffusion_model.query(message=prompt)
    response = diffusion_model.validate(response, Image.Image)

    image = diffusion_model.transform_to_image(response=response)

    image_io = io.BytesIO()
    image.save(image_io, 'JPEG')
    image_io.seek(0)

    return send_file(image_io, download_name='image.jpg', mimetype='image/jpeg', as_attachment=False)
