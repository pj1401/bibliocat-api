# BiblioCat API

Bibliotekskatalog API

## Contents

- [Usage](#usage)
  - [Installation](#installation)
- [Development](#development)
  - [Testing](#testing)
  - [File Structure](#file-structure)
- [Acknowledgements](#acknowledgements)

## Usage

The API is running on: [https://patriciaj.se/bibliocat-api](https://patriciaj.se/bibliocat-api)

Version 1 docs: [https://patriciaj.se/bibliocat-api/api/v1/docs/](https://patriciaj.se/bibliocat-api/api/v1/docs/)

## Development

see [Contributing](CONTRIBUTING.md)

### Testing

see [tests README](tests/README.md)

### File Structure
```
bibliocat-api
├── api/                        # Main project directory
│  ├── src/
│  │   ├── blueprints/          # Flask blueprints
│  │   │   ├── api/
│  │   │   │   └── v1/          # API v1 routes
│  │   │   │       ├── users/
|  |   |   |       |   └── routes.py
|  |   |   |       └── router.py
│  │   │   └── router.py
│  │   ├── config/
│  │   ├── controllers/         # API controllers
│  │   │   └── user_controller.py
│  │   ├── db/                  # Database connection manager
│  │   ├── hooks/               # Functions to run before and after requests
│  │   ├── repositories/        # Database interactions
│  │   │   └── user_repo.py
│  │   ├── services/            # Business logic
│  │   │   └── user_service.py
│  │   └── util/
│  │       ├── errors/
│  │       ├── models/          # SQL Alchemy models
│  │       └── schemas/         # Pydantic models
│  ├── Dockerfile
│  ├── main.py
│  ├── pyproject.toml
│  ├── requirements.txt
│  └── uv.lock
├── setup/
│  ├── data/                    # Dataset for loading database
│  ├── data-subset/
│  ├── src/
│  │   ├── database_loader.py
│  │   ├── extractor.py
│  │   ├── models.py            # SQL Alchemy models
│  │   └── transformer.py
│  ├── Dockerfile
│  ├── main.py
│  ├── pyproject.toml
│  ├── requirements.txt
│  └── uv.lock
├── .dockerignore
├── .example.env
├── .gitignore
├── docker-compose.yml
└── README.md
```

## Acknowledgements

- Full dataset: [Google Books Dataset](https://www.kaggle.com/datasets/bilalyussef/google-books-dataset)
- [Flask application factory](https://github.com/cookiecutter-flask/cookiecutter-flask/blob/master/%7B%7Bcookiecutter.app_name%7D%7D/%7B%7Bcookiecutter.app_name%7D%7D/app.py): used as a template for [api/main.py](./api/main.py)
- [README template](https://gist.github.com/ramantehlan/602ad8525699486e097092e4158c5bf1)
