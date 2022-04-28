'''
20. Escreva um programa que leia números inteiros no intervalo [0,50] e os armazene
num vetor com 10 posições. Preencha um segundo vetor apenas com os números
ímpares do primeiro vetor. Imprima os dois vetores, 2 elementos por linha
'''
valores = []
impares = []

for i in range(0,10):
    valores.append(int(input('Digite um número entre 0 a 50: ')))

    if (valores[i] % 2 == 1) and (valores[i] not in impares):
        impares.append(valores[i])

print(f'\nVetor:')
for i in range(len(valores)):
    if i % 2 == 0:
        print(valores[i], end=' ')
    else:
        print(valores[i])

print(f'\nNúmeros ímpares: ')
for i in range(len(impares)):
    if i % 2 == 0:
        print(impares[i], end=' ')
    else:
        print(impares[i])