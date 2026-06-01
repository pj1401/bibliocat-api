# Testing

## Pytest

**Prerequisites:**
 - uv, [uv installation instructions](https://docs.astral.sh/uv/getting-started/installation/)

```powershell
# Change to the api directory
cd api

# Create venv and install
uv sync --group dev

# Run tests
uv run pytest
```

## Apidog

**Prerequisites:**
 - docker compose, [Docker Compose installation instructions](https://docs.docker.com/compose/install/)
 - Node.js, [Download Node.js](https://nodejs.org/en/download)
 - Apidog CLI, [Installing and Running Apidog CLI](https://docs.apidog.com/installing-and-running-apidog-cli-605135m0)
 - Environment and secret variables have been set up. See [Installation: Set up secrets](../README.md#installation)

Start containers:

```powershell
# Start the services in detached mode
docker compose -f docker-compose.dev-subset.yml up -d --build

# Or if the full dataset is used:
docker compose up -d --build
```

Run API tests:

```powershell
apidog run ./tests/develop-env/collection.apidog-cli.json -n 1
apidog run ./tests/develop-env/auth.apidog-cli.json -n 1
apidog run ./tests/develop-env/books.apidog-cli.json -n 1
apidog run ./tests/develop-env/authors.apidog-cli.json -n 1
apidog run ./tests/develop-env/reading-logs.apidog-cli.json -n 1
```

Stop containers and remove data:

```powershell
docker compose down -v
```
