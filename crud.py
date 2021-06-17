from models import Base
from database import engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    recreate_database()
