CREATE TABLE ALUNO(
	mat_aluno VARCHAR (20),
	nome VARCHAR(150) NOT NULL,
	curso VARCHAR(100),
	email VARCHAR(100) NOT NULL UNIQUE,
	PRIMARY KEY(mat_aluno)

);

CREATE TABLE LIVRO ( 
	cod_livro VARCHAR(30),
	titulo VARCHAR(255) NOT NULL,
	autor VARCHAR(150),
	editora VARCHAR(100),
	ano INT,
	PRIMARY KEY(cod_livro)

);

CREATE TABLE EXEMPLAR (
	tombo VARCHAR(20),
	cod_livro VARCHAR(30) NOT NULL,
	PRIMARY KEY(tombo),
	FOREIGN KEY(cod_livro) REFERENCES LIVRO(cod_livro)



);
CREATE TABLE EMPRESTIMO (
    cod_emp SERIAL,
    data_emp DATE NOT NULL,
    data_dev DATE,
    data_prev DATE NOT NULL,
    atraso INT DEFAULT 0,
    mat_aluno VARCHAR(20) NOT NULL,
	PRIMARY KEY(cod_emp),
	FOREIGN KEY (mat_aluno) REFERENCES ALUNO(mat_aluno)
);

CREATE TABLE EMP_EXEMPLAR (
    tombo VARCHAR(20) NOT NULL,
    cod_emp INT NOT NULL,
    PRIMARY KEY (tombo, cod_emp),
    FOREIGN KEY (tombo) REFERENCES EXEMPLAR(tombo),
    FOREIGN KEY (cod_emp) REFERENCES EMPRESTIMO(cod_emp)
);