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
# No Linux/Mac:
source venv/bin/activate

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

Estrutura do Projeto

projeto-gestao-dados/
|-- app_visualizacao_estatisticas/
|   |-- migrations/         # Arquivos de migração do banco
|   |-- templates/          # Arquivos HTML
|   |-- static/             # Arquivos CSS e JavaScript
|   |-- views.py            # Funções de controle do backend
|   |-- models.py           # Definição do modelo de dados
|-- db.sqlite3              # Banco de dados SQLite
|-- manage.py               # Arquivo principal para comandos Django
|-- requirements.txt        # Dependências do projeto

Possíveis Erros e Soluções

Erro: "no such table"

Certifique-se de que as migrações do banco de dados foram aplicadas corretamente:

python manage.py makemigrations
python manage.py migrate

Erro: "OperationalError"

Verifique o nome da tabela no banco de dados e ajuste sua view para referenciar corretamente a tabela:

cursor.execute("SELECT * FROM nome_da_tabela")

Erro de Permissão ao Acessar URL:

Certifique-se de que o servidor Django está em execução e que a URL está correta.

Melhorias Futuras

Adicionar autenticação de usuários para proteger a edição de dados.

Implementar filtros para melhorar a navegação na tabela.

Exportar dados para formatos como CSV ou Excel.

Contribuições

São bem-vindas contribuições para melhorias no código, documentação ou novas funcionalidades. Por favor, envie um pull request ou abra uma issue neste repositório.