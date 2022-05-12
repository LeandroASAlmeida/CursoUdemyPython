
"""
5) Faça um programa que receba do usuário um arquivo texto e um caracter. Mostre
na tela quantas vezes aquele caractere ocorre dentro do arquivo.
"""

arquivo_ex05 = str(input("Informe o caminho do diretorio onde se encontra o arquivo: "))  # arquivos\arq5.txt

with open(arquivo_ex05, 'r', encoding='utf-8') as arquivo:
    caractere = str(input("Digite o caractere que você deseja saber a quantidade de vezes que ele "
                            "se repete no arquivo: ")).strip().lower()
    texto = arquivo.read()
    texto = texto.lower()

    print(f"\nO caractere '{caractere}' se repete {texto.count(caractere)} vez(es) no texto!")