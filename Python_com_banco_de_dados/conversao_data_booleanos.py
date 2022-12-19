import sqlite3 as conector
from modelo import Pessoa

try:
    # Abertura da conexão e aquisiçao do cursor
    conexao = conector.connect("./meu_banco.db", detect_types=conector.PARSE_DECLTYPES)
    cursor = conexao.cursor()

    """
    Se estivéssemos utilizando o BD PostgreSQL com o conector psycopg2,
    como os tipos DATE e BOOLEAN são suportados, esses valores seriam convertidos
    para o tipo correto. 
    Conversão para o sqlite3:
    --> Precisamos passar o argumento PARSE_DECLTYPES para o parâmetro detect_types (linha 4)
    --> Os tipos DATE e TIMESTAMP já possuem conversores embutidos no sqlite3, porém
    o tipo BOOLEAN não.
    --> Precisamos definir e registrar a função conversora utilizando a função register_converter
    --> reggister_converter espera, como primeiro parâmetro, uma stringg com o tipo da coluna
    a ser convertido e, como segundo parâmetro, uma função que recebe o dado e retorna esse
    dado convertido.
    """
    # Funções conversoras
    def conv_bool(dado):
        return True if dado == 1 else False

    # Registro de conversores
    conector.register_converter("BOOLEAN", conv_bool)

    # Definição dos comandos
    comando = '''SELECT * FROM Pessoa WHERE oculos=:usa_oculos;'''
    cursor.execute(comando, {"usa_oculos": True})

    # Recuperação dos registros
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