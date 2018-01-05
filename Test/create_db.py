from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table import Base

engine = create_engine('sqlite:///orm.db')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
