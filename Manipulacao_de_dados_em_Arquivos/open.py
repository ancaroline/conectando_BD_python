"""
arquivo = open(caminho)
"""
import os.path

arquivo = open("teste.txt")  # caminho relativo
print("Arquivo aberto com sucesso!")

print(os.path.relpath(arquivo.name))
print(os.path.abspath(arquivo.name))  # exibir o caminho absoluto
print(arquivo)

"""
Modos de acesso a um arquivo
Principais modos: r:leitura(read) , w:escrita(write), a:acrescentar(append)
x: criar um arquivo para escrita e falha, b: modo binário, t: modo texto,
+: abre arquivo para atualização
modo leitura é o modo padrão
"""
# Atributos de um arquivo [name, mode, closed]

print("Nome do arquivo:", arquivo.name) # nome do arquivo
print("Modo do arquivo:", arquivo.mode) # contém o modo de acesso do arquivo (r, w, a, rb)
print("Arquivo fechado?", arquivo.closed)  # verificar se o arquivo está fechado

arquivo.close()