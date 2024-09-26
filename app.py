from flask import Flask

from src.api.diffusion_ai.router import diffusion_blueprint

app = Flask(__name__)

app.register_blueprint(diffusion_blueprint)

if __name__ == "__main__":
	app.run(host='localhost', port=8080, debug=True)
