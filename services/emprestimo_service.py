
from sqlalchemy.orm import Session
from models.emprestimo import Emprestimo
from datetime import datetime 

class EmprestimoService:
    def __init__(self, db: Session):
        self.db = db

    def criar_emprestimo(self, data_emp: datetime, data_prev: datetime, mat_aluno: str, data_dev: datetime = None, atraso: int = 0):
        
        novo_emprestimo = Emprestimo(
            data_emp=data_emp,
            data_prev=data_prev,
            mat_aluno=mat_aluno,
            data_dev=data_dev, 
            atraso=atraso
        )
        self.db.add(novo_emprestimo)
        self.db.commit()
        self.db.refresh(novo_emprestimo)
        return novo_emprestimo

    def listar_emprestimos(self):
        return self.db.query(Emprestimo).all()

    def buscar_emprestimo_por_id(self, cod_emp: int):
        return self.db.query(Emprestimo).filter(Emprestimo.cod_emp == cod_emp).first()

    def atualizar_emprestimo(self, cod_emp: int, data_emp: datetime = None, data_prev: datetime = None, mat_aluno: str = None, data_dev: datetime = None, atraso: int = None):
        emprestimo = self.buscar_emprestimo_por_id(cod_emp)
        if emprestimo:
            if data_emp is not None:
                emprestimo.data_emp = data_emp
            if data_prev is not None:
                emprestimo.data_prev = data_prev
            if mat_aluno is not None:
                emprestimo.mat_aluno = mat_aluno
            if data_dev is not None:
                emprestimo.data_dev = data_dev
            if atraso is not None:
                emprestimo.atraso = atraso
            self.db.commit()
            self.db.refresh(emprestimo)
        return emprestimo

    def remover_emprestimo(self, cod_emp: int):
        emprestimo = self.buscar_emprestimo_por_id(cod_emp)
        if emprestimo:
            self.db.delete(emprestimo)
            self.db.commit()
            return True
        return False