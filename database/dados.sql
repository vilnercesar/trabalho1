-- SCRIPT PARA POPULAR O BANCO DE DADOS DA BIBLIOTECA
-- Autor: Gemini
-- Data: 11 de junho de 2025

-- ETAPA 0: LIMPEZA DAS TABELAS (para poder executar este script várias vezes)
-- O comando TRUNCATE é mais rápido que o DELETE para limpar tabelas inteiras.
-- RESTART IDENTITY reinicia os contadores dos campos SERIAL (como o cod_emp).
-- CASCADE garante que as tabelas dependentes também sejam limpas na ordem correta.
TRUNCATE TABLE ALUNO, LIVRO, EXEMPLAR, EMPRESTIMO, EMP_EXEMPLAR RESTART IDENTITY CASCADE;


-- ETAPA 1: POPULANDO A TABELA ALUNO
INSERT INTO ALUNO (mat_aluno, nome, curso, email) VALUES
('20240078687', 'Vilner César', 'Engenharia de Computação', 'vilner.cesar.110@ufrn.edu.br'),
('20230154987', 'Ana Beatriz Costa', 'Ciência da Computação', 'ana.costa.012@ufrn.edu.br'),
('20220033215', 'Carlos Eduardo Lima', 'Sistemas de Informação', 'carlos.lima.332@ufrn.edu.br'),
('20240098541', 'Mariana Oliveira', 'Engenharia de Software', 'mariana.oliveira.985@ufrn.edu.br'),
('20210045678', 'Juliana Santos', 'Ciência de Dados', 'juliana.santos.456@ufrn.edu.br');


-- ETAPA 2: POPULANDO A TABELA LIVRO
INSERT INTO LIVRO (cod_livro, titulo, autor, editora, ano) VALUES
('004.6 H595p 6.ed.', 'Banco de Dados', 'Heuser, Carlos Alberto.', 'Bookman', 2009),
('005.1 M363s', 'Engenharia de Software', 'Sommerville, Ian', 'Pearson', 2011),
('004 C811i', 'Código Limpo: Habilidades Práticas do Agile Software', 'Martin, Robert C.', 'Alta Books', 2009),
('005.133 P974p', 'Padrões de Projetos: Soluções Reutilizáveis de Software Orientado a Objetos', 'Gamma, Erich et al.', 'Bookman', 2000),
('005.43 T163s', 'Sistemas Operacionais Modernos', 'Tanenbaum, Andrew S.', 'Pearson', 2009);


-- ETAPA 3: POPULANDO A TABELA EXEMPLAR (vários exemplares para alguns livros)
INSERT INTO EXEMPLAR (tombo, cod_livro) VALUES
-- 2 exemplares de 'Banco de Dados'
('20170083632', '004.6 H595p 6.ed.'),
('20180011223', '004.6 H595p 6.ed.'),
-- 3 exemplares de 'Código Limpo'
('20190045678', '004 C811i'),
('20190045679', '004 C811i'),
('20200012345', '004 C811i'),
-- 1 exemplar de 'Engenharia de Software'
('20150098765', '005.1 M363s'),
-- 2 exemplares de 'Sistemas Operacionais Modernos'
('20160054321', '005.43 T163s'),
('20170054322', '005.43 T163s');


-- ETAPA 4: POPULANDO A TABELA EMPRESTIMO
-- Criando alguns empréstimos para diferentes alunos e com diferentes status (ativos e devolvidos)
INSERT INTO EMPRESTIMO (data_emp, data_prev, data_dev, mat_aluno) VALUES
-- Empréstimo 1: Ativo, para Ana Beatriz
('2025-05-20', '2025-06-10', NULL, '20230154987'),
-- Empréstimo 2: Devolvido, para Carlos Eduardo
('2025-04-10', '2025-04-25', '2025-04-24', '20220033215'),
-- Empréstimo 3: Devolvido com atraso, para Mariana Oliveira
('2025-03-01', '2025-03-15', '2025-03-20', '20240098541'),
-- Empréstimo 4: Ativo, com dois livros, para Vilner César
('2025-06-02', '2025-06-22', NULL, '20240078687');


-- ETAPA 5: POPULANDO A TABELA DE JUNÇÃO EMP_EXEMPLAR
-- Ligando os exemplares aos empréstimos. Os códigos de empréstimo (cod_emp) são 1, 2, 3, 4... na ordem em que foram inseridos acima.
INSERT INTO EMP_EXEMPLAR (cod_emp, tombo) VALUES
-- Empréstimo 1 (Ana) pegou 'Código Limpo'
(1, '20190045679'),
-- Empréstimo 2 (Carlos) pegou 'Engenharia de Software'
(2, '20150098765'),
-- Empréstimo 3 (Mariana) pegou 'Sistemas Operacionais'
(3, '20160054321'),
-- Empréstimo 4 (Vilner) pegou 'Banco de Dados' e outro exemplar de 'Código Limpo'
(4, '20170083632'),
(4, '20200012345');


-- ETAPA 6: VERIFICAÇÃO RÁPIDA (OPCIONAL)
-- Conte o número de registros em cada tabela para confirmar a inserção.
SELECT (SELECT COUNT(*) FROM ALUNO) AS total_alunos,
       (SELECT COUNT(*) FROM LIVRO) AS total_livros,
       (SELECT COUNT(*) FROM EXEMPLAR) AS total_exemplares,
       (SELECT COUNT(*) FROM EMPRESTIMO) AS total_emprestimos,
       (SELECT COUNT(*) FROM EMP_EXEMPLAR) AS total_itens_emprestados;