import psycopg2

DB_HOST = "localhost"
DB_NAME = "avaliacao_campus"
DB_USER = "postgres"
DB_PASSWORD = "1234"

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
