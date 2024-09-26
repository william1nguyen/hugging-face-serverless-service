# Hugging Face Serverless Calling Service

## How to run

* Create `.env` file from `.env.example`.
    ```
    $ cp .env.example .env
    ```

* Setup `miniconda` (optional: `miniforge`, `anaconda`) for running ML projects https://docs.anaconda.com/miniconda/.

* Create conda environment `hugging-face` and activate environment, and install all requirements from `requirements.txt`.
    ```
    $ conda activate hugging-face
    $ conda install -r requirements.txt
    ```

* Start Flask server
    ```
    $ flask run --host localhost --port 8080
    ```

## How to contribute

### Project structure
- `api/`: api blueprints, routers for flask
- `common/`: common config, utilities.
- `models/`: the most important folder, contain hugging face models implementation.
  - `hugging_face.py`: class `HuggingFace` is the parrent class, and others will inherit from this class.
  - Feel free to add more models from hugging face.
