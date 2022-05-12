"""
12. Abra um arquivo texto, calcule e escreva o número de caracteres, o número de linhas e
o número de palavras neste arquivo. Escreva também quantas vezes cada letra ocorre no arquivo (ignorando letras com acento).
 Obs.: palavras são separadas por um ou mais caracteres espaço, tabulação ou nova linha.
"""


from ex06 import qtd_letras # importando diretamente a função 


try: #criando arquivo caso não exista
    arquivo_ex12 = str(input('Nome do arquivo a ser editado, coloque o diretorio onde vai ser criado caso não exista:')) #arquivos\arq12.txt
    arquivo = open(arquivo_ex12, 'r+')#ler
except FileNotFoundError:
    arquivo = open(arquivo_ex12, 'w+')#escrever
    arquivo.write(u'Arquivo criado pois nao existia\n') # escreve diretamente no arquivo criado.
    arquivo.write("    O poeta e um fingidor.      \n")
    arquivo.write("    Finge tao completamente     \n")
    arquivo.write("    Que chega a fingir que e dor\n")
    arquivo.write("    A dor que deveras sente.    \n")
    arquivo.write("                Fernando Pessoa.\n")

    with open(arquivo_ex12, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()
        quebra_de_linha = texto.count("\n")
        caracteres = len(texto) - quebra_de_linha

        print(f"\n{caracteres} caracter(es)!")

        print(f"{quebra_de_linha+1} linha(s)!")

        palavras = texto.strip().split()

        print(f"{len(palavras)} palavra(s)!")

        qtd_letras(texto)









