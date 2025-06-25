from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Emprestimo(Base):
    __tablename__ = "emprestimo"
    cod_emp = Column(Integer, primary_key=True)
    data_emp = Column(DateTime, nullable=False)
    data_dev = Column(DateTime)
    data_prev = Column(DateTime, nullable=False)
    atraso = Column(Integer, default=0)
    mat_aluno = Column(String, nullable=False)

#definir as chaves estrangeiras

