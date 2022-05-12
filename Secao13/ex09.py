
"""
9) Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo
com o conteúdo dos dois primeiros (o conteúdo do primeiro seguido do conteúdo do
segundo).
"""
arquivo_ex09 = str(input("Informe o caminho do diretorio onde se encontra o arquivo: ")) #arquivos\arq9.txt


with open(arquivo_ex09, "r", encoding="utf-8") as arquivo1:
    arquivo_ex09_2 = str(input("Informe o caminho do diretorio onde se encontra o arquivo: "))#arquivos\arq9_2.txt

    with open(arquivo_ex09_2, "r", encoding="utf-8") as arquivo2:
        with open("arquivos/juncao_arquivos.txt", "w", encoding="utf-8") as arquivo_novo:
            arquivo_novo.write(arquivo1.read()+"\n")
            arquivo_novo.write(arquivo2.read())

print("\nSucesso!")