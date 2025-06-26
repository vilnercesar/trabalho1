from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import  relationship
from models import Base
from .livro import Livro
class Exemplar(Base):
    __tablename__ = "exemplar"
    tombo = Column(String, primary_key=True)
    cod_livro = Column(String,ForeignKey('livro.cod_livro'),nullable=False)
    livro_associado = relationship(Livro) 



