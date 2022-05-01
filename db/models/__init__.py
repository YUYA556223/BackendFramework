from typing import Any
from flask.app import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative.api import DeclarativeMeta
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

from sqlalchemy.orm.session import Session

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from plugins.reflection.module import Module
from sqlalchemy.ext.declarative import api


class DB:

    # Database path
    """
    データベースsqliteを使って（engine)、database_fileに保存されているdata_dbを使う、またechoで実行の際にsqliteを出す（echo=True)
    engine = create_engine(os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + PATH + "/data.db", convert_unicode=True, echo=True)
    """
    PATH = os.path.abspath(os.path.dirname(__file__))
    engine = create_engine(os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + PATH + "/data.db", convert_unicode=True, echo=True)

    session = scoped_session(sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    ))
    Base = declarative_base()
    Base.query = session.query_property()

    @staticmethod
    def initialize(app: Flask) -> None:
        for module in Module.GetModules("db/models"):
            print("[Database] " + module.Name + " was imported.")
        DB.Base.metadata.create_all(bind=DB.engine)
        print("[Database] Successful database initialization")
        pass
    """ Database settings
    """
