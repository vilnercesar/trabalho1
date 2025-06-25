from sqlalchemy.orm import Session
from models.livro import Livro 

class LivroService:
    def __init__(self, db: Session):
        self.db = db

    def criar_livro(self, cod_livro: str, titulo: str, autor: str, ano: int):
        novo_livro = Livro(cod_livro=cod_livro, titulo=titulo, autor=autor, ano=ano)
        self.db.add(novo_livro)
        self.db.commit()
        self.db.refresh(novo_livro)
        return novo_livro

    def listar_livros(self):
        return self.db.query(Livro).all()

    def buscar_livro_por_id(self, cod_livro: str):
        return self.db.query(Livro).filter(Livro.cod_livro == cod_livro).first()

    def atualizar_livro(self, cod_livro: str, titulo: str = None, autor: str = None, ano: int = None):
        livro = self.buscar_livro_por_id(cod_livro)
        if livro:
            if titulo is not None:
                livro.titulo = titulo
            if autor is not None:
                livro.autor = autor
            if ano is not None:
                livro.ano = ano
            self.db.commit()
            self.db.refresh(livro)
        return livro

    def remover_livro(self, cod_livro: str):
        livro = self.buscar_livro_por_id(cod_livro)
        if livro:
            self.db.delete(livro)
            self.db.commit()
            return True
        return False