from database import engine
from sqlalchemy.orm import Session
import models, schemas
import os

def get_actors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Actor).offset(skip).limit(limit).all()

def recreate_database():
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

# if __name__ == "__main__":
#     recreate_database()
