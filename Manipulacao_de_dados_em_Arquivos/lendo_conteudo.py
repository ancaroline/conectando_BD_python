"""
Lendo o conteúdo de um arquivo

3 métodos para leitura:
read > retorna todo o conteúdo de um arquivo como uma única string.
readline > retorna uma linha de um arquivo, incluindo caracteres de final de linha (\n ou \r\n)
readlines > retorna uma lista onde cada item da lista é uma linha do arquivo.
"""
arquivo = open("teste.txt", "r")
arquivo1 = open("teste.txt", "r")
arquivo2 = open("teste.txt", "r")

# read
conteudo = arquivo.read()
print("Tipo de conteúdo:", type(conteudo))
print("Conteúdo retornado pelo read:")
print(repr(conteudo)) # função para mostrar o conteúdo real contido da variável conteudo
arquivo.close()

# readline
conteudo = arquivo1.readline()
print("Tipo de conteúdo:", type(conteudo))
print("Conteúdo retornado pelo readline:")
print(repr(conteudo))
proximo_conteudo = arquivo1.readline()
print("Próximo conteúdo retornado pelo readline:")
print(repr(proximo_conteudo))
arquivo.close()

# readlines
conteudo = arquivo2.readlines()
print("Tipo de conteúdo:", type(conteudo))
print("Conteúdo retornado pelo readlines:")
print(repr(conteudo))
arquivo.close()
