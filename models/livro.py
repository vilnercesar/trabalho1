from sqlalchemy import Column, String, Integer

from models import Base

class Livro(Base):
    __tablename__ = "livro"
    cod_livro = Column(String, primary_key=True)
    titulo = Column(String, nullable=False)
    editora = Column(String)
    ano = Column(Integer)