# Hugging Face Serverless Calling Service

## How to run

### Local

* Create `.env` file from `.env.example`.
    ```
    $ cp .env.example .env
    ```

* Setup `miniconda` (optional: `miniforge`, `anaconda`) for running ML projects https://docs.anaconda.com/miniconda/.

* Create conda environment `hugging-face` from `environment.yml` and activate the environment.
    ```
    $ conda env create -f environment.yml
    $ conda activate hugging-face
    ```

* Start Flask server
  * Local
    ```
    $ flask run --host localhost --port 8080
    ```
  * Production
    ```
    $ gunicorn -b 0.0.0.0:5000 app:app -w 3 -k gevent --timeout 120 --keep-alive 10
    ```

### Docker
```
$ docker build -t hugging-face .
$ docker run -it -p 5000:5000 hugging-face
```

## How to contribute

### Project structure
- `api/`: api blueprints, routers for flask
- `common/`: common config, utilities.
- `models/`: the most important folder, contain hugging face models implementation.
  - `hugging_face.py`: class `HuggingFace` is the parrent class, and others will inherit from this class.
  - Feel free to add more models from hugging face.
