# Imports
from sqlalchemy import create_engine, Column, Integer, String, DateTime, \
    ForeignKey, event
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation
from sqlalchemy.ext.declarative import declarative_base

from flask import url_for, Markup
from datetime import datetime

from db_interaction import app, search

engine = create_engine(('sqlite:///C:\\Users\\Sam\\PycharmProjects\\PyLearning-Projects\\db_interaction\\20_Questions.sqlite'))

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflus=False,
                                         bind=engine))





def init_db():


