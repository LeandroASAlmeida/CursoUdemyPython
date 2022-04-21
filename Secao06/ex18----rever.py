'''
Escreva um algoritmo que leia certa quantidade de numeros e imprima o maior deles e 
quantas vezes o maior numero foi lido. A quantidade de numeros a serem lidos deve ser 
fornecida pelo usuario
'''

qtde_numeros = int(input('Informe quantos números deseja digitar: '))
maior, quantas_vezes = int(), 0

for i in range(qtde_numeros):
    num = int(input(f'Digite n{i + 1}: '))
    if i == 0:
        maior = num
        quantas_vezes = 1
    else:
        if num > maior:
            maior = num
            quantas_vezes = 1
        elif num == maior:
            quantas_vezes += 1

print(f'Maior número = {maior}')
print(f'Número de vezes = {quantas_vezes}')
