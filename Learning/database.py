from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLDB_URL = 'sqlite:///./itprogger.db'

engine = create_engine(SQLDB_URL, connect_args={"check_same_thread": False})

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()