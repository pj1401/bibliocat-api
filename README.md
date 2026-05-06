# BiblioCat API

Bibliotekskatalog API

## Contents

- [Usage](#usage)
  - [Installation](#installation)
- [Development](#development)
  - [Setting up the environment](#setting-up-the-environment)
  - [Instructions](#instructions)
  - [File Structure](#file-structure)

## Usage

Link to production here.

### Installation

The API can be run in a docker container.

**Prerequisites:**
- docker-compose, [Docker Compose installation instructions](https://docs.docker.com/compose/install/)

**Run setup:**

```powershell
# Start database and run setup in detached mode
docker compose up db setup -d
```

**Start API:**

The API service can be started after seeding the database.

```powershell
# Start the api service in detached mode
docker compose up api -d
```

The API can be accessed here: [127.0.0.1:5000](http://127.0.0.1:5000/)

**Stop container:**

```powershell
docker compose down
```

**Restart API:**

Don't start the setup service after initial setup:

```powershell
docker compose up db api -d
```

If volumes are removed with `docker compose down -v` the setup service has to run before starting the API again.

## Development

**Prerequisites:**
- docker-compose, [Docker Compose installation instructions](https://docs.docker.com/compose/install/)
- uv, [uv installation instructions](https://docs.astral.sh/uv/getting-started/installation/)

### Setting up the environment

If you haven't already set up an `.env` file:

```powershell
# Copy from .example.env to .env
cp .example.env .env
```

A PostgreSQL database is used to store data. Book data has to be inserted into the database before running the API. A subset of the books dataset is included in `setup/data-subset/`.

**Use full dataset (optional):**

The full dataset can be downloaded here: [Google Books Dataset](https://www.kaggle.com/datasets/bilalyussef/google-books-dataset)  

To use the full dataset:
 - Place the `google_books_1299.csv` file into the `setup/data` directory. (gitignored)
 - The `CSV_PATH` variable in the `docker-compose.yml` has to be updated.
 - Update the `dockerfile` in the `setup` directory, so the correct data is copied.

docker-compose.yml:

```docker-compose.yml
environment:
  CSV_PATH: data/google_books_1299.csv
```

dockerfile:

```dockerfile
# Copy dataset
# COPY setup/data-subset/ ./data-subset
COPY setup/data/ ./data
```

**Generating keys for the API:**

Any random string should work for the `FLASK_SECRET_KEY` environment variable. One way is to generate a random string using Python:

```python
# Get a random string for FLASK_SECRET_KEY in .env
>>> import os
>>> os.urandom(16).hex()
'aacddd29dfe77708800856e643ef2426'
```

The app uses ECDSA for JWT signing.  
To generate the key pair:

```bash
# Generate private key
openssl ecparam -name secp521r1 -genkey -noout -out bibliocat-api-jwt.pem

# Extract public key
openssl ec -in bibliocat-api-jwt.pem -pubout -out bibliocat-api-jwt.public.pem
```

Copy the contents of the key pair files to the `.env` file.

### Instructions

**Run setup:**

```powershell
# Build image
docker-compose build --no-cache

# Start database and run setup in detached mode
docker-compose up db setup -d
```

**Start API:**

```powershell
# Change to the api directory
cd api/

# Start the database if it's not running
docker-compose up db -d

# Create a virtual environment and activate it. See: https://docs.astral.sh/uv/pip/environments/
uv venv
.venv\Scripts\activate # Activates venv (Windows)

# Install dependencies
uv pip install -r pyproject.toml

# Start the app in debug mode
uv run -- flask --app main run --debug

# To stop the container
docker-compose down
docker-compose down -v # Removes volumes (data)
```

**For debugging setup:**

```powershell
# Change to setup directory
cd setup

# Create a virtual environment and activate it. See: https://docs.astral.sh/uv/pip/environments/
uv venv
.venv\Scripts\activate # Windows

# Install dependencies
uv pip install -r pyproject.toml

# Start database in detached mode
docker-compose up db -d

# Run setup script
uv run main.py
```

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

- [Flask application factory](https://github.com/cookiecutter-flask/cookiecutter-flask/blob/master/%7B%7Bcookiecutter.app_name%7D%7D/%7B%7Bcookiecutter.app_name%7D%7D/app.py): used as a template for [api/main.py](./api/main.py)
- [README template](https://gist.github.com/ramantehlan/602ad8525699486e097092e4158c5bf1)
