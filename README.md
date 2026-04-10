# Library App

Bibliotekskatalog

## Seed database

Dataset: [Google Books Dataset](https://www.kaggle.com/datasets/bilalyussef/google-books-dataset)  
A subset of the dataset is included in `setup/data-subset/`.

To use the full dataset:
 - Place the `google_books_1299.csv` file into the `setup/data` directory. (gitignored)
 - The `CSV_PATH` variable in the `.env` file has to be updated:

```
CSV_PATH=data/google_books_1299.csv
```

### Instructions

```powershell
# Copy from .example.env to .env
cp .example.env .env
```

## Run dev
