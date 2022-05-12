
"""
3) Faça um programa que receba do usuário um arquivo texto e mostre na tela
quantas letras são vogais.
"""


def conta_vogais(txt):# função para armazemnar e contar as vogais

    vogais = ['a', 'e', 'i', 'o', 'u']
    txt = txt.lower()# para que a comparação não seja sensível a maiuscula/minuscula
    qtd = 0

    for vogal in vogais:
        qtd += txt.count(vogal)
    return qtd


if __name__ == '__main__':
   
    arquivo_ex03 = str(input("Informe o caminho do diretorio onde se encontra o arquivo: "))  # arquivos\arq3.txt
    
with open(arquivo_ex03, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read() # argumento a ser passado para a função
    print(f"\nO arquivo texto tem {conta_vogais(texto)} vogais!")