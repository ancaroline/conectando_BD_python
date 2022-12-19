import sqlite3 as conector

try:
    # Abertura da conexão e aquisiçao do cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # Definição dos registros
    comando = '''SELECT nome, oculos FROM Pessoa;'''
    cursor.execute(comando)

    # Recuperação dos dados
    registros = cursor.fetchall()
    print("Tipo retornado pelo fetchall():", type(registros))

    for registro in registros:
        print("Tipo:", type(registro), "- Conteúdo:", registro)

except conector.DatabaseError as err:
    print("Erro de Banco de Dados", err)
finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()