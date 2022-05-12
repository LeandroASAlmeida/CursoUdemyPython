"""
11) Faça um programa no qual o usuário informa o nome do arquivo e uma palavra,
e retorne o número de vezes que aquela palavra aparece no arquivo.
"""

try: #criando arquivo caso não exista
    arquivo_ex11 = str(input('Nome do arquivo a ser editado, coloque o diretorio onde vai ser criado caso não exista:')) #arquivos\arq11.txt
    arquivo = open(arquivo_ex11, 'r+')#ler
except FileNotFoundError:
    arquivo = open(arquivo_ex11, 'w+')#escrever
    arquivo.writelines(u'Arquivo criado pois nao existia\n')
    arquivo.writelines(u'Texto Lorem Ipsum pode ser utilizado para voce que esta desenvolvendo seu projeto e precisa de texto aleatorio para preencher os espacos e fazer testes') # escreve diretamente no arquivo criado.

    with open(arquivo_ex11, "r", encoding="utf-8") as arquivo:
        palavra = str(input("Digite uma palavra: ")).strip().split()# strip() retorna uma cópia da string com os caracteres iniciais e finais removidos
        texto = arquivo.read().lower()
        print(f"\nA palavra '{palavra[0]}' se repete {texto.count(palavra[0].lower())} vez(es) no texto!")

