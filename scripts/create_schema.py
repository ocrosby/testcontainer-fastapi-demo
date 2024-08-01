import os
import sys
import psycopg2

from dotenv import load_dotenv

load_dotenv()


def execute_sql_files(directory):
    """
    Execute all SQL files in a directory

    :param directory:
    :return:
    """
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME", "postgres"),
        user=os.getenv("DB_USERNAME", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432")
    )
    cur = conn.cursor()

    sql_files = sorted([f for f in os.listdir(directory) if f.endswith('.sql')])
    for sql_file in sql_files:
        with open(os.path.join(directory, sql_file), 'r', encoding='utf-8') as f:
            cur.execute(f.read())
            print(f"Executed {sql_file}")

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    execute_sql_files('sql/schema')
    if len(sys.argv) > 1 and sys.argv[1] == '--with-data':
        execute_sql_files('sql/data')
