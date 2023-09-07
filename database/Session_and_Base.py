from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from sqlalchemy.ext.associationproxy import association_proxy
import click
import random

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///database/SMS.db')
Session = sessionmaker(bind=engine)
session = Session()