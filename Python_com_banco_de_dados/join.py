"""
Veiculo tenha acesso ao nome da Marca
"""
import sqlite3 as conector
from modelo import Veiculo, Marca

try:
    # Abertura da conexão e aquisiçao do cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # Definição dos comandos
    comando = '''SELECT
                    Veiculo.placa, Veiculo.ano, Veiculo.cor,
                    Veiculo.motor, Veiculo.proprietario,
                    Marca.nome FROM Veiculo JOIN Marca ON Marca.id = Veiculo.marca;'''
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