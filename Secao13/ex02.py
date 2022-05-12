"""
2) Faça um programa que receba do usuário um arquivo texto e mostre na tela
quantas linhas esse arquivo possui
"""

# colocando o caminho do arquivo e jogando ele em uma variavel.

arquivo_ex02 = str(input("Informe o caminho do diretorio onde se encontra o arquivo: "))  # arquivos\arq2.txt
                    
with open(arquivo_ex02, "r", encoding='utf-8') as arquivo: # 'r' abre para leitura (padrão)
    texto = arquivo.read() # texto aberto para leitura
    num= len(texto.splitlines()) # splitlines= retorna numero de linhas contando com linhas em branco
    print(f"\nO arquivo possui {num} linhas!")


