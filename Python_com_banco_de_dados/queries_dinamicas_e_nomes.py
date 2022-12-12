import sqlite3 as conector
from modelo import Pessoa

try:
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()
    # Criação de um objeto do tipo Pessoa
    pessoa = Pessoa(20000000099, 'Arthur', '1990-01-11', False)
    # Definição de um comando com query parameter
    comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) 
                        VALUES (:cpf,:nome,:data_nascimento,:usa_oculos);'''
    cursor.execute(comando, {"cpf": pessoa.cpf,
                             "nome": pessoa.nome,
                             "data_nascimento": pessoa.data_nascimento,
                             "usa_oculos": pessoa.usa_oculos})

    # Efetivação do comando
    conexao.commit()
except conector.DatabaseError as err:
    print("Erro de Banco de Dados", err)
finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()