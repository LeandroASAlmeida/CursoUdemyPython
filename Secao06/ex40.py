'''
Elabore um programa que faca leitura de varios numeros inteiros, ate que se digite um 
numero negativo. O programa tem que retornar o maior e o menor numero lido.
'''

lido_maior = 0
lido_menor = 0
lidos= 0


while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    if lidos == 0:
        lido_maior, lido_menor = num, num
        lidos = 1
    else:
        if num > lido_maior:
            lido_maior = num
        if num < lido_menor:
            lido_menor = num

print(f'Maior = {lido_maior} \nMenor = {lido_menor} ')

