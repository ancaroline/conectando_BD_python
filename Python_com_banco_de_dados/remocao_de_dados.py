import sqlite3 as conector
from modelo import Pessoa

try:
    # Abertura da conexão e aquisiçao do cursor
    conexao = conector.connect("./meu_banco.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    # Definição dos comandos
    # atualizando o valor para true para todos os dados da tabela
    comando = '''DELETE FROM Pessoa WHERE cpf = 21000000099;'''
    cursor.execute(comando)

    # Efeitivação do comando
    conexao.commit()
except conector.DatabaseError as err:
    print("Erro de Banco de Dados", err)
finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()