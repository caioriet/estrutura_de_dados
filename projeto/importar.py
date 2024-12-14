# Importa as bibliotecas necessárias

import requests  # Para fazer requisições HTTP e baixar arquivos da web
import pandas as pd  # Para manipulação e análise de dados em formato tabular
import sqlite3  # Para interagir com bancos de dados SQLite
from pathlib import Path  # Para trabalhar com caminhos de arquivos de forma mais robusta
import zipfile  # Para manipular arquivos ZIP

# URLs dos arquivos de dados a serem baixados
URL_CIA_ABERTA = "https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv"  # URL do arquivo CSV com dados de companhias abertas
URL_FRE_ZIP = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/FRE/DADOS/fre_cia_aberta_2024.zip"  # URL do arquivo ZIP com dados do FRE

# Cria um diretório chamado "data" para armazenar os arquivos baixados, caso ele não exista
DATA_DIR = Path("C:/Users/Caio Riet/Downloads/Caio Riet/estrutura_de_dados/projeto")
DATA_DIR.mkdir(exist_ok=True)

# Dicionário que mapeia nomes de arquivos a seus respectivos caminhos no diretório "data"
CSV_FILES = {
    "companhias_abertas": DATA_DIR / "cad_cia_aberta.csv",  # Caminho para o arquivo CSV de companhias abertas
    "fre_zip": DATA_DIR / "fre_cia_aberta_2024.zip"  # Caminho para o arquivo ZIP do FRE
}

# Caminho para o arquivo do banco de dados SQLite
DB_FILE = DATA_DIR / "db.sqlite3"

# Lista de nomes de arquivos CSV específicos a serem extraídos do arquivo ZIP do FRE
FRE_CSV_FILES = [
    "fre_cia_aberta_empregado_local_faixa_etaria_2024.csv",
    "fre_cia_aberta_empregado_local_declaracao_raca_2024.csv",
    "fre_cia_aberta_empregado_local_declaracao_genero_2024.csv"
]

# Função para baixar dados de uma URL e salvar em um arquivo
def baixar_dados(url, destino):
    """Baixa os dados da URL especificada e salva no destino."""
    print(f"Baixando dados de {url}...")  # Imprime a URL que está sendo baixada
    response = requests.get(url)  # Faz uma requisição GET para a URL
    response.raise_for_status()  # Levanta uma exceção se a requisição falhar
    with open(destino, "wb") as f:  # Abre o arquivo de destino em modo de escrita binária
        f.write(response.content)  # Escreve o conteúdo da resposta no arquivo
    print(f"Dados salvos em {destino}.")  # Imprime o caminho onde os dados foram salvos


# Função para extrair arquivos específicos de um arquivo ZIP
def extrair_arquivos_zip(arquivo_zip, destino, arquivos_desejados):
    """Extrai os arquivos específicos de um ZIP para o diretório especificado."""
    print(f"Extraindo arquivos desejados de {arquivo_zip} para {destino}...")  # Imprime os arquivos e diretório
    with zipfile.ZipFile(arquivo_zip, 'r') as zip_ref:  # Abre o arquivo ZIP em modo de leitura
        for file_name in arquivos_desejados:  # Itera sobre a lista de arquivos desejados
            if file_name in zip_ref.namelist():  # Verifica se o arquivo existe no ZIP
                zip_ref.extract(file_name, destino)  # Extrai o arquivo para o diretório de destino
                print(f"Extraído: {file_name}")  # Imprime o nome do arquivo extraído
    print(f"Arquivos desejados extraídos para {destino}.")  # Imprime o diretório onde os arquivos foram extraídos


# Função para ler um arquivo CSV e salvar os dados em uma tabela de um banco de dados SQLite
def processar_csv_para_sqlite(arquivo_csv, banco_dados, tabela):
    """Lê o CSV e salva os dados no banco de dados SQLite."""
    print(f"Processando {arquivo_csv} e salvando na tabela '{tabela}' no banco {banco_dados}...")  # Imprime informações sobre o processo
    df = pd.read_csv(arquivo_csv, sep=";", encoding="latin1")  # Lê o arquivo CSV usando pandas com o separador ';' e codificação 'latin1'

    with sqlite3.connect(banco_dados) as conn:  # Estabelece uma conexão com o banco de dados SQLite
        df.to_sql(tabela, conn, if_exists="replace", index=False)  # Salva o DataFrame como uma tabela no banco de dados, substituindo a tabela se ela já existir

    print(f"Dados salvos na tabela '{tabela}' no banco {banco_dados}.")  # Imprime a confirmação de que os dados foram salvos


# Função principal que executa o script
def main():
    # Baixa os dados se os arquivos ainda não existirem
    if not CSV_FILES["companhias_abertas"].exists():  # Verifica se o arquivo CSV de companhias abertas já existe
        baixar_dados(URL_CIA_ABERTA, CSV_FILES["companhias_abertas"])  # Baixa o arquivo se ele não existir
    else:
        print(f"Arquivo {CSV_FILES['companhias_abertas']} já existe. Pulando download.")  # Imprime uma mensagem informando que o arquivo já existe

    if not CSV_FILES["fre_zip"].exists():  # Verifica se o arquivo ZIP do FRE já existe
        baixar_dados(URL_FRE_ZIP, CSV_FILES["fre_zip"])  # Baixa o arquivo se ele não existir
        extrair_arquivos_zip(CSV_FILES["fre_zip"], DATA_DIR, FRE_CSV_FILES)  # Extrai os arquivos desejados do ZIP
    else:
        print(f"Arquivo {CSV_FILES['fre_zip']} já existe. Pulando download.")  # Imprime uma mensagem informando que o arquivo já existe

    # Processa os arquivos CSV e salva os dados no banco de dados SQLite
    processar_csv_para_sqlite(CSV_FILES["companhias_abertas"], DB_FILE, "companhias_abertas")  # Processa o arquivo CSV de companhias abertas

    # Processa os arquivos CSV extraídos do ZIP do FRE
    for csv_file in FRE_CSV_FILES:  # Itera sobre a lista de arquivos CSV do FRE
        arquivo_path = DATA_DIR / csv_file  # Cria o caminho completo para o arquivo CSV
        if arquivo_path.exists():  # Verifica se o arquivo existe
            tabela_nome = csv_file.replace(".csv", "").replace("fre_cia_aberta_empregado_local_", "")  # Define o nome da tabela no banco de dados
            processar_csv_para_sqlite(arquivo_path, DB_FILE, tabela_nome)  # Processa o arquivo CSV e salva os dados na tabela
        else:
            
            print(f"Aviso: Arquivo {csv_file} não encontrado no diretório {DATA_DIR}.")  # Imprime um aviso se o arquivo não for encontrado


# Executa a função main() se o script for executado diretamente
if __name__ == "__main__":
    main()