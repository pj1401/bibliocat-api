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

```powershell
# Copy from .example.env to .env
cp .example.env .env

# Build image
docker-compose build --no-cache

# Start database and run setup
docker-compose up db setup
docker-compose up db -d      # Start only database in detached mode

# Stop container
docker-compose down
docker-compose down -v # Removes volumes(data)
```

## Run dev
