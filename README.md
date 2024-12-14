Projeto: Gestão de Dados e Visualização Estatística

Descrição Geral

Este projeto é uma aplicação web desenvolvida com o framework Django para exibição e edição de dados armazenados em um banco de dados. O principal objetivo é permitir que os usuários visualizem, editem e salvem dados de forma intuitiva, utilizando uma interface web responsiva e amigável.

Tecnologias Utilizadas

Python: Linguagem de programação utilizada no backend.

Django: Framework web utilizado para a criação da aplicação.

SQLite: Banco de dados relacional utilizado para armazenar os dados.

HTML, CSS e Bootstrap: Para criar uma interface web responsiva.

Funcionalidades Principais

Visualização de Dados:

Os dados são exibidos em uma tabela responsiva gerada dinamicamente no frontend.


Organização e Leitura:

Os nomes das colunas e os dados são carregados dinamicamente do banco de dados para garantir flexibilidade.

Como Executar o Projeto

1. Configuração Inicial

Certifique-se de ter o Python e o pip instalados. Clone este repositório e acesse o diretório do projeto:

# Clone o repositório
git clone <URL-do-repositorio>

# Acesse a pasta do projeto
cd projeto-gestao-dados

2. Crie e Ative um Ambiente Virtual

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate

3. Instale as Dependências

pip install -r requirements.txt

4. Configure o Banco de Dados

Aplique as migrações para criar o banco de dados local:

python manage.py makemigrations
python manage.py migrate

5. Execute o Servidor

Inicie o servidor de desenvolvimento:

python manage.py runserver

Acesse a aplicação em http://127.0.0.1:8000.

