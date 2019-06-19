FROM python:3.7-alpine

# Set environment variables
ENV MODEL_NAME {{cookiecutter.project_slug}}

# Install Dependencies
COPY ./app/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Get Flask app
COPY ./app/app.py /app/app.py
WORKDIR /app

EXPOSE 5000

ENTRYPOINT python ./app/app.py
