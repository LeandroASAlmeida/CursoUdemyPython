'''Escreva um programa que, dada a idade de um nadador, classifique-o em uma das
seguintes categorias:'''

idade = int(input('Informe sua idade: '))

if idade >= 5 and idade <= 7:
    print('Categoria Infantil A')
if idade >= 8  and idade <= 10:
    print('Categoria Infantil B')
if idade >= 11  and idade <= 13:
    print('Categoria Juvenil A')
if idade >= 14  and idade <= 17:
    print('Categoria Juvenil B')
if idade >= 18:
    print('Maior de 18')