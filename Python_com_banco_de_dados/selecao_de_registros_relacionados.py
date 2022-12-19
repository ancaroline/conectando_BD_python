import sqlite3 as conector
from modelo import Veiculo, Marca

try:
    def recuperar_veiculos(conexao, cpf):
        # aquisição do cursor
        cursor = conexao.cursor()

        # definição dos comandos
        comando = '''SELECT * FROM Veiculo
                    JOIN Marca ON Marca.id = Veiculo.marca
                    WHERE Veiculo.proprietario = };'''


except conector.DatabaseError as err:
    print("Erro de Banco de Dados", err)
finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()
