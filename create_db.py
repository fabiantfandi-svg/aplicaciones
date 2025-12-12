import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

DB_NAME = "mi_basedatos"
DB_USER = "postgres"
DB_PASSWORD = "1234"  
DB_HOST = "localhost"
DB_PORT = "5432"

print("Conectando a PostgreSQL...")

try:
    con = psycopg2.connect(
        dbname="postgres",
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()

    cur.execute("SELECT 1 FROM pg_database WHERE datname=%s", (DB_NAME,))
    exists = cur.fetchone()

    if not exists:
        print(f"Creando la base de datos: {DB_NAME}")
        cur.execute(f'CREATE DATABASE "{DB_NAME}"')
        print("Base creada correctamente.")
    else:
        print("La base ya existe. OK.")

    cur.close()
    con.close()

except Exception as e:
    print("Error creando la base de datos:", e)
