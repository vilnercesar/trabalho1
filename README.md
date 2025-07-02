# Modelagem Relacional e Integração com ORM (PostgreSQL + Python)

Este projeto é uma aplicação Python que demonstra a integração com um banco de dados relacional PostgreSQL utilizando o ORM SQLAlchemy. O objetivo é consolidar conhecimentos em modelagem relacional e aplicar práticas modernas de desenvolvimento para interagir com um esquema de banco de dados de biblioteca previamente existente.

## Tecnologias Utilizadas

* **Python 3.x:** Linguagem de programação principal.
* **PostgreSQL:** Sistema de gerenciamento de banco de dados relacional.
* **SQLAlchemy:** ORM (Object-Relational Mapping) para interação com o banco de dados.
* **psycopg2:** Adaptador PostgreSQL para Python, utilizado pelo SQLAlchemy.

## Pré-requisitos

Para executar este projeto **do zero**, você precisará ter o seguinte instalado em sua máquina:

1.  **Python 3.x:** Recomenda-se a versão 3.8 ou superior.
    * [Baixar Python](https://www.python.org/downloads/)
2.  **PostgreSQL:** O servidor de banco de dados onde sua base de dados `lib_bd` reside.
    * [Baixar PostgreSQL](https://www.postgresql.org/download/)
3.  **pgAdmin (Opcional, mas Recomendado):** Uma ferramenta gráfica para gerenciar seu banco de dados PostgreSQL.
    * [Baixar pgAdmin](https://www.pgadmin.org/download/)

## Configuração do Ambiente e Execução do Projeto do Zero

Siga os passos abaixo para configurar e rodar o projeto em sua máquina, partindo de um ambiente limpo.

### 1. Clonar o Repositório

Primeiro, clone o repositório do GitHub para o seu ambiente local:

```bash
git clone https://github.com/vilnercesar/trabalho1.git
cd trabalho1
```

### 2.  Criar e Ativar o Ambiente Virtual
É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.

```bash
python -m venv venv
```
**Para ativar o ambiente virtual:**
* **Windows (PowerShell):**
  ```bash
  .\venv\Scripts\activate
  ```
  * Se você encontrar um erro relacionado à política de execução de scripts (.ps1), pode ser necessário alterar a política temporariamente. Abra o PowerShell como administrador e execute:
  ```bash
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
  Confirme com `S` (Sim) e tente ativar o ambiente novamente.
  
    
### 3. Instalar as Dependências Python
Com o ambiente virtual ativado, instale as bibliotecas Python necessárias. Um arquivo ```requirements.txt``` foi fornecido para facilitar a instalação:
```bash
pip install -r requirements.txt
```

### 4. Configuração do Banco de Dados PostgreSQL
Este projeto interage com um banco de dados PostgreSQL chamado ```lib_bd```. Você precisará ter este banco de dados e seu esquema (tabelas e relacionamentos) configurados em seu servidor PostgreSQL.

#### 1. Criar o Banco de Dados ```lib_bd```:
Se o banco de dados ```lib_bd``` ainda não existir no seu servidor PostgreSQL, crie-o. Você pode usar o pgAdmin ou o cliente de linha de comando ```psql```.
```bash
# Conecte-se ao seu servidor PostgreSQL (ex: como usuário 'postgres')
psql -U postgres

# Dentro do psql, crie o banco de dados
CREATE DATABASE lib_bd;
\q # Para sair do psql
```

#### 2. Restaurar o Esquema e Popular os Dados:
Este repositório contém os arquivos SQL ```bd.sql``` (para o esquema da base de dados) e ```dados.sql``` (para popular as tabelas com dados de exemplo) na pasta ```database/```. Você precisará restaurar o esquema e, opcionalmente, popular os dados para o seu banco de dados ```lib_bd```.

* Verifique a pasta ```database/``` no repositório clonado.

* Abra o terminal e navegue até a raiz do seu projeto (```trabalho1```).

* Execute os comandos ```psql``` para restaurar o esquema e os dados (substitua ```postgres``` pelo seu usuário do DB, se for diferente):
```bash
# Primeiro, restaure o esquema do banco de dados
psql -U postgres -d lib_bd -f database/bd.sql

# Em seguida, se desejar, popule o banco de dados com dados de exemplo
psql -U postgres -d lib_bd -f database/dados.sql
```

* Se for solicitada uma senha, digite a senha do usuário do seu PostgreSQL.

### 5. Configuração do Projeto (```db.py```)
O arquivo ```db.py``` contém a configuração da conexão com o banco de dados. Você precisará atualizar a ```DATABASE_URL``` com suas credenciais.

Abra o arquivo ```trabalho1/db.py``` e edite a linha ```DATABASE_URL```:

```bash
# trabalho1/db.py

DATABASE_URL = "postgresql+psycopg2://seu_usuario:sua_senha@localhost:5432/lib_bd"
```
* Substitua seu_usuario pelo nome de usuário do seu PostgreSQL (ex: postgres).

* Substitua sua_senha pela senha correspondente.

* localhost:5432 é o endereço e porta padrão para o PostgreSQL. Mantenha se o seu PostgreSQL estiver rodando localmente na porta padrão.

* lib_bd é o nome do banco de dados que você criou.

## Execução do Projeto

Para testar a aplicação e executar as operações CRUD de exemplo, navegue até o diretório raiz do projeto no seu terminal (com o ambiente virtual ativado) e execute o script ```main.py```:

```bash
.\venv\Scripts\activate # Ativa o ambiente virtual no Windows
python main.py
```
