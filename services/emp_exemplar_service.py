
from sqlalchemy.orm import Session
from models.emp_exemplar import EmpExemplar 

class EmprestimoExemplarService:
    def __init__(self, db: Session):
        self.db = db

    def criar_emprestimo_exemplar(self, tombo: str, cod_emp: int):
        novo_registro = EmpExemplar(tombo=tombo, cod_emp=cod_emp)
        self.db.add(novo_registro)
        self.db.commit()
        self.db.refresh(novo_registro)
        return novo_registro

    def listar_emprestimo_exemplares(self):
        return self.db.query(EmpExemplar).all()

    def buscar_emprestimo_exemplar_por_id(self, tombo: str, cod_emp: int):
        
        return self.db.query(EmpExemplar).filter_by(tombo=tombo, cod_emp=cod_emp).first()

    def atualizar_emprestimo_exemplar(self, tombo: str, cod_emp: int, novo_tombo: str = None, novo_cod_emp: int = None):
      
        registro = self.buscar_emprestimo_exemplar_por_id(tombo, cod_emp)
        if registro:
            alterado = False
            if novo_tombo is not None and novo_tombo != registro.tombo:
                registro.tombo = novo_tombo
                alterado = True
            if novo_cod_emp is not None and novo_cod_emp != registro.cod_emp:
                registro.cod_emp = novo_cod_emp
                alterado = True
            
            if alterado:
                self.db.commit()
                self.db.refresh(registro)
            return registro
        return None


    def remover_emprestimo_exemplar(self, tombo: str, cod_emp: int):
        registro = self.buscar_emprestimo_exemplar_por_id(tombo, cod_emp)
        if registro:
            self.db.delete(registro)
            self.db.commit()
            return True
        return False