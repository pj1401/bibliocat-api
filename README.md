# BiblioCat API

Bibliotekskatalog API

## Seed database

Dataset: [Google Books Dataset](https://www.kaggle.com/datasets/bilalyussef/google-books-dataset)  
A subset of the dataset is included in `setup/data-subset/`.

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

### Instructions

**Prerequisites**:
- docker-compose [Docker Compose installation instructions](https://docs.docker.com/compose/install/)
- uv [uv installation instructions](https://docs.astral.sh/uv/getting-started/installation/)
  - only needed for debug

```powershell
# Copy from .example.env to .env
cp .example.env .env

# Build image
docker-compose build --no-cache

# Start database and run setup
docker-compose up db setup

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

# Stop container
docker-compose down
docker-compose down -v # Removes volumes (data)
```

## Run dev

```python
# Get a random string for FLASK_SECRET_KEY in .env
>>> import os
>>> os.urandom(16).hex()
'aacddd29dfe77708800856e643ef2426'
```

### Instructions

**Prerequisites**:
- docker-compose [Docker Compose installation instructions](https://docs.docker.com/compose/install/)
- uv [uv installation instructions](https://docs.astral.sh/uv/getting-started/installation/)

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
