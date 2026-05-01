# BiblioCat API

Bibliotekskatalog API

## Contents

- [Development](#development)
  - [File Structure](#file-structure)
  - [Seed database](#seed-database)
    - [Instructions](#instructions)
  - [Run API](#run-api)
    - [Set up env](#set-up-env)
    - [Instructions](#instructions-1)

## Usage

Link to production here.

### Installation

Move docker-compose instructions here?

## Development

**Prerequisites:**
- docker-compose, [Docker Compose installation instructions](https://docs.docker.com/compose/install/)
- uv, [uv installation instructions](https://docs.astral.sh/uv/getting-started/installation/)
  - only needed for debug

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

### Seed database

A PostgreSQL database is used to store data. Before running the API book data has to be inserted into the database. A subset of the books dataset is included in `setup/data-subset/`.  
The full dataset can be downloaded here (optional): [Google Books Dataset](https://www.kaggle.com/datasets/bilalyussef/google-books-dataset)  

To use the full dataset:
 - Place the `google_books_1299.csv` file into the `setup/data` directory. (gitignored)
 - The `CSV_PATH` variable in the `.env` file has to be updated.
 - Update the `dockerfile` in the `setup` directory, so the correct data is copied.

```
CSV_PATH=data/google_books_1299.csv
```

```dockerfile
# Copy the src directory and main.py
COPY setup/src ./src
COPY setup/main.py .
# COPY setup/data-subset/ ./data-subset
COPY setup/data/ ./data
```

#### Instructions

**Run setup:**

```powershell
# Copy from .example.env to .env
cp .example.env .env

# Build image
docker-compose build --no-cache

# Start database and run setup in detached mode
docker-compose up db setup -d
```

**For debugging:**

If making changes to the setup script.

```powershell
# For debugging, start only database in detached mode
docker-compose up db -d

# Change to setup directory
cd setup

# Create a virtual environment and activate it. See: https://docs.astral.sh/uv/pip/environments/
uv venv
.venv\Scripts\activate # Windows

# Install dependencies
uv pip install -r pyproject.toml

# Run setup script
uv run main.py

# To stop the container
docker-compose down
docker-compose down -v # Removes volumes (data)
```

### Run API

After seeding the database the API service can be started using docker-compose.

```powershell
# Start the api service in detached mode
docker-compose up api -d
```

**For debugging:**

#### Set up env

Python can be used to generate a random string for the `FLASK_SECRET_KEY` env variable:

```python
# Get a random string for FLASK_SECRET_KEY in .env
>>> import os
>>> os.urandom(16).hex()
'aacddd29dfe77708800856e643ef2426'
```

Any random string should work.

The app uses ECDSA for JWT signing.  
To generate the key pair:

```bash
# Generate private key
openssl ecparam -name secp521r1 -genkey -noout -out bibliocat-api-jwt.pem

# Extract public key
openssl ec -in bibliocat-api-jwt.pem -pubout -out bibliocat-api-jwt.public.pem
```

Copy the contents of the key pair files to the `.env` file.

#### Instructions

```powershell
# Change to the api directory
cd api/

# Start the database
docker-compose up db -d

# Create a virtual environment and activate it. See: https://docs.astral.sh/uv/pip/environments/
uv venv
.venv\Scripts\activate # Activates venv (Windows)

# Install dependencies
uv pip install -r pyproject.toml

# Start the app in debug mode
uv run -- flask --app main run --debug

# Stop the database when done
docker-compose down
```

## Acknowledgements

- [Flask application factory](https://github.com/cookiecutter-flask/cookiecutter-flask/blob/master/%7B%7Bcookiecutter.app_name%7D%7D/%7B%7Bcookiecutter.app_name%7D%7D/app.py): used as a template for [api/main.py](./api/main.py)
- [README template](https://gist.github.com/ramantehlan/602ad8525699486e097092e4158c5bf1)
