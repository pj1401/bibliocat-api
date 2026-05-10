set -e

wait_for_db() {
  until pg_isready -U postgres -d postgres -h localhost; do
    echo "Waiting for PostgreSQL to be ready..."
    sleep 1
  done
}

wait_for_db

# Read secrets from files
DB_USER=$(cat /run/secrets/db_user)
DB_PASSWORD=$(cat /run/secrets/db_password)
DB_NAME=$(cat /run/secrets/db_name)

# Create the user and database
psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "postgres" <<-EOSQL
    CREATE USER "$DB_USER" WITH PASSWORD '$DB_PASSWORD';
    CREATE DATABASE "$DB_NAME";
    GRANT ALL PRIVILEGES ON DATABASE "$DB_NAME" TO "$DB_USER";
EOSQL
