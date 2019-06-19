# {{cookiecutter.project_slug}}
{{cookiecutter.project_short_description}} by {{cookiecutter.author}}

WARNING: this is a demonstration of cookiecutter only and will not work as a deployable model.

## Installation and Use

### Prerequisites
1. [Docker](https://docs.docker.com/get-started/#prepare-your-docker-environment) installed and daemon running.
2. GitHub repo has been cloned via SSH, and you're in the local repo:
```bash
    git clone git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.git
    cd {{cookiecutter.project_slug}}
```

### Run locally
1. Ensure the appropriate model files are in `app/data/`
   
2. Build docker image:
    `docker build -t {{cookiecutter.project_slug}} .`

3. Run the container:
   
```bash
  docker run -d -p 5000:5000 {{cookiecutter.project_slug}}
```

4. POST appropriately formatted JSON to ensure prediction is returned:

```bash
curl -d '{"message":"CHANGE"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/predict
```
Returns something like:
```bash
{
  "timestamp" : "06-19-2018 09:15",
  "status" : 200,
  "message" : "CHANGE"
}
```
