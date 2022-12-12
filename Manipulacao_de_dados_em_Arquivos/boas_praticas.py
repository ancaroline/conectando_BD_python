"""
Utilizar a palavra reservada with
Garante que o arquivo será fechado adequadamente após utilizarmos o arquivo,
não sendo necessário o método close

with open(caminho, modo) as nome:(codigo indentado)
"""
print("Iterando sobre o arquivo")
with open("teste.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)
    print("Fim do arquivo", arquivo.name)