from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from models import Base
DATABASE_URL = "postgresql+psycopg2://postgres:!V123c1234@localhost:5432/lib_bd" # Substitua pelos seus dados

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
