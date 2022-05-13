"""
28. Faça um programa que recebe como entrada o nome de um arquivo de entrada e o nome
de um arquivo de saída. Cada linha do arquivo de entrada possui colunas de tamanho de 30 caracteres.
No arquivo de saída deverá ser escrito o arquivo de entrada de forma inversa. Veja um exemplo:

Arquivo de entrada:
Hoje é dia de prova de AP
A prova está muito fácil
Vou tirar uma boa nota

Arquivo de saída:
Aton aob amu rarit uov 
Licát otium átse avorp A
PA ed avorp ed aid é ejoH

"""

entrada = str(input("Digite o caminho do arquivo de entrada ou o seu nome para cria-lo: ")).strip()#local para salvar os arquivos pasta "arquivos/"

entrada = entrada if ".txt" in entrada else entrada+".txt"

with open(entrada, "w", encoding="utf-8") as escreve:
    texto = str(input("\nInsira o texto do arquivo de entrada: ")).strip()

    conteudo = ""

    for palavra in range(len(texto)):
        conteudo += f"{texto[palavra]}\n" if (palavra+1) % 30 == 0 else f"{texto[palavra]}"

    escreve.write(conteudo)

with open(entrada, "r", encoding="utf-8") as leitura:
    saida = str(input("Digite o caminho do arquivo de saida ou o seu nome para cria-lo: ")).strip()

    saida = saida if ".txt" in saida else saida + ".txt"

    with open(saida, "w", encoding="utf-8") as saida:
        saida.write(leitura.read()[::-1])# reverse

