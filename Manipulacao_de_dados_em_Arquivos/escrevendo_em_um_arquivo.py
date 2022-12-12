"""
Modo W: abre o arquivo para escrita, truncando o arquivo em primeiro lugar.
Caso ele não exista, será criado um.
Modo A: abre o arquivo para escrita, acrescentando conteúdo AO FINAL DELE.
Se não existir, será criado um.

Dois métodos para escrita de conteúdo em um arquivo texto
1. write
2. writelines > iterável
"""
arquivo_escrita = open("dados_write.txt", "w")
arquivo_escrita.write("Conteúdo da primeira linha.")
arquivo_escrita.write("\nConteúdo da segunda linha")
arquivo_escrita.close()

linhas = ["Conteúdo wrilines1",
          "\nConteúdo writelines2"]

arquivo_escrita = open("dados_writelines.txt", "w")
arquivo_escrita.writelines(linhas)
arquivo_escrita.close()

