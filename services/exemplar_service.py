from sqlalchemy.orm import Session
from models.exemplar import Exemplar

class ExemplarService:
    def __init__(self, db: Session):
        self.db = db

    def criar_exemplar(self, tombo: str, cod_livro_fk: str):
        novo_exemplar = Exemplar(tombo=tombo, cod_livro_fk=cod_livro_fk)
        self.db.add(novo_exemplar)
        self.db.commit()
        self.db.refresh(novo_exemplar)
        return novo_exemplar

    def listar_exemplares(self):
        return self.db.query(Exemplar).all()

    def buscar_exemplar_por_id(self, tombo: str):
        return self.db.query(Exemplar).filter(Exemplar.tombo == tombo).first()

    def atualizar_exemplar(self, tombo: str, cod_livro_fk: str = None):
        exemplar = self.buscar_exemplar_por_id(tombo)
        if exemplar:
            if cod_livro_fk is not None:
                exemplar.cod_livro_fk = cod_livro_fk
            self.db.commit()
            self.db.refresh(exemplar)
        return exemplar

    def remover_exemplar(self, tombo: str):
        exemplar = self.buscar_exemplar_por_id(tombo)
        if exemplar:
            self.db.delete(exemplar)
            self.db.commit()
            return True
        return False