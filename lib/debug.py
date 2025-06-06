# lib/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine("sqlite:///freebies.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
# No session = Session() here
