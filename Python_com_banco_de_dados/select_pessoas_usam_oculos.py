import sqlite3 as conector
from modelo import Pessoa

try:
    # Abertura da conexão e aquisiçao do cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # Definição dos registros
    comando = '''SELECT * FROM Pessoa WHERE oculos=:usa_oculos;'''
    cursor.execute(comando, {"usa_oculos": True})

    # Recuperação dos dados
    registros = cursor.fetchall()
    for registro in registros:
        pessoa = Pessoa(*registro)
        print("cpf:", type(pessoa.cpf), pessoa.cpf)
        print("nome:", type(pessoa.nome), pessoa.nome)
        print("nascimento:", type(pessoa.data_nascimento), pessoa.data_nascimento)
        print("oculos:", type(pessoa.usa_oculos), pessoa.usa_oculos)

except conector.DatabaseError as err:
    print("Erro de Banco de Dados", err)
finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()