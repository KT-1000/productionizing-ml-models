FROM python:3.7-alpine

# Set environment variables
ENV MODEL_NAME {{cookiecutter.project_slug}}

# Add requirements file
COPY ./app/requirements.txt /app/requirements.txt

# Install Dependencies
WORKDIR /app
RUN pip install -r requirements.txt

COPY ./app/app.py /app/app.py
WORKDIR /app

EXPOSE 5000

ENTRYPOINT python ./app/app.py
