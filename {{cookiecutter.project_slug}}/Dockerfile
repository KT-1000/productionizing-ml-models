FROM python:3.7-alpine

ENV TRANSFORMATION_NAME {{cookiecutter.project_slug}}

# Add requirements file
COPY ./app/requirements.txt /app/app/requirements.txt

# Install Dependencies
WORKDIR /app/app
RUN pip install -r requirements.txt

# Download nltk corpora
RUN python -m nltk.downloader stopwords

COPY ./app /app
WORKDIR /app

CMD ["python", "transformation.py"]
