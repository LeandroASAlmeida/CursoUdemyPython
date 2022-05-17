from csv import writer
from csv import DictWriter
'''
#ESCREVENDO E CRIANDO UM ARQUIVO CSV
with open('filmes.csv','w', encoding='utf-8') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo','Genero','Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do Filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero:')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme,genero,duracao])'''


#DICTWRITER

with open ('filmes3.csv','w',encoding='utf-8') as arquivo:
    cabecalho = ['Titulo', 'Genero', 'Duracao']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme =None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('informe o genero do filme: ')
            duracao = input('Informe a duração do filme: ')
            escritor_csv.writerow({'Titulo':filme, 'Genero':genero, 'Duracao':duracao})