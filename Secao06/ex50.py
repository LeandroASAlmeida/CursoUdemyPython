'''
Chico tem 1.50 metro e cresce 2 centımetros por ano, enquanto Ze tem 1.10 metros e 
cresce 3 centımetros por ano. Escreva um programa que calcule e imprima quantos anos
serao necessarios para que Ze seja maior que Chico.

'''

chico = 1.50
ze = 1.10
anos= 0

while True:
    chico += 0.2  # chico recebe 2cm ( 150 + 2 = 152)
    ze += 0.3 # zé  recebe 3cm (110 + 3 = 113)
    if ze >= chico: # ze é maior ou igual a chico? .. não ,,então numero de anos  acrescenta mais um.( vai fazendo a comparação  e vai acrescentando até ser maior ou igual;)
        print('Levou {} anos para que Zé ultrapassasse Chico'.format(anos))
        break
    anos +=1





