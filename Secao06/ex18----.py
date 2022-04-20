'''
Escreva um algoritmo que leia certa quantidade de numeros e imprima o maior deles e 
quantas vezes o maior numero foi lido. A quantidade de numeros a serem lidos deve ser 
fornecida pelo usuario
'''

qtd= int(input('Entre com a quantidade de números a serem lidos: '))-----
maior = float('-inf') # vai criar um número infinito
cont = {}
for _ in range(qtd):
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
    c = cont.get(num, 0)
    cont[num] = c + 1

print(f'O maior valor é {maior} e ele ocorre {cont[maior]} vezes')
