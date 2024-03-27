import mariadb
import sys
import os


def get_connection():

    user = os.getenv('DB_USER', 'default_user')
    password = os.getenv('DB_PASSWORD', 'default_password')
    host = os.getenv('DB_ADDRESS', 'default_host')
    port = int(os.getenv('DB_PORT', 'default_port'))
    database = os.getenv('DB_DATABASE', 'default_database')

    try:
        conn = mariadb.connect(
            user=user, password=password, host=host, port=port, database=database
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    print("Connected to MariaDB Platform!")
    return conn
