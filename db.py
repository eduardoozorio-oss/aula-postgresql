import psycopg2 as pg
#pip install psycopg2 
#pip intall dotenv
from dotenv import load_dotenv
import os

#carregar as variavéis do .env
load_dotenv()

PARAMS = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.gevetn("DB_HOST"),
    "port": os.genetn("DB_PORT"),





}