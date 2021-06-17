from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

user_name = os.environ.get("USR")
pwd = os.environ.get("PWD")

DB_NAME = "dvdrentals"

DATABASE_URL = "postgresql://"+user_name+":"+pwd+"@localhost:5432/"

postgres_engine = create_engine(
    DATABASE_URL, isolation_level="AUTOCOMMIT"
)

def create_database(dbName:str):

    with postgres_engine.connect() as conn:
        #conn.execute("commit")
        dbs = conn.execute("SELECT datname FROM pg_database;")
        dbs = [f[0] for f in dbs]
        
        if dbName in dbs:
            print(f'{dbName}{" already exists!"}')
            SQLALCHEMY_DATABASE_URL = f'{DATABASE_URL}{dbName}'
            engine = create_engine(
                        SQLALCHEMY_DATABASE_URL, isolation_level="AUTOCOMMIT")

        else:
            conn.execute(f'{"CREATE DATABASE "}{dbName}')
            print(f'{"Created: "}{dbName}')
            SQLALCHEMY_DATABASE_URL = f'{DATABASE_URL}{dbName}'
            engine = create_engine(
                        SQLALCHEMY_DATABASE_URL, isolation_level="AUTOCOMMIT")
    return engine

def drop_database(dbName:str) -> None:

    with postgres_engine.connect() as conn:
        conn.execute("commit")
        conn.execute(f'{"DROP DATABASE "}{dbName}')

engine = create_database(DB_NAME)
# print(engine.table_names())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

