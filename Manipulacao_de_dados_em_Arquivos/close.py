"""
Fechando um arquivo
> Liberar memória alocada pelo interpretdor e o uso do arquivo por outros programas
"""
arquivo = open("teste.txt")
print("Arquivo fechado?", arquivo.closed)

arquivo.close()
print("Arquivo fechado?", arquivo.closed)