from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

Base = declarative_base()

class Category(Base):
    __tablename__ = "category"
    category_id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    name = Column(String)
    last_update = Column(Date)

    # def __repr__(self):
    #     return f'{"Category id: "}{self.category_id}{" Category name: "}{self.name}'