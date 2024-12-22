# Aplicação Web Django

  Este é um aplicativo web construído com o framework Django. Ele permite que os usuários extraiam, manipulem e visualizem dados de empresas abertas disponíveis nos sites abaixo:
  https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/
  https://dados.cvm.gov.br/dataset/cia_aberta-doc-fre

## Primeiros Passos

  Para iniciar este aplicativo, você precisará seguir os passos abaixo:

### 1. Configure um ambiente virtual

  Antes de clonar o projeto no github e instalar as dependências necessárias, é recomendável criar um ambiente virtual para isolar as dependências do projeto de outros projetos Python em seu sistema.

#### Criando um ambiente virtual

  Você pode criar um ambiente virtual usando venv.
  
  cmd
  python3 -m venv venv
  
#### Ativando o ambiente virtual
  Antes de trabalhar em seu projeto, você precisa ativar o ambiente virtual.
  
  cmd
  venv\Scripts\activate
  
  Após a ativação, você notará que o prompt de comando mudará para indicar que você está agora em um ambiente virtual.

### 2. Clone o repositório

  Agora, clone este repositório para sua máquina local usando o comando:
  
  cmd
  git clone https://github.com/caioriet/estrutura_de_dados.git
  
  Isso criará uma cópia do repositório em seu diretório atual.
  
### 3. Instale as dependências

  Este projeto tem suas dependências listadas em um arquivo requirements.txt. Para instalar as bibliotecas necessárias, execute o seguinte comando no terminal:

  cmd
  pip install -r requirements.txt
  
  Isso instalará todas as bibliotecas listadas no arquivo requirements.txt em seu ambiente virtual.

### 4. Importar dados
  Este projeto vem com um script para importar dados para o banco de dados. Para importar os dados, você precisará executar o seguinte comando no diretório raiz do projeto:
  
  cmd
  python importar.py
  
  Isso importará os dados do arquivo importar.py para o banco de dados db.sqlite3.
  
### 5. Inicialize o aplicativo Django
  Para iniciar o aplicativo Django, você precisará executar o seguinte comando no diretório raiz do projeto:
  
  cmd 
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
  
  Isso iniciará o servidor de desenvolvimento Django. Você pode acessar o aplicativo navegando até http://127.0.0.1:8000/ em seu navegador da web.

## Uso
  Esse sistema criado em django permite que o usuário crie, visualize, atualize e delete(CRUD) um registro do banco de dados através de uma aplicação web.
  Esse sistema também conta com uma sessão de dashboard que mostra:
  ▪ Distribuição percentual de funcionários por gênero.
  ▪ Distribuição percentual de funcionários por raça.
  ▪ Distribuição percentual de funcionários por faixa etária.

## Tecnologias utilizadas
  Para criar essa aplicação, foi utilizado
  Liguagens de programação:
    Python
    HTML 
    CSS 
    Javascripts
  
  Frameworks principais:
    Django
    Pandas
    Requests
    Bootstrap
    Plotly.js
  
  Banco de dados: 
    Sqlite3 

# Contato
Se você tiver alguma dúvida, sinta-se à vontade para entrar em contato comigo em caiorietb@gmail.com
