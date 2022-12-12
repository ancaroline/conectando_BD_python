"""
Para ler o conteúdo de um arquivo mais de uma vez:
1. Fechar e abrir novamente o arquivo
2. Utilizar o método seek(n)
A chamada seek(0) retorna o cursor para o início do arquivo
"""
arquivo = open("teste.txt", "r")
conteudo = arquivo.read()
print("Todo o conteúdo do arquivo")
print(repr(conteudo), '\n')

conteudo_releitura = arquivo.read()
print("Releitura de todo o conteúdo do arquivo")
print(repr(conteudo_releitura), '\n')  # conteudo virá vazio
arquivo.close()

# releitura de forma correta:
arquivo_reaberto = open("teste.txt", "r")
conteudo_reaberto = arquivo_reaberto.read()
print("Todo o conteúdo do arquivo novamente")
print(repr(conteudo_reaberto), '\n')

arquivo_reaberto.seek(0)
conteudo_seek = arquivo_reaberto.read()
print("Todo o conteúdo do arquivo após o SEKK")
print(repr(conteudo_seek))

arquivo_reaberto.close()
