import sqlite3 as conector
from modelo import Pessoa

try:
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()
    # Criação de um objeto do tipo Pessoa
    pessoa = Pessoa(21000000099, 'Heitor', '1990-01-23', True)
    # Definição de um comando com query parameter
    comando = '''INSERT INTO Pessoa VALUES (:cpf,:nome,:data_nascimento,:usa_oculos);'''
    cursor.execute(comando, vars(pessoa))
    print(vars(pessoa))

    # Efetivação do comando
    conexao.commit()
except conector.DatabaseError as err:
    print("Erro de Banco de Dados", err)
finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()