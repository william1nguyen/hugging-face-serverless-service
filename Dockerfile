FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml

# Activate the environment, and make sure it's activated:
RUN conda init
ENV CONDA_DEFAULT_ENV=hugging-face
ENV PATH /opt/conda/envs/hugging-face/bin:$PATH
RUN /bin/bash -c "source activate hugging-face"

# The code to run when container is started
COPY . .

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "-w", "3", "-k", "gevent", "--timeout", "120", "--keep-alive", "10"]
