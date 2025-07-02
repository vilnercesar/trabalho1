from db import SessionLocal
from models.aluno import Aluno
from services.aluno_service import AlunoService # Importe o serviço

def main():
    db = SessionLocal()
    aluno_service = AlunoService(db)

    try:
        # Exemplo de leitura de todos os alunos 
        print("--- Listando Alunos ---")
        alunos = aluno_service.listar_alunos()
        if not alunos:
            print("Nenhum aluno encontrado. Adicionando um para teste...")
            # Exemplo de criação de aluno
            aluno_criado = aluno_service.criar_aluno("2023001", "Maria Silva", "maria.silva@example.com", "Engenharia")
            print(f"Aluno criado: {aluno_criado.nome}")
            alunos = aluno_service.listar_alunos() # Lista novamente

        for aluno in alunos:
            print(f"Matrícula: {aluno.mat_aluno}, Nome: {aluno.nome}, Email: {aluno.email}, Curso: {aluno.curso}")

        # Exemplo de busca por ID
        print("\n--- Buscando Aluno por ID ---")
        aluno_encontrado = aluno_service.buscar_aluno_por_id("2023001")
        if aluno_encontrado:
            print(f"Aluno encontrado: {aluno_encontrado.nome}")
        else:
            print("Aluno não encontrado.")

        # Exemplo de atualização
        print("\n--- Atualizando Aluno ---")
        aluno_atualizado = aluno_service.atualizar_aluno(mat_aluno="2023001", nome="Maria Silva Atualizada", curso="Ciência da Computação")
        if aluno_atualizado:
            print(f"Aluno atualizado: {aluno_atualizado.nome}, Curso: {aluno_atualizado.curso}")
        else:
            print("Aluno não encontrado para atualização.")

        # Exemplo de remoção (descomente para testar a remoção)
        # print("\n--- Removendo Aluno ---")
        # if aluno_service.remover_aluno("2023001"):
        #     print("Aluno removido com sucesso.")
        # else:
        #     print("Erro ao remover aluno ou aluno não encontrado.")

        # Testar listar novamente após remoção (se descomentou a remoção)
        # print("\n--- Listando Alunos Após Remoção ---")
        # for aluno in aluno_service.listar_alunos():
        #     print(f"Matrícula: {aluno.mat_aluno}, Nome: {aluno.nome}")

    finally:
        db.close()

if __name__ == "__main__":
    main()