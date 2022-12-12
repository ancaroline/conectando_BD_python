import sqlite3 as conector

# Abertura da conexão
conexao = conector.connect("URL SQlite")
# Aquisição de um cursor
cursor = conexao.cursor()
# Execução comandos: SELECT, CREATE...
cursor.execute("...")
cursor.fetchall()

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()