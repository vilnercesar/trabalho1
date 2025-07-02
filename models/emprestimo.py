from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import  relationship
from models import Base
from .aluno import Aluno
class Emprestimo(Base):
    __tablename__ = "emprestimo"
    cod_emp = Column(Integer, primary_key=True)
    data_emp = Column(DateTime, nullable=False)
    data_dev = Column(DateTime)
    data_prev = Column(DateTime, nullable=False)
    atraso = Column(Integer, default=0)
    mat_aluno = Column(String,ForeignKey('aluno.mat_aluno'),nullable=False)
    aluno_associado = relationship(Aluno) 



