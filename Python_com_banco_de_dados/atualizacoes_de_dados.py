import sqlite3 as conector

try:
    # Abertura da conexão e aquisiçao do cursor
    conexao = conector.connect("./meu_banco.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    # Definição dos comandos
    # atualizando o valor para true para todos os dados da tabela
    comando1 = '''UPDATE Pessoa SET oculos = 1;'''
    cursor.execute(comando1)

    comando2 = '''UPDATE Pessoa SET oculos= ? WHERE cpf=10000000099;'''
    cursor.execute(comando2, (False,))

    comando3 = '''UPDATE Pessoa SET oculos= :usa_oculos WHERE cpf= :cpf;'''
    cursor.execute(comando3, {"usa_oculos": False, "cpf": 21000000099})

    # Efeitivação do comando
    conexao.commit()
except conector.DatabaseError as err:
    print("Erro de Banco de Dados", err)
finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()