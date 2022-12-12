import sqlite3 as conector

try:
    # abertura de conexão
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # execução de um comando:
    comando = '''CREATE TABLE Marca (
                    id INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    sigla CHARACTER(2) NOT NULL,
                    PRIMARY KEY (id)
                    );'''

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