"""
Buscar veícuos e suas respectivas marcas
"""
import sqlite3 as conector
from modelo import Veiculo

try:
    # Abertura da conexão e aquisiçao do cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # Definição dos registros
    comando = '''SELECT * FROM Veiculo;'''
    cursor.execute(comando)

    # Recuperação dos dados
    reg_veiculos = cursor.fetchall()
    for reg_veiculos in reg_veiculos:
        veiculo = Veiculo(*reg_veiculos)
        print("Placa:", veiculo.placa, ", Marca:", veiculo.marca)

except conector.DatabaseError as err:
    print("Erro de Banco de Dados", err)
finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()