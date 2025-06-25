from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Exemplar(Base):
    __tablename__ = "exemplar"
    tombo = Column(String, primary_key=True)
    cod_livro = Column(String,ForeignKey('livro.cod_livro'),nullable=False)
    
    livro_associado = relationship("Livro") 



