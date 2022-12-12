import sqlite3 as conector

try:
    # abertura de conexão
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # execução de um comando:
    comando = '''ALTER TABLE Veiculo
                    ADD motor REAL;'''

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
