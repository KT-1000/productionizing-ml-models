# {{cookiecutter.project_slug}}
{{cookiecutter.project_short_description}}

## Installation and Use

### Prerequisites
1. [Docker](https://docs.docker.com/get-started/#prepare-your-docker-environment) installed and daemon running.
2. GitHub repo has been cloned via SSH, and you're in the local repo:
```
    git clone git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.git
    cd {{cookiecutter.project_slug}}
```

### Run locally
1. Build docker image:
    `docker build -t {{cookiecutter.project_slug}} .`
