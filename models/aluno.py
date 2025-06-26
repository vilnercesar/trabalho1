from sqlalchemy import Column, String
from models import Base


class Aluno(Base):
    __tablename__ = "aluno"
    mat_aluno = Column(String, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    curso = Column(String)