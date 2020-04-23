#!/usr/bin/python3
"""This is the file storage class for AirBnB"""

import os

from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """This class save instances to a mysql db and
    get instances from the db
    Attributes:
            __engine: create the interfaces of comunication with db
            __session: open a comunication with the db
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of a DBStorage
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == 'test':
            # Drop all tables
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns a dictionary with all the objects from the db
        """
        data = {}
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Amenity).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            data[key] = obj
        return data

    def new(self, obj):
        """add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Delete an specific object from __objects
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        call remove() for session
        """
        self.__session.close()
