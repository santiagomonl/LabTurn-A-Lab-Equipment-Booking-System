from sqlalchemy import create_engine, text

# Database Configuration
DATABASE_URL = 'postgresql://santiagoml:t6cP6VgnMG8Xa9l8yNozRxKVF9EtTGcP@dpg-cuf6i9tumphs73aunut0-a.frankfurt-postgres.render.com/labturn_database'

# Create an engine for the default 'postgres' database
default_engine = create_engine(DATABASE_URL.replace('labturn_database', 'postgres'), isolation_level="AUTOCOMMIT")

# Drop the existing database
with default_engine.connect() as conn:
    conn.execute(text("DROP DATABASE IF EXISTS labturn_database"))

# Create a new database
with default_engine.connect() as conn:
    conn.execute(text("CREATE DATABASE labturn_database"))

print("Database reset successfully.")