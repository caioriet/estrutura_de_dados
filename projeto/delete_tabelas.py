import sqlite3

def apagar_tabela(db_file, table_name):
    """
    Apaga uma tabela de um banco de dados SQLite.

    Args:
        db_file: O caminho para o arquivo do banco de dados SQLite.
        table_name: O nome da tabela a ser apagada.
    """
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Apaga a tabela
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

        conn.commit()
        print(f"Tabela '{table_name}' apagada com sucesso.")

    except sqlite3.Error as e:
        print(f"Erro ao apagar tabela: {e}")

    finally:
        if conn:
            conn.close()

# Exemplo de uso:
db_file = "C:/Users/Caio Riet/Downloads/Caio Riet/estrutura_de_dados/projeto/db.sqlite3"  # Substitua pelo caminho do seu banco de dados
table_name = "companhias_abertas"  # Substitua pelo nome da tabela que você quer apagar

apagar_tabela(db_file, table_name)
