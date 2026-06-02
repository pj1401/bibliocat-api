# Contributing

## Contents

- [Getting started](#getting-started)
  - [Environment variables](#environment-variables)
  - [Start API](#start-api)
- [Folder structure](#folder-structure)
- [Coding style](#coding-style)
- [Branching](#branching)
- [Commit messages](#commit-messages)
- [Merging to main](#merging-to-main)
- [Running tests](#running-tests)
- [Time tracking (GitLab)](#time-tracking-gitlab)
- [Versioning](#versioning)

## Getting started

**Prerequisites:**
- docker compose, [Docker Compose installation instructions](https://docs.docker.com/compose/install/)
- uv for development, [uv installation instructions](https://docs.astral.sh/uv/getting-started/installation/)

```bash
# ssh
git clone git@github.com:pj1401/bibliocat-api.git

# change directory
cd bibliocat-api

# Copy from .example.env to .env
cp .example.env .env
```

### Environment variables

| Variable | Description |
|---|---|
| `CSV_PATH` | The path to the CSV file. Only used in setup. |
| `CHUNK_SIZE` | Specifies how many rows are loaded from the CSV file at a time. Only used in setup. |
| `POSTGRES_HOST` | The PostgreSQL host. |
| `POSTGRES_PORT` | The port to the PostgreSQL container. Defaults to 5432. |
| `POSTGRES_DB` | The database name. |
| `POSTGRES_USER` | The database username. |
| `POSTGRES_PASSWORD` | The password for the database user. |
| `BASE_URL` | The base URL of the application. Example: 'http://localhost:5000' for develop mode. |
| `FLASK_DEBUG` | Whether debug mode is enabled. Defaults to 'False'. |
| `FLASK_HOST` | The hostname to listen on. Set this to '0.0.0.0' to have the server available externally as well. Defaults to '127.0.0.1'. |
| `FLASK_PORT` | The port of the webserver. Defaults to 5000. |
| `FLASK_SECRET_KEY` | A secret key used for signing session cookies. |
| `JWT_PRIVATE_KEY` | An EC private key used for signing JWTs. |
| `JWT_PUBLIC_KEY` | An EC public key. |

**Set up secrets:**

Set up secrets for docker compose. The secrets are stored in the `secrets` directory which is not version controlled.

```bash
mkdir secrets
echo -n "library-postgres" > secrets/db_name.txt
echo -n "username" > secrets/db_user.txt
echo -n "password" > secrets/db_password.txt
echo "random-string" > secrets/flask_secret_key.txt
```

**There can't be any trailing newlines in `secrets/db_name.txt`, `secrets/db_user.txt` or `secrets/db_password.txt`. The database initialisation won't work if there is. Use `echo -n` to suppress the trailing newline.**

Any random string should work for the `FLASK_SECRET_KEY` environment variable. One way is to generate a random string using Python:

```python
>>> import os
>>> os.urandom(16).hex()
'aacddd29dfe77708800856e643ef2426'
```

The app uses ECDSA for JWT signing.  
To generate the key pair:

```bash
# Generate private key
openssl ecparam -name secp521r1 -genkey -noout -out secrets/bibliocat-api-jwt-key

# Extract public key
openssl ec -in secrets/bibliocat-api-jwt-key -pubout -out secrets/bibliocat-api-jwt-key.pub
```

**Use full dataset (optional):**

A PostgreSQL database is used to store data. Book data has to be inserted into the database before running the API. A subset of the books dataset is included in `setup/data-subset/`.

The full dataset can be downloaded here: [Google Books Dataset](https://www.kaggle.com/datasets/bilalyussef/google-books-dataset)  

To use the full dataset:
 - Place the `google_books_1299.csv` file into the `setup/data` directory. (gitignored)
 - Use `docker-compose.yml` when building with docker compose.

### Start API

**Using docker compose:**

```powershell
# Start the services in detached mode
docker compose -f docker-compose.dev-subset.yml up -d

# Remove '-f docker-compose.dev-subset.yml' if the full dataset is used:
docker compose up -d
```

The API can be accessed here: [127.0.0.1:5000](http://127.0.0.1:5000/)

**To stop containers:**

```powershell
docker compose down
docker compose down -v # Removes volumes (data)
```

**Rebuild images:**

To build images after code changes:

```powershell
docker compose -f docker-compose.dev-subset.yml up -d --build
```

**Using uv:**

The secrets have to be copied to the `.env` file if using uv.

```powershell
# Change to the api directory
cd api/

# Create venv and install
uv sync --group dev

# Start the database if it's not running
docker compose up db setup -d

# Start the app in debug mode
uv run -- flask --app src/main run --debug

# To stop the container
docker compose down
docker compose down -v # Removes volumes (data)
```

**For debugging setup:**

```powershell
# Change to setup directory
cd setup

# Create venv and install
uv sync --group dev

# Start database in detached mode
docker compose up db -d

# Run setup script
uv run main.py
```

## Folder structure

```
bibliocat-api
├── api/                        # Main project directory
│  ├── src/
│  │   ├── blueprints/          # Flask blueprints
│  │   │   ├── api/
│  │   │   │   └── v1/          # API v1 routes
│  │   │   └── router.py
│  │   ├── config/
│  │   ├── controllers/         # API controllers
│  │   ├── db/                  # Database connection manager
│  │   ├── hooks/               # Flask decorators.
│  │   ├── repositories/        # Database interactions
│  │   ├── services/            # Business logic
│  │   └── util/
│  │       ├── errors/
│  │       ├── models/          # SQL Alchemy models
│  │       └── schemas/         # Pydantic models
│  ├── dockerfile
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
│  │   └── transformer.py
│  ├── dockerfile
│  ├── main.py
│  ├── pyproject.toml
│  ├── requirements.txt
│  └── uv.lock
├── .example.env
├── .gitignore
├── docker-compose.yml
└── README.md
```

## Coding style

- Language/framework style guide: python, flask, SQLAlchemy
- Linting tool: pyright strict (used in main API project, not in setup script)
- Formatting tool: ruff

Pyright and ruff is installed with the other dependencies.

Code in the `main` branch should always be formatted. Before opening a pull request run these:

```
# Only in the api directory
uv run pyright

# Ruff is used in both the setup/ and api/ directories
uv run ruff check

uv run ruff format
```

## Branching

- `main` - stable, deployable code only
- `feature/your-feature` - one branch per issue
- Never push directly to `main`

## Commit messages

Short and descriptive. Reference the issue number:

```
Add login form (#12)
Fix broken redirect on logout (#15)
```

## Merging to main

Before merging a feature branch:
- [ ] Code works locally
- [ ] Tests pass
- [ ] No `.env` or secrets committed
- [ ] Linked to an issue

## Running tests

see [tests README](tests/README.md)

## Time tracking (GitLab)

Every issue should have an estimate and logged time. Use quick actions in issue comments:

```
/estimate 2h
```
```
Implemented the login form, took longer due to validation edge cases.
/spend 3h
```

**For non-development time** (reading, videos, lectures, meetings) - don't create a separate issue for each. Use one standing issue per iteration called **"Learning & overhead - Iteration N"** and log time there:

```
Watched CI/CD lecture video.
/spend 1h
```

```
Read course literature chapter 4.
/spend 1.5h
```

Log time as you go - **not at the end of the week.** All time counts: coding, reading, debugging, meetings.

## Versioning

This project uses [semantic versioning](https://semver.org) with Git tags: `vMAJOR.MINOR.PATCH`

- **MAJOR** - breaking changes
- **MINOR** - new features, backwards compatible
- **PATCH** - bug fixes

Each iteration ends with a tag. The tag is your deliverable - if it is not tagged, it is not done.

```bash
git describe --tags --dirty
# -> v1.0.0          (exactly on a tag)
# -> v1.0.0-4-gabcde (4 commits after v1.0.0)
# -> v1.0.0-4-gabcde-dirty (uncommitted changes)
```

Only repository admins are allowed to create tags in this repository.  
To tag a release:

```bash
git tag v1.0.0
git push origin v1.0.0
```
