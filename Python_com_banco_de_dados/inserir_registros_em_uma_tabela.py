import sqlite3 as conector

try:
    # abertura de conexão
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # execução de um comando:
    comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
            VALUES (12345678900, 'Joao', '2000-01-31', 1);'''

    cursor.execute(comando)
    # efetivação do comando
    conexao.commit()
except conector.DatabaseError as err:
    print("Erro de banco de dados", err)
finally:
    # fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()