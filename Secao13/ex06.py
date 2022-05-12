"""
6) Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas
vezes cada letra do alfabeto aparece dentro do arquivo.
"""
def qtd_letras(txt):

    txt = txt.lower()
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
              'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print()

    for letra in letras:
        print(f"A letra '{letra}' se repete {txt.count(letra)} vezes no texto")

if __name__ == "__main__":

    try: #criando arquivo caso não exista
        arquivo_ex06 = str(input('Nome do arquivo a ser editado, coloque o diretorio onde vai ser criado caso não exista:')) #arquivos\arq6.txt
        arquivo = open(arquivo_ex06, 'r+')
    except FileNotFoundError:
        arquivo = open(arquivo_ex06, 'w+')
        arquivo.writelines(u'Arquivo criado pois nao existia\n')
        arquivo.writelines(u'Texto Lorem Ipsum pode ser utilizado para voce que esta desenvolvendo seu projeto e precisa de texto aleatorio para preencher os espacos e fazer testes') # escreve diretamente no arquivo criado.

    arquivo.close()

    with open(arquivo_ex06, "r", encoding="utf-8") as arquivo:
            texto = arquivo.read().lower()
            qtd_letras(texto)


