#!/usr/bin/env python
# coding: utf-8

# import uuid
from datetime import datetime
from apps import logging

from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, DateTime, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import config


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer,
                     primary_key=True,
                     autoincrement=True)
    user_name = Column(String(20))
    user_type = Column(Integer, ForeignKey('user_type.type_id'))

    # def __init__(self, user_name, user_type):
    #     self.user_name = user_name
    #     self.user_type = user_type


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

    clienter_id = Column('client_id', String(20), primary_key=True)
    clienter_name = Column(String(20))


class Order(Base):
    """订单

    """
    __tablename__ = "order"

    ID = Column(String(20), primary_key=True)
    clienter = Column(String(20), nullable=False)
    tick = Column(String(20))
    user = Column(String(6))
    addr = Column(String(128), nullable=False)
    tel = Column(String(11))
    count = Column(Integer)
    express = Column(String(10))
    time = Column(DateTime,
                  default=datetime.now)
    descript = Column(String(256))
    print_status = Column(String(5))
    cancel_status = Column(Boolean)

    status = Column(String(10), nullable=False, default="Import")

    courise = Column(Integer, ForeignKey("courise.courise_id"))

    def __init__(self,
                 ID,
                 clienter=None,
                 tick=None,
                 user=None,
                 addr=None,
                 tel=None,
                 count=None,
                 express=None,
                 time=None,
                 descript=None,
                 print_status=None,
                 cancel_status=None):
        self.ID = ID
        self.clienter = clienter
        self.tick = tick
        self.user = user
        self.addr = addr
        self.tel = tel
        self.count = count
        self.express = express
        self.status = "Import"
        self.time = time
        self.descript = descript
        self.print_status = print_status
        self.cancel_status = cancel_status


class courise(Base):
    """ 快递员
    """

    __tablename__ = "courise"

    courise_id = Column(String(20), primary_key=True)
    courise_name = Column(String(10), nullable=False)

# TODO: session
# Session = sessionmaker()
# Session.configure(bind=engine)

engine = create_engine(config.DB_URL)


def init_database():
    Base.metadata.create_all(engine)
    logging.info("Database inited!")


def make_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
