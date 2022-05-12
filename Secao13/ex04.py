
"""
4) Faça um programa que receba do usuário um arquivo texto e mostre na tela
quantas letras são vogais e quantas são consoantes

"""

def conta_vogais(txt):# função para armazemnar e contar as vogais

    vogais = ['a', 'e', 'i', 'o', 'u']
    txt = txt.lower()# para que a comparação não seja sensível a maiuscula/minuscula
    qtd = 0

    for vogal in vogais:
        qtd += txt.count(vogal)
    return qtd

def conta_consoantes(txt):# função para armazemnar e contar as consoantes

        consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                      'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        txt = txt.lower()# para que a comparação não seja sensível a maiuscula/minuscula
        qtd = 0

        for consoante in consoantes:
            qtd += txt.count(consoante)

        return qtd


if __name__ == '__main__':
   
    arquivo_ex04 = str(input("Informe o caminho do diretorio onde se encontra o arquivo: "))  # arquivos\arq4.txt
    
with open(arquivo_ex04, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read() # argumento a ser passado para a função
    print(f"\nO arquivo texto tem {conta_vogais(texto)} vogais, e tem {conta_consoantes(texto)} ")



