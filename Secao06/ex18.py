'''
Escreva um algoritmo que leia certa quantidade de numeros e imprima o maior deles e 
quantas vezes o maior numero foi lido. A quantidade de numeros a serem lidos deve ser 
fornecida pelo usuario
'''

qtd = int(input('Informe quantos números deseja digitar: '))
qtd_vezes = 0

for i in range(qtd):
    num = int(input(f'Digite n{i + 1}: '))# contador da string "n0"
    if i == 0:
        maior = int(num)
        qtd_vezes = 1
    else:
        if num > maior:
            maior = num
            qtd_vezes = 1
        elif num == maior:
            qtd_vezes += 1 # contador

print('Maior número = {}'.format(maior))
print('Número de vezes = {}'.format(qtd_vezes))
