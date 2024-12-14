import sqlite3

def dados():
    conn = sqlite3.connect('C:/Users/Caio Riet/Downloads/Caio Riet/estrutura_de_dados/projeto/db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM companhias_abertas")
    registros = cursor.fetchall() # Retorna uma lista de tuplas
    for registro in registros:
        print(registro)
    conn.close()       
    

dados()