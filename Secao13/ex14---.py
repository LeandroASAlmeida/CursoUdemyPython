"""
14. Dado um arquivo contendo um conjunto de nome e data de nascimento (DD MM AAAA,
isto é, 3 inteiros em sequência), faça um programa que leia o nome do arquivo e a data 
de hoje e construa outro arquivo contendo o nome e a idade de cada pessoa do primeiro arquivo.

"""



try: #criando arquivo caso não exista
    arquivo_ex14 = str(input('Nome do arquivo a ser editado, coloque o diretorio onde vai ser criado caso não exista:')) #arquivos\arq14.txt
    arquivo = open(arquivo_ex14, 'r+')#ler
except FileNotFoundError:
    arquivo = open(arquivo_ex14, 'w+')#escrever
    arquivo.writelines(u'Arquivo criado pois nao existia\n')


