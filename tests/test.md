# Testing

## Pytest

**Prerequisites:**
 - uv, [uv installation instructions](https://docs.astral.sh/uv/getting-started/installation/)

```powershell
# Change to the api directory
cd api

# Install the package
uv pip install -e .

# Run tests
pytest
```

## Apidog

**Prerequisites:**
 - docker-compose, [Docker Compose installation instructions](https://docs.docker.com/compose/install/)
 - Apidog CLI is installed, see [https://docs.apidog.com/installing-and-running-apidog-cli-605135m0](https://docs.apidog.com/installing-and-running-apidog-cli-605135m0)

```powershell
# Start the containers
docker compose up -d --build

apidog run ./tests/develop-env/collection.apidog-cli.json -n 1
apidog run ./tests/develop-env/auth.apidog-cli.json -n 1
apidog run ./tests/develop-env/books.apidog-cli.json -n 1
apidog run ./tests/develop-env/authors.apidog-cli.json -n 1
apidog run ./tests/develop-env/reading-logs.apidog-cli.json -n 1
```
