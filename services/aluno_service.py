from sqlalchemy.orm import Session
from models.aluno import Aluno 

class AlunoService:
    def __init__(self, db: Session):
        self.db = db

    def criar_aluno(self, mat_aluno: str, nome: str, email: str, curso: str):
        novo_aluno = Aluno(mat_aluno=mat_aluno, nome=nome, email=email, curso=curso)
        self.db.add(novo_aluno)
        self.db.commit()
        self.db.refresh(novo_aluno)
        return novo_aluno

    def listar_alunos(self):
        return self.db.query(Aluno).all()

    def buscar_aluno_por_id(self, mat_aluno: str):
        return self.db.query(Aluno).filter(Aluno.mat_aluno == mat_aluno).first()

    def atualizar_aluno(self, mat_aluno: str, nome: str = None, email: str = None, curso: str = None):
        aluno = self.buscar_aluno_por_id(mat_aluno)
        if aluno:
            if nome:
                aluno.nome = nome
            if email:
                aluno.email = email
            if curso:
                aluno.curso = curso
            self.db.commit()
            self.db.refresh(aluno)
        return aluno

    def remover_aluno(self, mat_aluno: str):
        aluno = self.buscar_aluno_por_id(mat_aluno)
        if aluno:
            self.db.delete(aluno)
            self.db.commit()
            return True
        return False