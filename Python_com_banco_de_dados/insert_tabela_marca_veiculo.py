import sqlite3 as conector
from modelo import Marca, Veiculo

try:
    conexao = conector.connect("./meu_banco.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()
    # Inserção de dados na tabela Marca
    comando1 = '''INSERT INTO Marca (nome, sigla) VALUES (:nome, :sigla);'''
    marca1 = Marca("Marca A", "MA")
    cursor.execute(comando1, vars(marca1))
    marca1.id = cursor.lastrowid

    marca2 = Marca("Marca B", "MB")
    cursor.execute(comando1, vars(marca2))
    marca2.id = cursor.lastrowid

    # Inserção de dados na tabela Veiculo
    comando2 = '''INSERT INTO Veiculo
                    VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca);'''
    veiculo1 = Veiculo("AAA0001", 2001, "Prata", 1.0, 10000000099, marca1.id)
    veiculo2 = Veiculo("BAA0002", 2002, "Branco", 1.4, 21000000099, marca2.id)
    veiculo3 = Veiculo("CAA0003", 2003, "Preto", 2.0, 20000000099, marca1.id)
    veiculo4 = Veiculo("DAA004", 2004, "Azul", 2.1, 12345678900, marca2.id)

    cursor.execute(comando2, vars(veiculo1))
    cursor.execute(comando2, vars(veiculo2))
    cursor.execute(comando2, vars(veiculo3))

    # Efetivação do comando
    conexao.commit()
except conector.DatabaseError as err:
    print("Erro de Banco de Dados", err)
finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()