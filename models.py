from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ARRAY, Boolean, CHAR, Column, Date, DateTime, Enum, ForeignKey, Index, Integer, LargeBinary, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.postgresql import TSVECTOR

Base = declarative_base()

# class Category(Base):
#     __tablename__ = "category"
#     category_id = Column(Integer, primary_key=True)
#     title = Column(String, index=True)
#     name = Column(String)
#     last_update = Column(Date)

    # def __repr__(self):
    #     return f'{"Category id: "}{self.category_id}{" Category name: "}{self.name}'



# from sqlalchemy import ARRAY, Boolean, CHAR, Column, Date, DateTime, Enum, ForeignKey, Index, Integer, LargeBinary, Numeric, SmallInteger, String, Table, Text, text
# from sqlalchemy.orm import relationship
# from sqlalchemy.dialects.postgresql import TSVECTOR
# from sqlalchemy.ext.declarative import declarative_base

#Base = declarative_base()
#metadata = Base.metadata


class Actor(Base):
    __tablename__ = 'actor'

    actor_id = Column(Integer, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False, index=True)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))


class Country(Base):
    __tablename__ = 'country'

    country_id = Column(Integer, primary_key=True)
    country = Column(String(50), nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

class Language(Base):
    __tablename__ = 'language'

    language_id = Column(Integer, primary_key=True)
    name = Column(CHAR(20), nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

class City(Base):
    __tablename__ = 'city'

    city_id = Column(Integer, primary_key=True)
    city = Column(String(50), nullable=False)
    country_id = Column(ForeignKey('country.country_id'), nullable=False, index=True)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

    country = relationship('Country')

class Film(Base):
    __tablename__ = 'film'

    film_id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text)
    release_year = Column(Integer)
    language_id = Column(ForeignKey('language.language_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False, index=True)
    rental_duration = Column(SmallInteger, nullable=False, server_default=text("3"))
    rental_rate = Column(Numeric(4, 2), nullable=False, server_default=text("4.99"))
    length = Column(SmallInteger)
    replacement_cost = Column(Numeric(5, 2), nullable=False, server_default=text("19.99"))
    rating = Column(Enum('G', 'PG', 'PG-13', 'R', 'NC-17', name='mpaa_rating'), server_default=text("'G'::mpaa_rating"))
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))
    special_features = Column(ARRAY(Text()))
    fulltext = Column(TSVECTOR, nullable=False, index=True)

    language = relationship('Language')


class Addres(Base):
    __tablename__ = 'address'

    address_id = Column(Integer, primary_key=True)
    address = Column(String(50), nullable=False)
    address2 = Column(String(50))
    district = Column(String(20), nullable=False)
    city_id = Column(ForeignKey('city.city_id'), nullable=False, index=True)
    postal_code = Column(String(10))
    phone = Column(String(20), nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

    city = relationship('City')


class FilmActor(Base):
    __tablename__ = 'film_actor'

    actor_id = Column(ForeignKey('actor.actor_id', ondelete='RESTRICT', onupdate='CASCADE'), primary_key=True, nullable=False)
    film_id = Column(ForeignKey('film.film_id', ondelete='RESTRICT', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

    actor = relationship('Actor')
    film = relationship('Film')


class FilmCategory(Base):
    __tablename__ = 'film_category'

    film_id = Column(ForeignKey('film.film_id', ondelete='RESTRICT', onupdate='CASCADE'), primary_key=True, nullable=False)
    category_id = Column(ForeignKey('category.category_id', ondelete='RESTRICT', onupdate='CASCADE'), primary_key=True, nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

    category = relationship('Category')
    film = relationship('Film')


class Inventory(Base):
    __tablename__ = 'inventory'
    __table_args__ = (
        Index('idx_store_id_film_id', 'store_id', 'film_id'),
    )

    inventory_id = Column(Integer, primary_key=True)
    film_id = Column(ForeignKey('film.film_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    store_id = Column(SmallInteger, nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

    film = relationship('Film')


class Customer(Base):
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True)
    store_id = Column(SmallInteger, nullable=False, index=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False, index=True)
    email = Column(String(50))
    address_id = Column(ForeignKey('address.address_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False, index=True)
    activebool = Column(Boolean, nullable=False, server_default=text("true"))
    create_date = Column(Date, nullable=False, server_default=text("('now'::text)::date"))
    last_update = Column(DateTime, server_default=text("now()"))
    active = Column(Integer)

    address = relationship('Addres')


class Staff(Base):
    __tablename__ = 'staff'

    staff_id = Column(Integer, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    address_id = Column(ForeignKey('address.address_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    email = Column(String(50))
    store_id = Column(SmallInteger, nullable=False)
    active = Column(Boolean, nullable=False, server_default=text("true"))
    username = Column(String(16), nullable=False)
    password = Column(String(40))
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))
    picture = Column(LargeBinary)

    address = relationship('Addres')


class Rental(Base):
    __tablename__ = 'rental'
    __table_args__ = (
        Index('idx_unq_rental_rental_date_inventory_id_customer_id', 'rental_date', 'inventory_id', 'customer_id', unique=True),
    )

    rental_id = Column(Integer, primary_key=True)
    rental_date = Column(DateTime, nullable=False)
    inventory_id = Column(ForeignKey('inventory.inventory_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False, index=True)
    customer_id = Column(ForeignKey('customer.customer_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    return_date = Column(DateTime)
    staff_id = Column(ForeignKey('staff.staff_id'), nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

    customer = relationship('Customer')
    inventory = relationship('Inventory')
    staff = relationship('Staff')


class Store(Base):
    __tablename__ = 'store'

    store_id = Column(Integer, primary_key=True)
    manager_staff_id = Column(ForeignKey('staff.staff_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False, unique=True)
    address_id = Column(ForeignKey('address.address_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

    address = relationship('Addres')
    manager_staff = relationship('Staff')


class Payment(Base):
    __tablename__ = 'payment'

    payment_id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.customer_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False, index=True)
    staff_id = Column(ForeignKey('staff.staff_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False, index=True)
    rental_id = Column(ForeignKey('rental.rental_id', ondelete='SET NULL', onupdate='CASCADE'), nullable=False, index=True)
    amount = Column(Numeric(5, 2), nullable=False)
    payment_date = Column(DateTime, nullable=False)

    customer = relationship('Customer')
    rental = relationship('Rental')
    staff = relationship('Staff')