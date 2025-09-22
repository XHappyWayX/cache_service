from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

DATABASE = DATABASE_URL
if DATABASE is None:
    raise RuntimeError("DATABASE_URL environment variable must be set")

engine = create_engine(DATABASE)
Session = sessionmaker(bind=engine)
session = Session()
