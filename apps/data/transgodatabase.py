#!/usr/bin/env python
# coding: utf-8

from sqlalchemy import Column
from sqlalchemy import String, Integer
from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = Column(String(20), primary_key=True)
    user_name = Column(String(20))


class UserType(Base):
    """用户类型

    """
    __tablename__ = "user_type"

    type_id = Column(Integer(), primary_key=True)
    type_name = Column(String(20))


class Clienter(Base):
    """客户

    """
    __tablename__ = "clienter"

    clienter_id = Column(String(20), primary_key=True)
    clienter_name = Column(String(20))


class Order(Base):
    """订单

    """
    __tablename__ = "order"

    order_id = Column(String(20), primary_key=True)
    order_client = Column(String(20))

# TODO: session
# Session = sessionmaker()
# Session.configure(bind=engine)


def init_database():
    engine = create_engine("sqlite:///data/transgo.db")
    Base.metadata.create_all(engine)
