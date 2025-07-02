from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import  relationship
from models import Base
from .exemplar import Exemplar 
from .emprestimo import Emprestimo

class EmpExemplar(Base):
    __tablename__ = "emp_exemplar"
    tombo = Column(String, ForeignKey('exemplar.tombo'),nullable=False, primary_key=True)
    cod_emp = Column(Integer, ForeignKey('emprestimo.cod_emp'),nullable=False, primary_key=True)
    exemplar_associado = relationship(Exemplar)
    emprestimo_associado = relationship(Emprestimo)
